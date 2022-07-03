import random


class Node:
    """
    Node if a singly linked list
    """
    def __init__(self, data):
        self.data = data
        self.next = None


def has_loop(head: Node) -> bool:
    """
    Detects if the given singly linked list has a loop/cycle in it or not
    A linked list has a loop/cycle if same node is visited again while traversing the list
    Many algorithms which assumes that last_node.next would be Null, may break in this scenarios
    :param head:
    :return: True if it has a loop or False otherwise
    """
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def test_has_loop_with_loop_in_the_middle():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(3)
    a.next = b
    b.next = c
    c.next = d
    d.next = b
    assert has_loop(a)


def test_has_loop_with_loop_in_the_beginning():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(3)
    a.next = b
    b.next = c
    c.next = d
    d.next = a
    assert has_loop(a)


def test_has_loop_with_loop_self_reference():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(3)
    a.next = b
    b.next = c
    c.next = d
    d.next = d
    assert has_loop(a)


def test_has_loop_with_loop_self_reference_first_node():
    a = Node(1)
    a.next = a
    assert has_loop(a)


def test_has_loop_with_no_loop():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(3)
    a.next = b
    b.next = c
    c.next = d
    assert not has_loop(a)


def test_has_loop_with_no_loop_single_node():
    a = Node(1)
    assert not has_loop(a)


def test_has_loop_with_no_loop_empty_list():
    assert not has_loop(None)


def test_has_loop_with_loop_very_big_list():
    """
    Created 10000 nodes and randomly introduces a cycle in the list and tests
    :return:
    """
    node = Node(1)
    max_nodes = 10000
    random_cycle_index = int(random.random() * (max_nodes - 3)) + 2
    cycle_node = None
    for i in range(2, max_nodes):
        node.next = Node(i)
        if i == random_cycle_index:
            cycle_node = node
    node.next = cycle_node
    assert has_loop(node)


if __name__ == "__main__":
    print("Loop/Cycle Detection using two pointers")
