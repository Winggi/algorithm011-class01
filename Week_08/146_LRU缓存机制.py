class LinkNode:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.left = None
        self.right = None

class LRUCache:
    def __init__(self, capacity: int):
        self.remained = capacity
        self.hashmap = {}
        self.thead = LinkNode(-1, -1)
        self.ttail = LinkNode(-1, -1)
        self.thead.right = self.ttail
        self.ttail.left = self.thead

    def get(self, key: int) -> int:
        if key not in self.hashmap.keys(): return -1
        node = self.hashmap[key]
        self.move2Head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.hashmap.keys():
            self.remained -= 1
        else:
            self.delNode(self.hashmap[key])
        node = LinkNode(key, value)
        self.add2Head(node)
        self.hashmap[key] = node
        # is full
        if self.remained < 0:
            self.hashmap.pop(self.ttail.left.key)
            self.ttail.left = self.ttail.left.left
            self.ttail.left.right = self.ttail
            self.remained += 1
        return
    
    def move2Head(self, node):
        self.delNode(node)
        self.add2Head(node)

    def delNode(self, node):
        node.left.right, node.right.left = node.right, node.left

    def add2Head(self, node):
        tmp = self.thead.right
        self.thead.right = node
        tmp.left = node
        node.left = self.thead
        node.right = tmp


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)