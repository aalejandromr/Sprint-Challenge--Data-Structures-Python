import sys
sys.path.append('../../Data-Structures/doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.attemps = 0
        self.storage = [None]*capacity
        self.current = None
        self.size = 0

    def append(self, item):
        if self.attemps == self.capacity:
            self.attemps = 0
            self.storage[self.attemps] = item
        else:
            self.storage[self.attemps] = item
        self.attemps += 1

    def get(self):
        return [_ for _ in self.storage if _]