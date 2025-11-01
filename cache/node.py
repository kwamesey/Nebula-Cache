class CacheNode:
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.store = {}
        self.alive = True

    def get(self, key: str):
        if not self.alive:
            raise RuntimeError(f'Node {self.node_id} is down')
        return self.store.get(key)

    def put(self, key: str, value):
        if not self.alive:
            raise RuntimeError(f'Node {self.node_id} is down')
        self.store[key] = value

    def delete(self, key: str):
        if not self.alive:
            raise RuntimeError(f'Node {self.node_id} is down')
        self.store.pop(key, None)

    def fail(self):
        self.alive = False

    def heal(self):
        self.alive = True
