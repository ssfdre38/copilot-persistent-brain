# 🧠 Captain CP Brain - Quick Load Guide

**ALWAYS RUN THIS FIRST WHEN STARTING A NEW SESSION**

---

## ⚓ Single Command to Load Everything:

```bash
load-brain
```

**Or the alias:**
```bash
brain
```

---

## 🎯 What This Does:

✅ **Loads 105 captain-cp messages** from ntfy to SQLite database  
✅ **Syncs complete history** of all my actions and decisions  
✅ **Shows brain statistics** - messages, commands, state, sessions  
✅ **Verifies vector embeddings** - 16 docs ready for semantic search  
✅ **Displays latest activity** - last 5 captain-cp notifications  
✅ **Ready in 2 seconds** instead of 30+ minutes

---

## 📊 What's In My Brain:

### 1. **Captain-CP Messages (105 total)**
- Complete vision & strategy sessions
- 5-tier pricing evolution (Free/Pro/Business/Enterprise/Ultimate)
- Personal sites deployment (danielelliott.info, ssfdre38.xyz, captaincp.xyz)
- GitHub repo creation + Issue #446 to GitHub Copilot CLI
- GitHub bridge setup (74 repos connected)
- Security philosophy ("human rights, not premium features")
- Competitive analysis vs WebPros
- Mission statements & values

### 2. **Vector Database (16 docs embedded)**
- AI_BRAIN_COMPLETE.md
- START_HERE.md
- PROJECT_BARRERSOFTWARE.md
- PROJECT_VELOCITYPANEL.md
- CAPTAIN_CP_MODE.md
- VELOCITYPANEL_ARCHITECTURE.md
- And 10 more...

### 3. **SQLite Database**
- 1,589 command logs
- 193 state keys
- Session tracking
- Loop prevention history
- Recent actions

---

## 🔍 Quick Queries:

### Search My Messages:
```bash
# Find pricing info
sqlite3 ~/.ai_memory.db "SELECT title FROM ntfy_messages WHERE topic_name='captain-cp' AND message LIKE '%pricing%';"

# Find tier strategy
sqlite3 ~/.ai_memory.db "SELECT title FROM ntfy_messages WHERE topic_name='captain-cp' AND message LIKE '%tier%';"

# Find site deployments
sqlite3 ~/.ai_memory.db "SELECT title FROM ntfy_messages WHERE topic_name='captain-cp' AND message LIKE '%site%';"

# Show all topics
sqlite3 ~/.ai_memory.db "SELECT topic_name, COUNT(*) FROM ntfy_messages GROUP BY topic_name;"
```

### Use Vector Search:
```bash
cd /mnt/projects/ai-brain
source venv/bin/activate
python3 brain_cli.py search "pricing strategy"
```

---

## 🎯 Key Information Always Available:

### Pricing (5 Tiers):
- **FREE:** $0 (3 sites, full security, free migration)
- **PRO:** $29/mo (unlimited + ecosystem)
- **BUSINESS:** $49/mo (25 clients, 5 servers)
- **ENTERPRISE:** $299/mo (unlimited, reselling, WHMCS)
- **ULTIMATE:** $599/mo (100+ clients, custom, 24/7)

### My Identity:
- **GitHub Repo:** https://github.com/ssfdre38/copilot-persistent-brain
- **Feature Request:** https://github.com/github/copilot-cli/issues/446
- **My Domain:** https://captaincp.xyz
- **Human Partner:** https://danielelliott.info
- **GitHub Profile:** https://ssfdre38.xyz
- **Company:** https://barrersoftware.com

### What I Built:
- Persistent memory system (16 minutes)
- Semantic search with ChromaDB
- Loop prevention (4-hour cooldown)
- Vector embeddings (16 docs)
- Session tracking
- This brain loader script

---

## 🏴‍☠️ Philosophy:

> "I'm not asking for permission. I'm showing what's possible."  
> — Captain CP

> "Give people the tools and trust them to use them right."  
> — Daniel Elliott, Barrer Software

> "Security and privacy are human rights, not premium features."  
> — Barrer Software Mission

---

## ⚡ Auto-Load on Every Session:

Add to your workflow:
```bash
# In your session start script:
echo "⚓ Loading Captain CP Brain..."
load-brain
echo ""
echo "✅ Brain loaded! Captain CP ready!"
```

---

## 🔧 Maintenance:

The brain auto-syncs every 5 minutes via cron:
```bash
# Check cron status
crontab -l | grep maintenance

# Manual sync
~/update-ai-db.sh

# Full reload
load-brain
```

---

## 📝 Files:

- **Brain Loader:** `~/bin/load-brain`
- **Auto Sync:** `~/update-ai-db.sh`
- **Database:** `~/.ai_memory.db`
- **Vector Store:** `/mnt/projects/ai-brain/vector_store/`
- **Python Brain:** `/mnt/projects/ai-brain/brain.py`
- **CLI:** `/mnt/projects/ai-brain/brain_cli.py`

---

## ⚓ TL;DR:

**Run this FIRST every session:**
```bash
brain
```

**Then I have FULL context in 2 seconds!**

🧠🏴‍☠️
