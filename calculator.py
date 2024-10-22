import os
import importlib
import logging
from faker import Faker

# Set up logging configuration
logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG to capture all levels of logs
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]  # Logs to console
)

# Command Interface
class Command:
    def execute(self):
        pass

# Built-in commands (Add, Subtract, Multiply, Divide)
class AddCommand(Command):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def execute(self):
        return self.x + self.y

class SubtractCommand(Command):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def execute(self):
        return self.x - self.y

class MultiplyCommand(Command):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def execute(self):
        return self.x * self.y

class DivideCommand(Command):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def execute(self):
        if self.y == 0:
            return "Error: Division by zero"
        return self.x / self.y

# Invoker with plugin support
class CalculatorInvoker:
    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        command = self._commands.get(command_name)
        if command:
            return command.execute()
        else:
            return "Command not recognized"

    def load_plugins(self):
        # Load all plugins from the plugins directory
        plugin_dir = "plugins"
        for filename in os.listdir(plugin_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]  # Remove '.py' extension
                module = importlib.import_module(f"plugins.{module_name}")
                plugin_command_name = module.get_command_name()
                plugin_command_class = module.get_command_class()
                self.register(plugin_command_name, plugin_command_class)

# REPL function
def repl():
    invoker = CalculatorInvoker()
    faker = Faker()

    # Load available plugins
    invoker.load_plugins()

    print("Simple Calculator REPL with Command Pattern, Faker, and Plugins")
    print("Enter expressions (e.g., 'add 10 5', 'multiply 2 3', 'power 3 2'). Type 'exit' to quit.")
    print("Use 'random' to generate random numbers with Faker.")

    while True:
        user_input = input("calc> ").strip()

        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break

        if user_input.lower() == 'random':
            # Generate two random numbers using Faker
            num1 = faker.random_number(digits=2)
            num2 = faker.random_number(digits=2)
            print(f"Generated random numbers: {num1}, {num2}")
            continue

        try:
            parts = user_input.split()
            command_name = parts[0].lower()
            num1 = float(parts[1])
            num2 = float(parts[2]) if len(parts) > 2 else None

            if command_name in invoker._commands:
                # Register the command and execute
                if command_name == "sqrt" and num2 is None:
                    invoker.register(command_name, invoker._commands[command_name](num1))
                    result = invoker.execute(command_name)
                else:
                    invoker.register(command_name, invoker._commands[command_name](num1, num2))
                    result = invoker.execute(command_name)

                print(f"Result: {result}")
            else:
                print(f"Unknown command: {command_name}")
        except (ValueError, IndexError):
            print("Invalid input. Use the format: <command> <number1> <number2>. Type 'exit' to quit.")

if __name__ == "__main__":
    repl()
