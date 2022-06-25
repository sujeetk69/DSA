from typing import Any, List


class Stack:
    """
    Basic implementation of a Stack data structure with minimal methods as required for Tree algorithms
    Underlying data structure is a python list
    """
    def __init__(self):
        """
        Constructor: creates an instance of this class
        """
        self.list: List = list()

    def push(self, data: Any) -> None:
        """
        Pushes the object unto the stack
        :param data:
        :return:
        """
        self.list.append(data)

    def pop(self) -> Any:
        """
        Removes and return the object from top of the list
        Warning: when the stack is empty it will raise IndexError
        I did not handle it intentionally
        :return:
        """
        return self.list.pop()

    def peek(self) -> Any:
        """
        Returns the current object on the top of the stack but does not removes it
        :return:
        """
        return self.list[-1]

    def is_empty(self) -> bool:
        return len(self.list) == 0


class Queue:
    """
    Basic implementation of a Queue data structure with minimal methods as required for Tree algorithms
    """
    def __init__(self):
        """
        Constructor: create an instance of Queue
        """
        self.list = list()

    def enqueue(self, data: Any) -> None:
        """
        Insert an object at the tail of the queue
        :param data:
        :return:
        """
        self.list.insert(0, data)

    def dequeue(self) -> Any:
        """
        Removes and returns the object on the front of the queue
        :return:
        """
        return self.list.pop()

    def is_empty(self) -> bool:
        return len(self.list) == 0


class Node:
    """
    Implementation of a Binary Tree Node
    """
    def __init__(self, data: Any):
        self.value: Any = data
        self.left_child: Node = None
        self.right_child: Node = None


def inorder(root_node: Node) -> None:
    """
    In Order traversal of a binary tree given it's root_node node
    1. Traverse left subtree
    2. Visit the node
    3. Traverse right subtree
    :param root_node: Root Node
    :return:
    """
    print(f"Inorder traversal of a binary tree")
    if root_node is None:
        return
    current = root_node
    inorder(current.left_child)
    print(current.value, end=" ")
    inorder(current.right_child)
    print()


def inorder_non_recursive(root_node: Node) -> None:
    """
    In Order traversal of a binary tree using a stack
    :param root_node:
    :return:
    """
    print(f"Inorder traversal of a binary tree")
    if root_node is None:
        return
    stack = Stack()
    current = root_node
    while True:
        if current:
            stack.push(current)
            current = current.left_child
        elif not stack.is_empty():
            current = stack.pop()
            print(current.value, end=" ")
            current = current.right_child
        else:
            break
    print()


def bfs(root_node: Node) -> None:
    """
    Breadth first search - also level order traversal
    :param root_node:
    :return:
    """
    print(f"Breadth First Search")
    queue = Queue()
    queue.enqueue(root_node)
    while not queue.is_empty():
        current = queue.dequeue()
        if current:
            print(current.value, end=" ")
            queue.enqueue(current.left_child)
            queue.enqueue(current.right_child)
    print()


def dfs(root_node: Node) -> None:
    """
    Depth first search
    :param root_node:
    :return:
    """
    print(f"Depth First Search")
    stack = Stack()
    stack.push(root_node)
    while not stack.is_empty():
        current = stack.pop()
        if current:
            print(current.value, end=" ")
            stack.push(current.right_child)
            stack.push(current.left_child)
    print()


if __name__ == '__main__':
    # Create a node with some data
    root: Node = Node(1)
    root.left_child = Node(2)
    root.right_child = Node(3)
    root.left_child.left_child = Node(4)
    root.left_child.right_child = Node(5)
    # inorder(root)
    inorder_non_recursive(root)
    bfs(root)
    dfs(root)
    # print('PyCharm')
