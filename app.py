import sys

from commands.power import run as power
from commands.multiply import run as multiply
from commands.fibo import run as fibo

def run():
    commands = {
        "power": power,
        "multiply": multiply,
        "fibo": fibo
    }

    command = sys.argv[1] if len(sys.argv) > 1 else None

    if command not in commands:
        print("Unknown command.")
        exit()

    commands[command]()

# prevent potential files importing app to run it automatically
if __name__ == "__main__" :
    run()