import abc


class Token:
    """
    Program Token is which of identifer, number or string

    """

    def __init__(self, line_number):
        self._line_number = line_number

    def __str__(self):
        return str(self.line_number)

    def line_number(self):
        return self._line_number

    # TODO() avoid redundunt java style
    @abc.abstractmethod
    def is_identifier(self):
        return False

    @abc.abstractmethod
    def is_number(self):
        return False

    @abc.abstractmethod
    def is_string(self):
        return False


EOF = Token(-1)  # end of file
EOL = '\n'  # end of line

# TODO() debug
print(EOF)
