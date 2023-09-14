from tokens import Integer, Float, Operator, String


class Interpreter:
    def __init__(self, tree):
        self.tree = tree

    def convert_INT(self, value):
        return int(value)

    def convert_FLT(self, value):
        return float(value)

    def compute_binary(self, left, op, right):
        left_type = left.type
        right_type = right.type

        left = getattr(self, f"convert_{left_type}")(left.value)
        right = getattr(self, f"convert_{right_type}")(right.value)

        output = 0

        match op.value:
            case "+":
                output = left + right
            case "-":
                output = left - right
            case "*":
                output = left * right
            case "/":
                output = left / right
            case _:
                output = output

        return (
            Float(output)
            if isinstance(left, float) or isinstance(right, float)
            else Integer(output)
        )

    def interpret(self, tree=None):
        # POST ORDER TRAVERSAL
        # LEFT, RIGHT, DATA

        if tree is None:
            tree = self.tree
        # Passing tree as none by default

        if not isinstance(tree, list):
            # just a single factor
            return tree

        # Recursively evaluating left subtree
        left_node = tree[0]
        if isinstance(left_node, list):
            left_node = self.interpret(left_node)

        # Recursively evaluating right subtree
        right_node = tree[2]
        if isinstance(right_node, list):
            right_node = self.interpret(right_node)

        operator = tree[1]  # Root node, operator

        return self.compute_binary(left_node, operator, right_node)
