from typing import Any, List


class Stack:
    def __init__(self):
        self.list: List = list()

    def push(self, data: Any) -> None:
        self.list.append(data)

    def pop(self) -> Any:
        return self.list.pop()

    def peek(self) -> Any:
        return self.list[-1]

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
    if root_node is None:
        return
    current = root_node
    inorder(current.left_child)
    print(current.value, end=" ")
    inorder(current.right_child)


def inorder_non_recursive(root_node: Node) -> None:
    """
    In Order traversal of a binary tree using a stack
    :param root_node:
    :return:
    """
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


if __name__ == '__main__':
    # Create a node with some data
    root: Node = Node(1)
    root.left_child = Node(2)
    root.right_child = Node(3)
    root.left_child.left_child = Node(4)
    root.left_child.right_child = Node(5)
    # inorder(root)
    inorder_non_recursive(root)
    # print('PyCharm')
