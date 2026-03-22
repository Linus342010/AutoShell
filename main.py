from src.interpreter import interpret
import argparse
import src.log as log




def run_script(file_path):
    try:
        with open(file_path, "r") as f:
            for line_number, line in enumerate(f, start=1):
                interpret(line, line_number)
    except Exception as e:
        print(f"Fehler beim Ausführen: {e}")

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="Run a script file")
        parser.add_argument("-s", "--script", help="Script file to run", default="run.ashell")
        args = parser.parse_args()
    except Exception as e:
        log.error(f"Error parsing arguments: {e}")
        exit(1)
    run_script(args.script)