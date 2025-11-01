import hashlib
from bisect import bisect_right

class ConsistentHashRing:
    def __init__(self, replicas: int = 100):
        self.replicas = replicas
        self.ring = {}
        self.sorted_keys = []

    def _hash(self, key: str) -> int:
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)

    def add_node(self, node_id: str):
        for i in range(self.replicas):
            h = self._hash(f"{node_id}:{i}")
            self.ring[h] = node_id
            self.sorted_keys.append(h)
        self.sorted_keys.sort()

    def remove_node(self, node_id: str):
        to_remove = []
        for h, n in self.ring.items():
            if n == node_id:
                to_remove.append(h)
        for h in to_remove:
            del self.ring[h]
            self.sorted_keys.remove(h)

    def get_node(self, key: str):
        if not self.ring:
            return None
        h = self._hash(key)
        idx = bisect_right(self.sorted_keys, h)
        if idx == len(self.sorted_keys):
            idx = 0
        return self.ring[self.sorted_keys[idx]]

    def get_n_nodes(self, key: str, n: int):
        if not self.ring:
            return []
        h = self._hash(key)
        idx = bisect_right(self.sorted_keys, h)
        result = []
        seen = set()
        for _ in range(len(self.sorted_keys)):
            if idx == len(self.sorted_keys):
                idx = 0
            node_id = self.ring[self.sorted_keys[idx]]
            if node_id not in seen:
                result.append(node_id)
                seen.add(node_id)
                if len(result) == n:
                    break
            idx += 1
        return result
