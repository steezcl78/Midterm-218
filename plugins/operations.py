class AddCommand:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def execute(self):
        return self.x + self.y

def get_command_name():
    return "add"

def get_command_class():
    return AddCommand


class SubtractCommand:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def execute(self):
        return self.x - self.y

def get_command_name():
    return "subtract"

def get_command_class():
    return SubtractCommand


class MultiplyCommand:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def execute(self):
        return self.x * self.y

def get_command_name():
    return "multiply"

def get_command_class():
    return MultiplyCommand


class DivideCommand:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def execute(self):
        if self.y == 0:
            return "Error: Division by zero"
        return self.x / self.y

def get_command_name():
    return "divide"

def get_command_class():
    return DivideCommand