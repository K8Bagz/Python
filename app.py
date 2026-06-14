import sys

from commands.power import run as power
#from commands.multiply import run as multiply
#from commands.reverse import run as reverse

commands = {
    "power": power,
#    "multiply": multiply,
#    "reverse": reverse
}

command = sys.argv[1] if len(sys.argv) > 1 else None

if command not in commands:
    print("Unknown command.")
    exit()

commands[command]()