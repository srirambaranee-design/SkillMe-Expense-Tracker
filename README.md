# Python Expense Tracker

A Python-based Expense Tracker developed as part of the **SkillMe Python Engineering Internship**.

## Project Description

This application helps users manage and analyse expenses using Python, CSV files, classes, and separate modules.

## Features

- Display all expense records
- Add new expenses and save them to CSV
- Load expense records from a CSV file
- Detect invalid records and count skipped rows
- Search expenses by description (case-insensitive)
- Calculate spending totals by category
- Export category totals to a JSON report
- Handle invalid menu choices and invalid amount inputs

## Project Structure

```text
SkillMe_Internship/
├── main.py
├── tracker.py
├── storage.py
├── report.py
├── report.json
├── README.md
└── data/
    ├── expenses.csv
    ├── test_expenses.csv
    └── test_invalid.csv
```

## Requirements

- Python 3
- No external libraries required

## How to Run

1. Clone or download this repository.
2. Open the project folder in your terminal.
3. Run:

```bash
py main.py
```

## CSV Format

Expense records are stored in `data/expenses.csv` using these columns:

- Date
- Category
- Description
- Amount

## Technologies Used

- Python
- CSV
- JSON
- Object-Oriented Programming
- Git
- GitHub

## Internship

**Program:** SkillMe Python Engineering Internship

**Week 1:** Read a CSV and Summarise It

**Week 2:** Classes, Modules and Clean Data