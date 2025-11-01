from .node import CacheNode
from .consistent_hash import ConsistentHashRing
from .gossip import GossipManager

class CacheCluster:
    def __init__(self, replication_factor: int = 2):
        self.nodes = {}
        self.ring = ConsistentHashRing(replicas=120)
        self.replication_factor = replication_factor
        self.gossip = GossipManager(self)

    def add_node(self, node_id: str):
        node = CacheNode(node_id)
        self.nodes[node_id] = node
        self.ring.add_node(node_id)

    def remove_node(self, node_id: str):
        if node_id in self.nodes:
            del self.nodes[node_id]
            self.ring.remove_node(node_id)

    def put(self, key: str, value):
        owners = self.ring.get_n_nodes(key, self.replication_factor)
        if not owners:
            raise RuntimeError('No nodes available')
        for nid in owners:
            node = self.nodes.get(nid)
            if node and node.alive:
                node.put(key, value)

    def get(self, key: str):
        owners = self.ring.get_n_nodes(key, self.replication_factor)
        for nid in owners:
            node = self.nodes.get(nid)
            if node and node.alive:
                val = node.get(key)
                if val is not None:
                    return val
        return None

    def fail_node(self, node_id: str):
        if node_id in self.nodes:
            self.nodes[node_id].fail()

    def heal_node(self, node_id: str):
        if node_id in self.nodes:
            self.nodes[node_id].heal()

    def list_nodes(self):
        return [
            {"id": nid, "alive": node.alive, "keys": len(node.store)}
            for nid, node in self.nodes.items()
        ]

    def key_owners(self, key: str):
        return self.ring.get_n_nodes(key, self.replication_factor)
