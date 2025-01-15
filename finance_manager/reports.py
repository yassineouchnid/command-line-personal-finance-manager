from .transactions import view_transactions
from .budgets import get_budgets
from tabulate import tabulate
from collections import defaultdict

def generate_summary(start_date=None, end_date=None):
    transactions = view_transactions(start_date, end_date)
    summary = defaultdict(float)
    for txn in transactions:
        if txn[2] == 'Expense':
            summary[txn[3]] += txn[4]
        elif txn[2] == 'Income':
            summary[txn[3]] -= txn[4]
    table = []
    for category, total in summary.items():
        table.append([category, f"${total:.2f}"])
    print(tabulate(table, headers=['Category', 'Net Amount'], tablefmt='pretty'))

def generate_ascii_chart(start_date=None, end_date=None):
    transactions = view_transactions(start_date, end_date)
    summary = defaultdict(float)
    for txn in transactions:
        if txn[2] == 'Expense':
            summary[txn[3]] += txn[4]
        elif txn[2] == 'Income':
            summary[txn[3]] -= txn[4]
    
    for category, total in summary.items():
        bar = '*' * int(abs(total) / 10)  # Adjust scaling as needed
        sign = '-' if total < 0 else '+'
        print(f"{category:15} {sign} {bar} (${total:.2f})")
