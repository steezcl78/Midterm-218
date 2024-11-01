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


