from typing import Any, Optional


class Node:
    """
    Node for a doubly linked list
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    An implementation of a doubly linked list
    """
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def __str__(self) -> str:
        str_rep = "HEAD <-> "
        current = self.head
        while current:
            str_rep += f"{current.data} <-> "
            current = current.next
        str_rep += "TAIL"
        return str_rep

    def insert_first(self, data: Any) -> Node:
        node = Node(data)
        if self.head:
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node
        return node

    def delete_first(self) -> Optional[Node]:
        deleted_node: Node = None
        if self.head:
            deleted_node = self.head
            if self.head.next:
                # List has more than one node
                self.head = self.head.next
                self.head.prev = None
            else:
                # List has only one node
                self.head = None
                self.tail = None
        return deleted_node

    def insert_last(self, data: Any) -> None:
        node = Node(data)
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def delete_last(self) -> Optional[Node]:
        deleted_node: Node = None
        if self.tail:
            deleted_node = self.tail
            if self.tail.prev:
                # List has more than one node
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                # List has only one node
                self.head = None
                self.tail = None
        return deleted_node

    def delete_node(self, node: Node) -> None:
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

    def print(self) -> None:
        print(self)

    def is_empty(self) -> bool:
        return self.head is None

    def size(self) -> int:
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size


def test_insert_first():
    test_dll = DoublyLinkedList()
    test_dll.insert_first(1)
    assert str(test_dll) == "HEAD <-> 1 <-> TAIL"
    test_dll.insert_first(2)
    assert str(test_dll) == "HEAD <-> 2 <-> 1 <-> TAIL"
    test_dll.insert_first(3)
    assert str(test_dll) == "HEAD <-> 3 <-> 2 <-> 1 <-> TAIL"
    test_dll.insert_first(4)
    assert str(test_dll) == "HEAD <-> 4 <-> 3 <-> 2 <-> 1 <-> TAIL"
    print("test_insert_first: successful")


def test_delete_first():
    test_dll = DoublyLinkedList()
    test_dll.insert_first(1)
    test_dll.insert_first(2)
    test_dll.insert_first(3)
    test_dll.insert_first(4)
    assert str(test_dll) == "HEAD <-> 4 <-> 3 <-> 2 <-> 1 <-> TAIL"
    assert test_dll.delete_first().data == 4
    assert str(test_dll) == "HEAD <-> 3 <-> 2 <-> 1 <-> TAIL"
    assert test_dll.delete_first().data == 3
    assert str(test_dll) == "HEAD <-> 2 <-> 1 <-> TAIL"
    assert test_dll.delete_first().data == 2
    assert str(test_dll) == "HEAD <-> 1 <-> TAIL"
    assert test_dll.delete_first().data == 1
    assert str(test_dll) == "HEAD <-> TAIL"
    assert test_dll.delete_first() is None
    assert str(test_dll) == "HEAD <-> TAIL"
    print("test_delete_first: successful")


def test_insert_last():
    test_dll = DoublyLinkedList()
    test_dll.insert_last(1)
    assert str(test_dll) == "HEAD <-> 1 <-> TAIL"
    test_dll.insert_last(2)
    assert str(test_dll) == "HEAD <-> 1 <-> 2 <-> TAIL"
    test_dll.insert_last(3)
    assert str(test_dll) == "HEAD <-> 1 <-> 2 <-> 3 <-> TAIL"
    test_dll.insert_last(4)
    assert str(test_dll) == "HEAD <-> 1 <-> 2 <-> 3 <-> 4 <-> TAIL"
    print("test_insert_last: successful")


def test_delete_last():
    test_dll = DoublyLinkedList()
    test_dll.insert_first(1)
    test_dll.insert_first(2)
    test_dll.insert_first(3)
    test_dll.insert_first(4)
    assert str(test_dll) == "HEAD <-> 4 <-> 3 <-> 2 <-> 1 <-> TAIL"
    assert test_dll.delete_last().data == 1
    assert str(test_dll) == "HEAD <-> 4 <-> 3 <-> 2 <-> TAIL"
    assert test_dll.delete_last().data == 2
    assert str(test_dll) == "HEAD <-> 4 <-> 3 <-> TAIL"
    assert test_dll.delete_last().data == 3
    assert str(test_dll) == "HEAD <-> 4 <-> TAIL"
    assert test_dll.delete_last().data == 4
    assert str(test_dll) == "HEAD <-> TAIL"
    assert test_dll.delete_last() is None
    assert str(test_dll) == "HEAD <-> TAIL"
    print("test_delete_last: successful")


def test_is_empty():
    test_dll = DoublyLinkedList()
    assert test_dll.is_empty()
    test_dll.insert_first(1)
    assert not test_dll.is_empty()
    test_dll.insert_first(2)
    assert not test_dll.is_empty()
    test_dll.delete_first()
    assert not test_dll.is_empty()
    test_dll.delete_first()
    assert test_dll.is_empty()
    print("test_is_empty: successful")


def test_size():
    test_dll = DoublyLinkedList()
    assert test_dll.size() == 0
    test_dll.insert_first(1)
    assert test_dll.size() == 1
    test_dll.insert_first(2)
    assert test_dll.size() == 2
    test_dll.delete_last()
    assert test_dll.size() == 1
    test_dll.delete_last()
    assert test_dll.size() == 0
    print("test_size: successful")


def test_delete_node():
    test_dll = DoublyLinkedList()
    np1 = test_dll.insert_first(1)
    np2 = test_dll.insert_first(2)
    np3 = test_dll.insert_first(3)
    np4 = test_dll.insert_first(4)
    assert str(test_dll) == "HEAD <-> 4 <-> 3 <-> 2 <-> 1 <-> TAIL"
    test_dll.delete_node(np1)
    assert str(test_dll) == "HEAD <-> 4 <-> 3 <-> 2 <-> TAIL"
    test_dll.delete_node(np3)
    assert str(test_dll) == "HEAD <-> 4 <-> 2 <-> TAIL"
    test_dll.delete_node(np4)
    assert str(test_dll) == "HEAD <-> 2 <-> TAIL"
    test_dll.delete_node(np2)
    assert str(test_dll) == "HEAD <-> TAIL"
    print("test_delete_node: successful")


if __name__ == "__main__":
    print("Doubly Linked List")
    test_insert_first()
    test_delete_first()
    test_insert_last()
    test_delete_last()
    test_is_empty()
    test_delete_node()
