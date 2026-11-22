
import argparse
import sqlite3
from datetime import datetime

from db import import_csv
from tracker import Expense, ExpenseTracker


def main():
    parser = argparse.ArgumentParser(
        description="Expense Tracker CLI"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # Import command
    import_parser = subparsers.add_parser(
        "import",
        help="Import expenses from a CSV file"
    )
    import_parser.add_argument("path")

    # Summary command
    summary_parser = subparsers.add_parser(
        "summary",
        help="Show category-wise expense totals"
    )
    summary_parser.add_argument(
        "--month",
        help="Filter expenses by month (YYYY-MM)"
    )

    # Add command
    add_parser = subparsers.add_parser(
        "add",
        help="Add a new expense"
    )
    add_parser.add_argument("--date", required=True)
    add_parser.add_argument("--category", required=True)
    add_parser.add_argument("--description", required=True)
    add_parser.add_argument("--amount", required=True, type=float)

    args = parser.parse_args()

    try:
        if args.command == "import":
            import_csv(args.path)

        elif args.command == "summary":
            if args.month:
                try:
                    datetime.strptime(args.month, "%Y-%m")
                except ValueError:
                    print("Error: Month must use YYYY-MM format.")
                    return

            tracker = ExpenseTracker()
            totals = tracker.totals_by_category(args.month)

            if not totals:
                print("No expenses found.")
                return

            print("\n===== EXPENSE SUMMARY =====")

            for category, amount in totals.items():
                print(f"{category}: ₹{amount:.2f}")

            print("---------------------------")
            print(f"Total: ₹{sum(totals.values()):.2f}")

        elif args.command == "add":
            try:
                datetime.strptime(args.date, "%Y-%m-%d")
            except ValueError:
                print("Error: Date must use YYYY-MM-DD format.")
                return

            if not args.category.strip() or not args.description.strip():
                print("Error: Category and description cannot be empty.")
                return

            if args.amount < 0:
                print("Error: Amount cannot be negative.")
                return

            expense = Expense(
                args.date,
                args.category.strip().title(),
                args.description.strip(),
                args.amount
            )

            tracker = ExpenseTracker()
            tracker.add_expense(expense)
            print("Expense added successfully!")

    except sqlite3.Error as error:
        print("Database error:", error)


if __name__ == "__main__":
    main()
