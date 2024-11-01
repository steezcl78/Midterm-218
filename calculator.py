import os
import importlib
import logging
from faker import Faker

# Set up logging configuration to both console and file
logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG to capture all levels of logs
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Logs to console
        logging.FileHandler("calculator.log")  # Logs to a file named calculator.log
    ]
)


# Invoker with plugin support
class CalculatorInvoker:
    def __init__(self):
        self._commands = {}
        self._history = []  # Store the history of executed commands

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name, *args):
        command = self._commands.get(command_name)
        if command:
            result = command(*args).execute()
            # Store the command execution in history
            self._history.append({
                'command': command_name,
                'args': args,
                'result': result
            })
            return result
        else:
            return "Command not recognized"

    def load_plugins(self):
        # Load all plugins from the plugins directory
        plugin_dir = "plugins"
        for filename in os.listdir(plugin_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]  # Remove '.py' extension
                try:
                    module = importlib.import_module(f"plugins.{module_name}")
                    plugin_command_name = module.get_command_name()
                    plugin_command_class = module.get_command_class()
                    # Registering the command without instantiation for dynamic use in the REPL
                    self.register(plugin_command_name, plugin_command_class)
                except AttributeError as e:
                    logging.error(f"Error loading plugin '{module_name}': {e}")

    def get_history(self):
        # Returns the command history as a list of strings
        return [
            f"{entry['command']} {entry['args']} = {entry['result']}"
            for entry in self._history
        ]


# REPL function
def repl():
    invoker = CalculatorInvoker()
    faker = Faker()

    # Load available plugins
    invoker.load_plugins()

    print("Simple Calculator REPL with Command Pattern, Faker, Plugins, and History")
    print("Enter expressions (e.g., 'add 10 5', 'multiply 2 3', 'power 3 2'). Type 'exit' to quit.")
    print("Use 'random' to generate random numbers with Faker.")
    print("Use 'history' to view the command history.")

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

        if user_input.lower() == 'history':
            # Display command history
            history = invoker.get_history()
            if history:
                print("Command History:")
                for entry in history:
                    print(entry)
            else:
                print("No history available.")
            continue

        try:
            parts = user_input.split()
            command_name = parts[0].lower()
            num1 = float(parts[1])
            num2 = float(parts[2]) if len(parts) > 2 else None

            if command_name in invoker._commands:
                # Execute without re-registering
                if num2 is None:
                    result = invoker.execute(command_name, num1)
                else:
                    result = invoker.execute(command_name, num1, num2)

                print(f"Result: {result}")
            else:
                print(f"Unknown command: {command_name}")
        except (ValueError, IndexError):
            print("Invalid input. Use the format: <command> <number1> <number2>. Type 'exit' to quit.")

if __name__ == "__main__":
    repl()


