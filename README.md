# NebulaCache ☁️🌀  
**A distributed cache that refuses to die.**
I built NebulaCache because I wanted to learn how real distributed caches (think Redis Cluster, Memcached, Dynamo-style systems) handle **scaling**, **rebalancing**, and **node failure** — but I also wanted it to be fun to run from the terminal.
NebulaCache is a Python-based, terminal-first, simulated distributed in-memory cache. It uses:
- 🌀 **Consistent hashing** — data is evenly spread across nodes.  
- ❤️ **Replication** — one dead node doesn’t mean heartbreak.  
- 📡 **Gossip protocol** — nodes “talk” behind each other’s backs about who’s alive.  
- ⚡ **Dynamic scaling** — add or remove nodes while everything stays balanced.  
- 🎨 **Rich CLI output** — colorful terminal tables because logs deserve vibes too.
The vibe: *“what if a cache had trust issues and over-communicated?”*
---
## 💻 Features
- Horizontal scalability via consistent hashing  
- Fault-tolerance through replication  
- Self-healing simulation with node failures and recovery  
- Interactive CLI (`put`, `get`, `add-node`, `fail-node`, `show-nodes`, `where`)  
- No servers, no databases — just pure distributed chaos in your terminal  
---
## ⚙️ Quickstart
create and activate a venv (optional)
python -m venv .venv && source .venv/bin/activate
install deps
pip install -r requirements.txt
start a cluster with 3 nodes
python -m cache.cli --nodes 3
Inside the prompt:
> put user:1 "kwame"
> get user:1
> add-node
> show-nodes
> fail-node node-2
> heal-node node-2
> where user:1
> exit
You’ll watch the ring rebalance and data move to healthy nodes — like ants rebuilding a colony after I accidentally kicked it (the ants are Docker containers, for legal reasons).
---
## 🧠 Architecture Overview
User CLI  
│  
├── CacheCluster (manages nodes & hashing)  
│   ├── ConsistentHashRing  → maps keys → nodes  
│   ├── GossipManager       → tracks node health  
│   └── CacheNode           → stores key/value pairs  
│  
└── Rich-powered CLI UI     → displays node health + data placement  
Each key is stored on multiple nodes (replication factor configurable). If a node fails, the next node in the ring instantly takes over responsibility for that range of keys.  
---
## 🧰 Tech Stack
- **Language:** Python 3.11  
- **Libraries:** `asyncio`, `rich`, `argparse`  
- **Infra:** optional Docker Compose for one-command clusters  
---
## 🧩 Example Commands
Add a node to the ring  
> add-node  
Kill a node  
> fail-node node-3  
Heal it again  
> heal-node node-3  
Show who owns a key  
> where user:1  
---
## ☕ Motivation
Redis memes are funny until your cache actually dies. So I built my own — one that scales, heals, gossips, and looks good doing it.  
---
## 🧾 License
MIT — fork it, extend it, or just run it to feel like you’re managing a tiny cloud. PRs welcome.
