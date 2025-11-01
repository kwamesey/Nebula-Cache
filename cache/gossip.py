import random

class GossipManager:
    def __init__(self, cluster):
        self.cluster = cluster

    def heartbeat(self):
        return {nid: node.alive for nid, node in self.cluster.nodes.items()}

    def random_failure(self, chance: float = 0.0):
        if random.random() < chance and self.cluster.nodes:
            nid = random.choice(list(self.cluster.nodes.keys()))
            self.cluster.nodes[nid].fail()
            return nid
        return None
