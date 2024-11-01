Midterm 218
Christian Lee

I used command design pattern in add, subtract, multiply, divide, power and sqroot .py plugin files in plugins folder.

Example:

```class AddCommand:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def execute(self):
        return self.x + self.y

    def get_command_name():
        return "add"

    def get_command_class():
        return AddCommand"```

    
    
I used enviroment variables to set defaults. The code is in calculator.py.

Example:

"LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG").upper()  # Default to DEBUG level
LOG_FILE = os.getenv("LOG_FILE", "calculator.log")  # Default log file name
PLUGIN_DIR = os.getenv("PLUGIN_DIR", "plugins")  # Default plugin directory"



I am returning log to both console and log file.

Example:

"logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG to capture all levels of logs
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Logs to console
        logging.FileHandler("calculator.log")  # Logs to a file named calculator.log
    ]
)"


I am using try/catch/exceptions to try and catch when the user inputs the proper or incorrect input format. This illustrates LBYL and EAFP

Example:

"try:
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
            print("Invalid input. Use the format: <command> <number1> <number2>. Type 'exit' to quit.")"



Link to demo video: https://drive.google.com/file/d/1Tyv_uyF23FrjXtvqUiCzxQMS8Ipxh137/view?usp=sharing

