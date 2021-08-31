class Node:
    def __init__(self, key=0, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

        
class DLList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def push(self, n: Node) -> None:
        n.next = self.head.next
        n.prev = self.head
        self.head.next.prev = n
        self.head.next = n
    
    def remove(self, n: Node) -> None:
        n.prev.next = n.next
        n.next.prev = n.prev
    
    def pop(self) -> Node:
        removed = self.tail.prev
        prev = removed.prev
        prev.next = self.tail
        self.tail.prev = prev
        return removed


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.list = DLList()
    
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.list.remove(node)
        self.list.push(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.list.remove(self.map[key])
            node = Node(key, value)
            self.list.push(node)
            self.map[key] = node
            return
        if self.capacity > 0:
            self.capacity -= 1
        else:
            tail_key = self.list.pop().key
            del self.map[tail_key]

        node = Node(key, value)
        self.list.push(node)
        self.map[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)