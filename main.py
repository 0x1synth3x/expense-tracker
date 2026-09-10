import argparse
import json
import datetime
from pathlib import Path

expense_record = "expense_record.json"
expense = {"Expense": []}

if Path(expense_record).exists():
    with open(expense_record, "r") as f:
        content = f.read()

        if(content):
            expense = json.loads(content)

class Features:

    def save():
        with open(expense_record, "w") as f:
            json.dump(expense, f, indent=4)

    def add_expense():
        pass

    def list_expense():
        pass

    def summary():
        pass

    def delete():
        pass
    
parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest="command")

add_parser = subparser.add_parser("add")
add_parser.add_argument("--description")
add_parser.add_argument("--amount", type=float)

list_parser = subparser.add_parser("list")

summary_parser = subparser.add_parser("summary")

delete_parser = subparser.add_parser("delete")
delete_parser.add_argument("--id", type=int)

args = parser.parse_args()

# commands = {
#     "add": add_parser,
#     "list": list_parser,
#     "summary": summary_parser,
#     "delete": delete_parser
#     }

if args.command == "add":
    print("add is working")

elif args.command == "list":
    print("list is working")

elif args.command == "summary":
    print("summary is working")

elif args.command == "delete":
    print("delete is working")