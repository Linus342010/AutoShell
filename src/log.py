import colorama
from colorama import Fore, Style

colorama.init()

def success(msg):
    print(f"{Fore.GREEN}[Success]{Style.RESET_ALL} {msg}")

def error(msg):
    print(f"{Fore.RED}[Error]{Style.RESET_ALL} {msg}")

def info(msg):
    print(f"{Fore.BLUE}[Info]{Style.RESET_ALL} {msg}")

