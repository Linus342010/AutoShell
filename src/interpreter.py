import re
from src.commands import *
import src.log as log

COMMANDS = {
    "open_app": open_app,
    "press": press,
    "close_app": close_app,
    "open_url": open_url,
    "open_file": open_file,
    "open_file": open_file,
    "show_in_explorer": show_in_explorer,
    "print": print_text,
}

COMMAND_PATTERN = re.compile(r'^(\w+)\((.*)\)$')


def parse_args(arg_string):
    if not arg_string.strip():
        return []

    args = []
    parts = re.split(r',\s*', arg_string)

    for part in parts:
        part = part.strip()

        # String
        if (part.startswith('"') and part.endswith('"')) or (part.startswith("'") and part.endswith("'")):
            args.append(part[1:-1])

        # Zahl
        elif part.isdigit():
            args.append(int(part))

        else:
            args.append(part)

    return args


def interpret(line: str, line_number: int):
    line = line.strip()

    if not line or line.startswith("#"):
        return



    match = COMMAND_PATTERN.match(line)

    if not match:
        log.error(f"Syntax error on line {line_number}: {line}")
        return

    name = match.group(1)
    arg_string = match.group(2)

    if name not in COMMANDS:
        log.error(f"Unknown command on line {line_number}: {name}")
        return

    args = parse_args(arg_string)

    try:
        COMMANDS[name](*args)
    except Exception as e:
        log.error(f"Error on line {line_number}: {e}")