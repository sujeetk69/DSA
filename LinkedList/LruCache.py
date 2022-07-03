import random
from collections import deque
from typing import Any, Optional


class Node:
    def __init__(self, key: Any, value: Any):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    """
    An implementation of the LRU Cache
    'get' and 'put' both operations are performed in O(1) time
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.map = dict()
        self.size = 0

    def __str__(self):
        str_rep = "HEAD <-> "
        current = self.head
        while current:
            n = "X"
            p = "X"
            if current.next:
                n = current.next.key
            if current.prev:
                p = current.prev.key
            str_rep += f"[({p}) <- {current.key}: {current.value} -> ({n})] <-> "
            current = current.next
        str_rep += "TAIL"
        return str_rep

    def _insert_first(self, node: Node) -> None:
        if self.head:
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node

    def _delete_last(self) -> Optional[Node]:
        """
        Deletes the last node from the list
        :return:
        """
        deleted_node: Node = None
        if self.tail:
            deleted_node = self.tail
            if deleted_node.prev:
                # List has more than one node
                prev_node = deleted_node.prev
                self.tail = prev_node
                prev_node.next = None
            else:
                # List has only one node
                self.head = None
                self.tail = None
        return deleted_node

    def _delete_node(self, node: Node) -> None:
        """
        Deletes a node from the list by node address
        :return:
        """
        prev_node = node.prev
        next_node = node.next
        if prev_node:
            # This is not the first node
            prev_node.next = next_node
        else:
            # This is the first node, update the head
            self.head = next_node
        if next_node:
            # This is not the last node
            next_node.prev = prev_node
        else:
            # This is the last node, update the tail
            self.tail = prev_node
        node.next = None
        node.prev = None

    def get(self, key: Any) -> Any:
        if key in self.map:
            self._delete_node(self.map[key])
            self._insert_first(self.map[key])
            return self.map[key].value
        return -1

    def put(self, key: Any, value: Any) -> Any:
        if key in self.map:
            # If the key already present then update the value and put the item at the front
            self._delete_node(self.map[key])
            self._insert_first(self.map[key])
            self.map[key].value = value
        else:
            if self.capacity == self.size:
                # Remove the item on tail AND the map
                deleted_node: Node = self._delete_last()
                if deleted_node.key not in self.map:
                    print(f"key = {deleted_node.key}, value = {deleted_node.value}")
                    print(f"Map = {self.map}")
                    # print(f"Cache = {self.__str__()}")
                self.map.pop(deleted_node.key)
                self.size -= 1
            # Key does not exist, create a new node and put at the front
            new_node = Node(key, value)
            self.map[key] = new_node
            self._insert_first(new_node)
            self.size += 1


class LRUCacheBasic:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.cache: dict = dict()
        self.age_q = deque()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.age_q.remove(key)
            self.age_q.appendleft(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.age_q.remove(key)
        else:
            if len(self.cache) == self.capacity:
                lru_key = self.age_q.pop()
                self.cache.pop(lru_key)
        self.age_q.appendleft(key)
        self.cache[key] = value


def stress_test():
    """
    Stress test to troubleshoot the defect which caused the loop in the linked list and subsequent failure
    WARNING: This function uses infinite loop
    :return:
    """
    capacity_range = [1, 2, 3, 4, 5]
    operations = ["get", "put"]
    halt = False
    while True:
        random_capacity = random.choice(capacity_range)
        lru_basic = LRUCacheBasic(random_capacity)
        lru = LRUCache(random_capacity)
        print(f"capacity = {random_capacity}")
        ops_count = int(random.random() * 100)
        ops = []
        for i in range(ops_count):
            op = random.choice(operations)
            key = int(random.random() * 100)  # Random integers between 0 and 100
            if op == "put":
                value = int(random.random() * 100)  # Random integers between 0 and 100
                ops.append((op, key, value))
            else:
                ops.append((op, key))

        for op in ops:
            if op[0] == "put":
                print(f"put({op[1]}, {op[2]})")
                lru.put(op[1], op[2])
                lru_basic.put(op[1], op[2])
            else:
                v1 = lru.get(op[1])
                v2 = lru_basic.get(op[1])
                print(f"get({op[1]}), basic = {v2}, advanced = {v1}")
                if v1 != v2:
                    halt = True
                    break

        if halt:
            break


if __name__ == "__main__":
    print("LRU Cache Implementation")
    # stress_test() # WARNING: this function contains infinite loop to find the bug
    lru = LRUCache(4)
    lru.put(85, 27)
    lru.put(59, 30)
    lru.put(73, 14)
    lru.put(60, 34)
    lru.put(16, 32)
    lru.get(60)
    lru.get(60)
    lru.put(67, 76)
    lru.put(72, 83)
    lru.put(90, 97)
    lru.put(98, 6)


