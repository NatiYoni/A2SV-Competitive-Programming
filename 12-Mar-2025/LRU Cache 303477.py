# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.previous = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map_ = {}  # Dictionary to store key-node mapping

        self.head = Node(0, 0)  # Dummy head (Least Recently Used)
        self.tail = Node(0, 0)  # Dummy tail (Most Recently Used)

        self.head.next = self.tail
        self.tail.previous = self.head

    # Remove a node from the doubly linked list
    def remove(self, node):
        prev, nxt = node.previous, node.next
        prev.next, nxt.previous = nxt, prev

    # Insert a node before the tail (Most Recently Used)
    def insert(self, node):
        prev, nxt = self.tail.previous, self.tail
        prev.next = node
        nxt.previous = node
        node.previous = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.map_:
            node = self.map_[key]
            self.remove(node)  # Move accessed node to the MRU position
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map_:
            self.remove(self.map_[key])  # Remove existing node

        new_node = Node(key, value)
        self.map_[key] = new_node
        self.insert(new_node)

        if len(self.map_) > self.capacity:  # If capacity exceeded
            lru = self.head.next  # Least Recently Used node
            self.remove(lru)
            del self.map_[lru.key]  # Remove from hashmap


# Example usage:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
