#!/usr/bin/env python3
"""
Brain CLI - Command-line interface for AI Brain
Usage: brain_cli.py [command] [args]
"""

import sys
from brain import AIBrain

def main():
    if len(sys.argv) < 2:
        print("Usage: brain_cli.py [search|check|stats|embed]")
        sys.exit(1)
    
    brain = AIBrain()
    command = sys.argv[1]
    
    if command == "search":
        if len(sys.argv) < 3:
            print("Usage: brain_cli.py search <query>")
            sys.exit(1)
        query = " ".join(sys.argv[2:])
        results = brain.semantic_search(query, n_results=3)
        print(f"\n🔍 Search results for: {query}\n")
        for i, result in enumerate(results, 1):
            print(f"{i}. {result['metadata']['filename']} (distance: {result['distance']:.3f})")
            print(f"   {result['document'][:150]}...\n")
    
    elif command == "check":
        if len(sys.argv) < 3:
            print("Usage: brain_cli.py check <action> [context]")
            sys.exit(1)
        action = sys.argv[2]
        context = sys.argv[3] if len(sys.argv) > 3 else ""
        should, reason = brain.should_execute_action(action, context)
        print(f"{'✅ ALLOW' if should else '❌ BLOCK'}: {reason}")
    
    elif command == "stats":
        stats = brain.get_stats()
        print("\n📊 Brain Statistics:\n")
        for key, value in stats.items():
            print(f"  {key}: {value}")
        print()
    
    elif command == "embed":
        brain.embed_documentation()
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
