from abc import ABC
from dataclasses import dataclass
from datetime import datetime


class Category(ABC):
    ...


@dataclass
class Expense:
    amount: float
    title: str = ""
    description: str = ""
    category: Category = Category


class ExpenseTracker:
    def __init__(self):
        self.expense_report = {}

    def log_expense(self, expense: Expense):
        self.expense_report[datetime.now()] = {}

    def get_report(self):
        print(self.expense_report)
