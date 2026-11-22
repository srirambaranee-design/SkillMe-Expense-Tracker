
from db import add_expense, get_all, totals_by_category


class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self):
        return (
            f"{self.date} | {self.category} | "
            f"{self.description} | ₹{self.amount:.2f}"
        )


class ExpenseTracker:

    def add_expense(self, expense):
        add_expense(
            expense.date,
            expense.category,
            expense.description,
            expense.amount
        )

    def show_expenses(self):
        expenses = get_all()

        for expense in expenses:
            print(
                f"{expense[0]} | {expense[1]} | "
                f"{expense[2]} | ₹{expense[3]:.2f}"
            )

    def total_spent(self):
        expenses = get_all()

        return sum(expense[3] for expense in expenses)

    def totals_by_category(self, month=None):
        return dict(totals_by_category(month))

    def biggest_expense(self):
        expenses = get_all()

        if not expenses:
            return None

        biggest = max(expenses, key=lambda expense: expense[3])

        return Expense(*biggest)

    def search_expenses(self, keyword):
        expenses = get_all()
        results = []

        for expense in expenses:
            if keyword.lower() in expense[2].lower():
                results.append(Expense(*expense))

        return results
