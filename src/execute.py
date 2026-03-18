import os
from src.commands import *
import argparse
import src.log as log

# Allowed commands
commands = ("open_app", "press", "mouse_click")

def execute(file):
    try:
        with open(file, "r") as f:
            for line in f:
                cmd = line.rstrip()
                name = cmd.split("(")[0]
                arg_str = cmd.split("(")[1][:-1]
                # Parse arguments: split by comma, strip spaces and quotes
                args = [s.strip().strip('"') for s in arg_str.split(",") if s.strip().strip('"')]
                if name in commands:
                    log.info(f"Executing command: {name} with arguments: {args}")
                    if len(args) == 0:
                        globals()[name]()
                        log.success("executed command without arguments")
                    else:
                        globals()[name](*args)
                        log.success("executed command with arguments")
                else:
                    log.error(f"Unknown command: {name}")

    except Exception as e:
        log.error(f"Error occurred while executing {file}: {e}")

if __name__ == "__main__":
    #parse = argparse.ArgumentParser(description="Execute commands")
    #parse.add_argument("-f", "--file", help="File to execute")
    #args = parse.parse_args()
    #if args.file:
        #execute(args.file)
    #else:
    execute("run.ashell") # eingerückt




