from cli.tools import print_banner
from time import sleep
from typing import Callable


def default():
    print_banner()
    print("This is working fine!!")
    sleep(2)


class Menu:
    def __init__(self, parent=""):
        self._options: dict = {}
        self._actions: dict = {}
        self._parent: Menu = parent if parent else self

    def add_option(
        self, option_name: str = "", action: Callable = default, option_key: str = ""
    ):
        if not option_key:
            option_key = str(len(self._options) + 1)
        self._options[option_key] = option_name
        self._actions[option_name] = action

    def _add_default_options(self):
        self.last_option = "9" * len(str(len(self._options)))
        self.add_option("Go Back", self._parent.display, self.last_option)
        self.add_option("Exit", exit, "0")

    def display(self):
        # TODO : Add split between options to display two in a row
        print_banner()
        self._add_default_options()

        for key, option in self._options.items():
            print(f"\t[{key}]:{option}")

        print()

        choice = input(f"\nEnter your option [1-{len(self._options)}] :: \t")

        self._actions[self._options[choice]]()
