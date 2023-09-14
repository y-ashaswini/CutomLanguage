from errors import Errors


class Parse:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_index = 0
        self.current_token = self.tokens[self.current_index]

    def update_token(self):
        try:
            self.current_index += 1
            if self.current_index < len(self.tokens):
                self.current_token = self.tokens[self.current_index]
        except Exception as e:
            Errors.append_error(
                "UPDATION ERROR",
                "Couldn't update counter",
                "update_token() function @ Parse Class",
            )

    # NON TERMINALS :       expression, term, factor
    # METHODS       :       define 3 different methods to identify them + one to evaluate them
    # EXAMPLE       :       1 + 2 * 3 = [1, +, [2, *, 3]]

    # Token not updated after factor
    def factor(self):
        if self.current_token.type == "INT" or self.current_token.type == "FLT":
            return self.current_token

    # Token is updated after term
    def term(self):
        left_node = self.factor()

        self.update_token()
        while self.current_token.value == "*" or self.current_token.value == "/":
            operator = self.current_token

            self.update_token()
            right_node = self.factor()
            left_node = [left_node, operator, right_node]
            self.update_token()

        return left_node

    # Token not updated after expression
    def expression(self):
        left_node = self.term()

        while self.current_token.value == "+" or self.current_token.value == "-":
            operator = self.current_token

            self.update_token()
            right_node = self.term()
            left_node = [left_node, operator, right_node]

        return left_node

    def parse(self):
        return self.expression()

    # Works with any combination of numbers and operators
    # FOR EXAMPLE   :   2 * 2 + 1 * 2
    # [['2', '*', '2'], '+', ['1', '*', '2']]
