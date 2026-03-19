import src.interpreter
import argparse
import src.log as log


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="Run a script file")
        parser.add_argument("-s", "--script", help="Script file to run", default="run.ashell")
        args = parser.parse_args()
    except Exception as e:
        log.error(f"Error parsing arguments: {e}")
        exit(1)

    src.interpreter.praser(args.script)