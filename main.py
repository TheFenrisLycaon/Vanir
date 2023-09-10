from src import vanir
from cli import menu, tools


def main():
    tools.print_banner()

    main_menu = menu.Menu()

    settings = menu.Menu(main_menu)
    settings.add_option("Add Categories")
    settings.add_option("Add Account")
    settings.add_option("Remove Categories")
    settings.add_option("Remove Account")
    settings.add_option("Reset")

    data = menu.Menu(main_menu)
    data.add_option("Import Data")
    data.add_option("Export Data")

    expense_log = menu.Menu(main_menu)
    expense_log.add_option("Last 5 transaction")
    expense_log.add_option("Last 5 expenses")
    expense_log.add_option("Last 5 incomes")
    expense_log.add_option("Last 5 transfer")

    main_menu.add_option("Add Income")
    main_menu.add_option("Add Expense")
    main_menu.add_option("Add Transfer")
    main_menu.add_option("Settings", settings.display)
    main_menu.add_option("Data", data.display)
    main_menu.add_option("Show Expenses", expense_log.display)

    while True:
        main_menu.display()


if __name__ == "__main__":
    main()
