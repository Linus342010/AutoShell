import os
from commands import *
import argparse

commands = ("open_app", "press")

def execute(file):
    try:
        with open(file, "r") as f:
            for line in f:
                cmd = line.rstrip()
                name = cmd.split("(")[0]
                arg = cmd.split("(")[1][:-1]
                if name in commands:
                    globals()[name](arg)
                else:
                    print("lkjdhg")

    except Exception as e:
        print(f"Error occurred while executing {file}: {e}")
    
if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Execute commands")
    parse.add_argument("-f", "--file", help="File to execute")
    args = parse.parse_args()
    if args.file:
        execute(args.file)
    else:
        execute("run.ashell")







