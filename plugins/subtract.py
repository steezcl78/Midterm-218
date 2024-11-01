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

def get_description():
    return "Subtraction"