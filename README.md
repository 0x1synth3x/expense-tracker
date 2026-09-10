# Expense Tracker CLI

A simple command-line application to manage personal expenses — add, update, delete, list, and summarize your spending. Built as part of the [roadmap.sh backend projects](https://roadmap.sh/projects/expense-tracker).

## Features

- Add an expense with a description and amount
- Delete an expense by ID
- View all expenses in a table
- View a summary of total expenses
- View a summary of expenses for a specific month (current year)

## Requirements

- Python 3.7+
- No external dependencies (uses only the standard library: `argparse`, `json`, `datetime`, `pathlib`)

## Installation

```bash
git clone https://github.com/<your-username>/expense-tracker.git
cd expense-tracker
```

No pip install needed — the script only uses Python's standard library.

## Usage

Run the script with `python expense_tracker.py <command> [options]`.

### Add an expense

```bash
python expense_tracker.py add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)
```

### List all expenses

```bash
python expense_tracker.py list
# ID   Date        Description  Amount
# 1    2024-08-06  Lunch        $20
```

### View summary of all expenses

```bash
python expense_tracker.py summary
# Total expense: $20
```

### View summary for a specific month

```bash
python expense_tracker.py summary --month 8
# Total expense for August: $20
```

### Delete an expense

```bash
python expense_tracker.py delete --id 1
# Expense deleted successfully
```

## Data storage

Expenses are stored locally in `expense_record.json` in the same directory as the script. The file is created automatically the first time you add an expense.

## Project structure

```
expense-tracker/
├── expense_tracker.py
├── expense_record.json   # generated automatically
└── README.md
```
## Acknowledgements

Built for the [Expense Tracker](https://roadmap.sh/projects/expense-tracker) project on [roadmap.sh](https://roadmap.sh).
