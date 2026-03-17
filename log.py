import colorama
from colorama import Fore, Style

colorama.init()

def success(str):
    print(f"{Fore.GREEN}[Success] {str}{Style.RESET_ALL}")

def error(str):
    print(f"{Fore.RED}[Error] {str}{Style.RESET_ALL}")

def info(str):
    print(f"{Fore.BLUE}[Info] {str}{Style.RESET_ALL}")