from tokens import Integer, Float, Operator, String


class Lexer:
    digits = "0123456789"
    alphabets_begin = "abcdefghijklmnopqrstuvwxyz"
    alphabets_begin += alphabets_begin.upper() + "_"
    alphabets_end = alphabets_begin + digits
    operators = "+-/*"

    def __init__(self, text):
        self.text = text
        self.current_index = 0
        self.tokens = []
        self.current_char = self.text[self.current_index]
        self.current_token = None

    def tokenize(self):
        while self.current_index < len(self.text):
            if self.current_char == " ":
                while self.current_char == " " and self.current_index < len(self.text):
                    self.update_token()

            # if integer or float
            if self.current_char in self.digits or self.current_char == ".":
                isFloat = False

                if self.current_char == ".":
                    isFloat = True

                # part of a number of >=1 digits
                token_start = token_end = self.current_index

                interrupt_type_int = False
                interrupt_type_float = False

                while (
                    self.current_index < len(self.text)
                    and interrupt_type_float == False
                    and interrupt_type_int == False
                ):
                    self.update_token()
                    if self.current_char not in Lexer.digits:
                        if self.current_char == ".":
                            if isFloat == False:
                                isFloat = True
                            else:
                                interrupt_type_float = True
                        elif self.current_char.isspace():
                            break
                        else:
                            interrupt_type_int = True

                # read the int or float only if interruped by operator
                if interrupt_type_int == False and interrupt_type_float == False:
                    token_end = self.current_index
                elif (
                    interrupt_type_float == False
                    and interrupt_type_int == True
                    and (self.current_char in self.operators)
                ):
                    token_end = self.current_index

                # append current token as integer or float
                if token_start != token_end:
                    if isFloat:
                        self.current_token = Float(self.text[token_start:token_end])
                    else:
                        self.current_token = Integer(self.text[token_start:token_end])

                    self.tokens.append(self.current_token)
                    if interrupt_type_float:
                        self.update_token()

            # append if operator
            elif self.current_char in Lexer.operators:
                self.current_token = Operator(self.current_char)
                self.tokens.append(self.current_token)
                self.update_token()

            # append if string
            elif self.current_char in Lexer.alphabets_begin:
                # only consider if previous character is a space or an operator
                if (
                    self.current_index != 0
                    and not self.text[self.current_index - 1].isspace()
                    and self.text[self.current_index - 1] not in self.operators
                ):
                    self.update_token()

                else:
                    interrupt_type_string = False
                    interrupt_type_op = False
                    token_start = token_end = self.current_index

                    while (
                        self.current_index < len(self.text)
                        and interrupt_type_string == False
                        and interrupt_type_op == False
                    ):
                        self.update_token()
                        if self.current_char not in self.alphabets_end:
                            if self.current_char.isspace():
                                break
                            if self.current_char in self.operators:
                                interrupt_type_op = True
                            else:
                                interrupt_type_string = True

                    if not interrupt_type_string and not interrupt_type_op:
                        token_end = self.current_index
                    elif not interrupt_type_string and interrupt_type_op:
                        token_end = self.current_index

                    if token_start != token_end:
                        self.current_token = String(self.text[token_start:token_end])
                        self.tokens.append(self.current_token)

                        if self.current_char not in self.operators:
                            self.update_token()

            else:
                self.update_token()

    def update_token(self):
        self.current_index += 1
        if self.current_index < len(self.text):
            self.current_char = self.text[self.current_index]

    def print_tokens(self):
        for i in self.tokens:
            print(i.type + "\t" + i.value)

    def return_tokens(self):
        return self.tokens
