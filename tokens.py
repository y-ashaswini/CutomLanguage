class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value


# Integer, String and all other types inherit from Token Class


class Integer(Token):
    def __init__(self, value):
        super().__init__("INT", value)


class Float(Token):
    def __init__(self, value):
        super().__init__("FLT", value)


class Operator(Token):
    def __init__(self, value):
        super().__init__("OP", value)


class String(Token):
    def __init__(self, value):
        super().__init__("STR", value)
