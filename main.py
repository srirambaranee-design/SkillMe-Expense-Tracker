
import csv

def load_expenses(path):
    expenses = []

    with open(path, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)


        for row in reader:

            row["Amount"] = float(row["Amount"])
            expenses.append(row)

    return expenses
def totals_by_category(expenses):
    totals = {}

    for expense in expenses:
        category = expense["Category"]
        amount = expense["Amount"]

        if category in totals:
            totals[category] = totals[category] + amount
        else:
            totals[category] = amount

    return totals

def total_spent(expenses):
    total = 0

    for expense in expenses:
        total = total + expense["Amount"]

    return total
def biggest_expense(expenses):
    biggest = expenses[0]

    for expense in expenses:
        if expense["Amount"] > biggest["Amount"]:
            biggest = expense

    return biggest


data = load_expenses("data/expenses.csv")



while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Show all expenses")
    print("2. Totals by category")
    print("3. Biggest expense")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n{:<15} {:<18} {:>10}".format(
            "DATE", "CATEGORY", "AMOUNT"
        ))
        print("-" * 45)

        for expense in data:
            print("{:<15} {:<18} {:>10.2f}".format(
                expense["Date"],
                expense["Category"],
                expense["Amount"]
            ))

    elif choice == "2":
        print("\n===== SPENDING BY CATEGORY =====")
        print("{:<20} {:>12}".format("CATEGORY", "TOTAL"))
        print("-" * 33)

        category_totals = totals_by_category(data)

        for category, amount in category_totals.items():
            print("{:<20} {:>12.2f}".format(category, amount))

        print("-" * 33)

    elif choice == "3":
        print("\n===== BIGGEST EXPENSE =====")
        print("{:<15} {:<18} {:>10}".format(
            "DATE", "CATEGORY", "AMOUNT"
        ))
        print("-" * 45)

        biggest = biggest_expense(data)

        print("{:<15} {:<18} {:>10.2f}".format(
            biggest["Date"],
            biggest["Category"],
            biggest["Amount"]
        ))

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Try again.")
