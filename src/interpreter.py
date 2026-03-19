import re

from src.commands import *
import src.log

COMMANDS = {
    "open_app": open_app,

}

def interpret(line: str, line_number: int):
    line = line.strip()

    COMMAND_PATTERN = re.compile(r'^(\w+)\(\s*["\'](.+?)["\']\s*\)\s*$')

    if not line or line.startswith("#"):
        log.info("Skip empty line or comment")
        return
    
    command = COMMAND_PATTERN.match(line)
    if not command:
        log.error(f"Syntax error on line {line_number}: {line}")
        return

    name = command.group(1)
    arg = command.group(2)

    if name not in COMMANDS:
        log.error(f"Unknown command on line {line_number}: {name}")
        return
    
    COMMANDS[name](arg)


def praser(file: str):
    try:
        with open(file, "r") as f:
            for line_number, line in enumerate(f, start=1):
                interpret(line, line_number)
    except Exception as e:
        log.error(f"Error occurred while parsing {file}: {e}")


