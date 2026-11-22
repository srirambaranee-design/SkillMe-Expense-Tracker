# Python Expense Tracker

A Python-based Expense Tracker developed as part of the **SkillMe Python Engineering Internship**.

## Project Description

This application helps users manage, store, analyse, and track expenses using Python, CSV files, SQLite databases, classes, and separate modules.

## Features

### Week 1 – CSV Basics
- Load expense records from a CSV file.
- Display all expense records.
- Calculate total spending.
- Calculate category-wise spending.
- Identify the biggest expense.

### Week 2 – Classes, Modules and Clean Data
- Implement `Expense` and `ExpenseTracker` classes.
- Add new expenses.
- Search expenses by description (case-insensitive).
- Detect invalid records and count skipped rows.
- Export category totals to a JSON report.
- Organise code into separate Python modules.

### Week 3 – SQLite and Error Handling
- Store expenses in an SQLite database.
- Automatically create the database table if it does not exist.
- Import expense records from CSV files.
- Prevent duplicate expense imports.
- Calculate category-wise totals using SQL `GROUP BY`.
- Filter expense summaries by month.
- Add expenses through command-line arguments.
- Use `argparse` to provide `import`, `summary`, and `add` commands.
- Handle missing files, incorrect CSV columns, and invalid amounts.
- Use parameterized SQL queries to protect database operations.

## Project Structure

```text
SkillMe_Internship/
├── main.py
├── tracker.py
├── storage.py
├── db.py
├── expenses.db
├── report.py
├── report.json
├── README.md
└── data/
    └── expenses.csv
```

## Requirements

- Python 3
- SQLite3 (included with Python)
- No external libraries required

## How to Run

Open the project folder in your terminal.

### Display available commands

```bash
py main.py --help
```

### Import expenses from CSV

```bash
py main.py import data/expenses.csv
```

### Display all category summaries

```bash
py main.py summary
```

### Display monthly summary

```bash
py main.py summary --month 2026-11
```

### Add a new expense

```bash
py main.py add --date 2026-11-22 --category Food --description "Breakfast" --amount 150
```

## CSV Format

Expense records are imported from CSV files using these columns:

- Date
- Category
- Description
- Amount

Example:

```csv
Date,Category,Description,Amount
2026-11-22,Food,Breakfast,150
2026-11-23,Travel,Bus fare,100
```

## Technologies Used

- Python
- SQLite
- SQL
- CSV
- JSON
- Object-Oriented Programming
- Argparse
- Git
- GitHub

## Internship

**Program:** SkillMe Python Engineering Internship

**Week 1:** Read a CSV and Summarise It

**Week 2:** Classes, Modules and Clean Data

**Week 3:** Save to SQLite and Handle Errors
