class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def printstack(self):
        print(self.stack)


def perform_stack_operations():
    stack = Stack()
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)
    stack.printstack()
    stack.pop()
    stack.printstack()
    print("top of stack:", stack.peek())
    stack.pop()
    stack.printstack()
    print("top of stack:", stack.peek())
    stack.pop()
    stack.printstack()
    print("top of stack:", stack.peek())


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = Node(root)

    def preorder(self, start, records=[]):
        if start is not None:
            records.append(start.value)
            records = self.preorder(start.left, records)
            records = self.preorder(start.right, records)

        return records

    def inorder(self, start, records=[]):
        if start is not None:
            records = self.inorder(start.left, records)
            records.append(start.value)
            records = self.inorder(start.right, records)

        return records


def perform_tree_operations():
    tree = Tree(4)
    tree.root.left = Node(2)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(3)
    tree.root.right = Node(5)
    print("preorder: ", tree.preorder(tree.root))
    print("inorder: ", tree.inorder(tree.root))


# perform_stack_operations()
# perform_tree_operations()
