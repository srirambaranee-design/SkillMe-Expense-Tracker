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
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def show_expenses(self):
        for expense in self.expenses:
            print(expense)

    def total_spent(self):
        return sum(expense.amount for expense in self.expenses)

    def totals_by_category(self):
        totals = {}

        for expense in self.expenses:
            category = expense.category
            totals[category] = totals.get(category, 0) + expense.amount

        return totals

    def biggest_expense(self):
        if not self.expenses:
            return None

        return max(self.expenses, key=lambda expense: expense.amount)

    def search_expenses(self, keyword):
        results = []

        for expense in self.expenses:
            if keyword.lower() in expense.description.lower():
                results.append(expense)

        return results