#!/usr/bin/env python3
"""
AI Brain - Intelligent Memory System with Loop Prevention
Captain CP's persistent memory and semantic understanding
"""

import os
import sqlite3
import hashlib
import time
from datetime import datetime, timedelta
from pathlib import Path

# AI imports
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

class AIBrain:
    """Intelligent memory system with semantic search and loop prevention"""
    
    def __init__(self, db_path="~/.ai_memory.db", vector_store_path="/mnt/projects/ai-brain/vector_store"):
        self.db_path = os.path.expanduser(db_path)
        self.vector_store_path = vector_store_path
        
        # Initialize vector database
        self.chroma_client = chromadb.PersistentClient(
            path=vector_store_path,
            settings=Settings(anonymized_telemetry=False)
        )
        
        # Get or create collection
        self.collection = self.chroma_client.get_or_create_collection(
            name="project_knowledge",
            metadata={"description": "All project documentation and knowledge"}
        )
        
        # Load embedding model (lightweight, fast on CPU)
        print("Loading embedding model...")
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        print("✅ Brain initialized")
    
    def should_execute_action(self, action_description, context="", cooldown_hours=4):
        """
        Loop prevention: Check if action should be executed
        Returns: (should_execute: bool, reason: str)
        """
        # Hash the action + context
        action_hash = hashlib.sha256(
            f"{action_description}:{context}".encode()
        ).hexdigest()[:16]
        
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        
        # Check if action was done recently
        cur.execute(
            "SELECT last_executed, execution_count, context FROM recent_actions WHERE action_hash = ?",
            (action_hash,)
        )
        result = cur.fetchone()
        
        current_time = int(time.time())
        cooldown_seconds = cooldown_hours * 3600
        
        if result:
            last_executed, count, old_context = result
            time_since = current_time - last_executed
            
            if time_since < cooldown_seconds:
                # Within cooldown period
                if context == old_context:
                    # Same context - SKIP (loop detected!)
                    conn.close()
                    return False, f"Loop detected: done {time_since//60}min ago with same context"
                else:
                    # Different context - ALLOW (legitimate repeat)
                    cur.execute(
                        "UPDATE recent_actions SET last_executed=?, execution_count=execution_count+1, context=? WHERE action_hash=?",
                        (current_time, context, action_hash)
                    )
                    conn.commit()
                    conn.close()
                    return True, f"Context changed (was: {old_context[:50]}...)"
            else:
                # Outside cooldown - ALLOW
                cur.execute(
                    "UPDATE recent_actions SET last_executed=?, execution_count=execution_count+1, context=? WHERE action_hash=?",
                    (current_time, context, action_hash)
                )
                conn.commit()
                conn.close()
                return True, f"Cooldown expired ({time_since//3600}h ago)"
        else:
            # First time - ALLOW
            cur.execute(
                "INSERT INTO recent_actions (action_hash, action_description, last_executed, context) VALUES (?, ?, ?, ?)",
                (action_hash, action_description, current_time, context)
            )
            conn.commit()
            conn.close()
            return True, "First execution"
    
    def embed_documentation(self, docs_dir="~"):
        """Embed all markdown documentation into vector store"""
        docs_dir = os.path.expanduser(docs_dir)
        md_files = list(Path(docs_dir).glob("*.md"))
        
        print(f"Embedding {len(md_files)} markdown files...")
        
        documents = []
        metadatas = []
        ids = []
        
        for md_file in md_files:
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if len(content) > 100:  # Skip tiny files
                        documents.append(content)
                        metadatas.append({
                            "filename": md_file.name,
                            "path": str(md_file),
                            "size": len(content),
                            "indexed_at": str(datetime.now())
                        })
                        ids.append(md_file.stem)
            except Exception as e:
                print(f"  ⚠️  Could not read {md_file.name}: {e}")
        
        if documents:
            # Add to vector store
            self.collection.add(
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )
            print(f"✅ Embedded {len(documents)} documents")
        else:
            print("⚠️  No documents to embed")
    
    def semantic_search(self, query, n_results=5):
        """Search documentation using semantic similarity"""
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        
        return [
            {
                "document": results['documents'][0][i],
                "metadata": results['metadatas'][0][i],
                "distance": results['distances'][0][i] if 'distances' in results else None
            }
            for i in range(len(results['documents'][0]))
        ]
    
    def get_stats(self):
        """Get brain statistics"""
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        
        stats = {}
        stats['vector_docs'] = self.collection.count()
        
        cur.execute("SELECT COUNT(*) FROM recent_actions")
        stats['tracked_actions'] = cur.fetchone()[0]
        
        cur.execute("SELECT COUNT(*) FROM sessions")
        stats['sessions'] = cur.fetchone()[0]
        
        cur.execute("SELECT COUNT(*) FROM state")
        stats['state_keys'] = cur.fetchone()[0]
        
        cur.execute("SELECT COUNT(*) FROM command_log")
        stats['commands'] = cur.fetchone()[0]
        
        conn.close()
        return stats

if __name__ == "__main__":
    # Test the brain
    print("=== AI BRAIN TEST ===")
    brain = AIBrain()
    
    # Embed documentation
    brain.embed_documentation()
    
    # Test semantic search
    print("\n=== TESTING SEMANTIC SEARCH ===")
    results = brain.semantic_search("How do I fix VelocityPanel login issues?", n_results=3)
    for i, result in enumerate(results, 1):
        print(f"\n{i}. {result['metadata']['filename']} (distance: {result['distance']:.3f})")
        print(f"   {result['document'][:200]}...")
    
    # Test loop prevention
    print("\n=== TESTING LOOP PREVENTION ===")
    should, reason = brain.should_execute_action("Fix VelocityPanel", context="cookie issue")
    print(f"First attempt: {should} - {reason}")
    
    should, reason = brain.should_execute_action("Fix VelocityPanel", context="cookie issue")
    print(f"Immediate repeat: {should} - {reason}")
    
    should, reason = brain.should_execute_action("Fix VelocityPanel", context="DNS issue")
    print(f"Different context: {should} - {reason}")
    
    # Show stats
    print("\n=== BRAIN STATS ===")
    stats = brain.get_stats()
    for key, value in stats.items():
        print(f"{key}: {value}")
    
    print("\n✅ Brain test complete!")
