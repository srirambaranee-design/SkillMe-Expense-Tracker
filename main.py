
from report import export_category_report
from tracker import Expense, ExpenseTracker
from storage import load_expenses, save_expenses

# Create tracker
tracker = ExpenseTracker()

# Load existing expenses
expenses, skipped_rows = load_expenses("data/expenses.csv")

for expense in expenses:
    tracker.add_expense(expense)

print("Expenses loaded:", len(expenses))
print("Invalid rows skipped:", skipped_rows)


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Show all expenses")
    print("2. Add new expense")
    print("3. Search expenses")
    print("4. Export category report")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        tracker.show_expenses()

    elif choice == "2":
        date = input("Enter date: ").strip()
        category = input("Enter category: ").strip().title()
        description = input("Enter description: ").strip()

        if not date or not category or not description:
            print("Date, category and description cannot be empty.")
            continue

        try:
            amount = float(input("Enter amount: "))

            if amount < 0:
                print("Amount cannot be negative.")
                continue

        except ValueError:
            print("Please enter a valid amount.")
            continue

        new_expense = Expense(date, category, description, amount)
        tracker.add_expense(new_expense)

        save_expenses("data/expenses.csv", tracker.expenses)

        print("Expense added and saved successfully!")

    elif choice == "3":
        keyword = input("Enter description to search: ").strip()
        results = tracker.search_expenses(keyword)

        if results:
            for expense in results:
                print(expense)
        else:
            print("No matching expenses found.")

    elif choice == "4":
        totals = tracker.totals_by_category()
        export_category_report(totals, "report.json")

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Try again.")
