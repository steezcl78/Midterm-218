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

def get_description():
    return "Multiplication"