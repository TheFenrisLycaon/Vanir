from typing import Callable
import os

BANNER = "config/banner.txt"


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def print_banner():
    clear()
    with open(BANNER, "r") as f:
        print(f.read())
