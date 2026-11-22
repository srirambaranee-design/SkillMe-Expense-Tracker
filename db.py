
import sqlite3
import csv


# Connect to SQLite database
def connect_db():
    connection = sqlite3.connect("expenses.db")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT NOT NULL,
            amount REAL NOT NULL
        )
    """)

    # Prevent duplicate expenses
    connection.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS unique_expense
        ON expenses (date, category, description, amount)
    """)

    connection.commit()

    return connection


# Add a new expense
def add_expense(date, category, description, amount):
    connection = connect_db()

    try:
        connection.execute("""
            INSERT OR IGNORE INTO expenses
            (date, category, description, amount)
            VALUES (?, ?, ?, ?)
        """, (date, category, description, amount))

        connection.commit()

    finally:
        connection.close()


# Retrieve all expenses
def get_all():
    connection = connect_db()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT date, category, description, amount
            FROM expenses
            ORDER BY id
        """)

        expenses = cursor.fetchall()

        return expenses

    finally:
        connection.close()



def totals_by_category(month=None):
    connection = connect_db()

    try:
        cursor = connection.cursor()

        if month:
            cursor.execute("""
                SELECT category, SUM(amount)
                FROM expenses
                WHERE date LIKE ?
                GROUP BY category
            """, (month + "%",))

        else:
            cursor.execute("""
                SELECT category, SUM(amount)
                FROM expenses
                GROUP BY category
            """)

        return cursor.fetchall()

    finally:
        connection.close()



# Import expenses from CSV
def import_csv(path):
    imported = 0
    skipped = 0

    try:
        with open(path, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            required_columns = {
                "Date", "Category", "Description", "Amount"
            }

            if not reader.fieldnames or not required_columns.issubset(reader.fieldnames):
                print("Error: CSV has incorrect columns.")
                return 0, 0

            connection = connect_db()

            try:
                for row in reader:
                    try:
                        date = row["Date"].strip()
                        category = row["Category"].strip().title()
                        description = row["Description"].strip()
                        amount = float(row["Amount"])

                        if not date or not category or not description or amount < 0:
                            raise ValueError

                        cursor = connection.execute("""
                            INSERT OR IGNORE INTO expenses
                            (date, category, description, amount)
                            VALUES (?, ?, ?, ?)
                        """, (date, category, description, amount))

                        if cursor.rowcount == 1:
                            imported += 1
                        else:
                            skipped += 1

                    except (ValueError, TypeError, AttributeError):
                        skipped += 1

                connection.commit()

            finally:
                connection.close()

    except FileNotFoundError:
        print("Error: CSV file not found.")
        return 0, 0

    except OSError as error:
        print("Error reading CSV:", error)
        return 0, 0

    print("Imported:", imported)
    print("Skipped:", skipped)

    return imported, skipped
