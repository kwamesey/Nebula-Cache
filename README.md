# NebulaCache ☁️🌀
**A distributed cache that refuses to die.**

I built NebulaCache to learn how real distributed caches handle scaling, rebalancing, and node failure,
but I wanted to run the whole thing from the terminal and make it fun.

Main ideas:
- Consistent hashing ring
- Replication factor (so one node dying doesn't delete everything)
- Tiny gossip/heartbeat layer
- Interactive CLI (put/get/add-node/fail-node/show-nodes)

```bash
pip install -r requirements.txt
python -m cache.cli --nodes 3
```

Then inside:
```text
> put user:1 "kwame"
> get user:1
> add-node
> show-nodes
```

MIT License.