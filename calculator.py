import os
import importlib
import logging
from faker import Faker

# Set up environment variables with defaults
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG").upper()  # Default to DEBUG level
LOG_FILE = os.getenv("LOG_FILE", "calculator.log")  # Default log file name
PLUGIN_DIR = os.getenv("PLUGIN_DIR", "plugins")  # Default plugin directory

# Set up logging configuration to both console and file
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.DEBUG),  # Use LOG_LEVEL environment variable
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Logs to console
        logging.FileHandler(LOG_FILE)  # Logs to a file from LOG_FILE environment variable
    ]
)

# Invoker with plugin support
class CalculatorInvoker:
    def __init__(self):
        self._commands = {}
        self._history = []  # Store the history of executed commands

    def register(self, command_name, command, description="No description available"):
        self._commands[command_name] = {"class": command, "description": description}
        logging.info(f"Registered command '{command_name}'")

    def execute(self, command_name, *args):
        command_info = self._commands.get(command_name)
        if command_info:
            result = command_info["class"](*args).execute()
            # Store the command execution in history
            self._history.append({
                'command': command_name,
                'args': args,
                'result': result
            })
            logging.info(f"Executed command '{command_name}' with args {args}, result: {result}")
            return result
        else:
            logging.warning(f"Command '{command_name}' not recognized")
            return "Command not recognized"

    def load_plugins(self):
        # Load all plugins from the plugins directory specified by PLUGIN_DIR
        for filename in os.listdir(PLUGIN_DIR):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]  # Remove '.py' extension
                try:
                    module = importlib.import_module(f"{PLUGIN_DIR}.{module_name}")
                    plugin_command_name = module.get_command_name()
                    plugin_command_class = module.get_command_class()
                    plugin_description = module.get_description()
                    # Registering the command with description for REPL menu display
                    self.register(plugin_command_name, plugin_command_class, plugin_description)
                except AttributeError as e:
                    logging.error(f"Error loading plugin '{module_name}': {e}")

    def get_history(self):
        # Returns the command history as a list of strings
        logging.info("Accessed command history")
        return [
            f"{entry['command']} {entry['args']} = {entry['result']}"
            for entry in self._history
        ]

    def get_menu(self):
        # Returns a list of available commands and descriptions
        return [
            f"{command_name}: {command_info['description']}"
            for command_name, command_info in self._commands.items()
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
    print("Use 'menu' to view available commands.")

    while True:
        user_input = input("calc> ").strip()

        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            logging.info("User exited the REPL")
            break

        if user_input.lower() == 'random':
            # Generate two random numbers using Faker
            num1 = faker.random_number(digits=2)
            num2 = faker.random_number(digits=2)
            print(f"Generated random numbers: {num1}, {num2}")
            logging.info(f"Generated random numbers: {num1}, {num2}")
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

        if user_input.lower() == 'menu':
            # Display the available commands and descriptions
            menu = invoker.get_menu()
            if menu:
                print("Available Commands:")
                for entry in menu:
                    print(entry)
            else:
                print("No commands available.")
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
            logging.error("Invalid input provided by the user")
            print("Invalid input. Use the format: <command> <number1> <number2>. Type 'exit' to quit.")

if __name__ == "__main__":
    repl()


