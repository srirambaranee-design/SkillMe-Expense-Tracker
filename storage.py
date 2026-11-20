import csv
from tracker import Expense


def load_expenses(path):
    expenses = []
    skipped_rows = 0

    with open(path, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                date = row["Date"].strip()
                category = row["Category"].strip()
                description = row["Description"].strip()
                amount = float(row["Amount"])

                if not date or not category or not description or amount < 0:
                    raise ValueError

                expense = Expense(date, category, description, amount)
                expenses.append(expense)

            except (ValueError, KeyError, TypeError):
                skipped_rows += 1

    return expenses, skipped_rows
def save_expenses(path, expenses):
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Date", "Category", "Description", "Amount"])

        for expense in expenses:
            writer.writerow([
                expense.date,
                expense.category,
                expense.description,
                expense.amount
            ])