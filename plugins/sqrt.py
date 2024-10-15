import math

class SqrtCommand:
    def __init__(self, x, y=None):  # y is ignored, only x is needed for square root
        self.x = x

    def execute(self):
        return math.sqrt(self.x)

def get_command_name():
    return "sqrt"

def get_command_class():
    return SqrtCommand
