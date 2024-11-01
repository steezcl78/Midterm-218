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

def get_description():
    return "Division"