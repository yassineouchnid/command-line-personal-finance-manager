# main.py
import argparse
from finance_manager.db import initialize_db
from finance_manager.transactions import add_transaction, view_transactions
from finance_manager.budgets import set_budget, get_budgets
from finance_manager.reports import generate_summary, generate_ascii_chart

def main():
    initialize_db()
    
    parser = argparse.ArgumentParser(
        description='Command-Line Personal Finance Manager'
    )
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add Transaction
    parser_add = subparsers.add_parser('add', help='Add a new transaction')
    parser_add.add_argument('type', choices=['Income', 'Expense'], help='Type of transaction')
    parser_add.add_argument('category', help='Category of transaction')
    parser_add.add_argument('amount', type=float, help='Amount')
    parser_add.add_argument('--description', help='Description', default='')

    # View Transactions
    parser_view = subparsers.add_parser('view', help='View transactions')
    parser_view.add_argument('--start', help='Start date (YYYY-MM-DD)')
    parser_view.add_argument('--end', help='End date (YYYY-MM-DD)')
    parser_view.add_argument('--category', help='Filter by category')
    parser_view.add_argument('--type', choices=['Income', 'Expense'], help='Filter by type')

    # Set Budget
    parser_budget = subparsers.add_parser('budget', help='Set a budget for a category')
    parser_budget.add_argument('category', help='Category to set budget for')
    parser_budget.add_argument('amount', type=float, help='Budget amount')

    # View Budgets
    parser_view_budget = subparsers.add_parser('view_budget', help='View all budgets')

    # Generate Summary
    parser_summary = subparsers.add_parser('summary', help='Generate summary report')
    parser_summary.add_argument('--start', help='Start date (YYYY-MM-DD)')
    parser_summary.add_argument('--end', help='End date (YYYY-MM-DD)')

    # Generate ASCII Chart
    parser_chart = subparsers.add_parser('chart', help='Generate ASCII chart of spending')
    parser_chart.add_argument('--start', help='Start date (YYYY-MM-DD)')
    parser_chart.add_argument('--end', help='End date (YYYY-MM-DD)')

    args = parser.parse_args()

    if args.command == 'add':
        add_transaction(args.type, args.category, args.amount, args.description)
        print('Transaction added successfully.')

    elif args.command == 'view':
        transactions = view_transactions(args.start, args.end, args.category, args.type)
        if transactions:
            from tabulate import tabulate
            table = []
            for txn in transactions:
                table.append(txn)
            print(tabulate(table, headers=['ID', 'Date', 'Type', 'Category', 'Amount', 'Description'], tablefmt='pretty'))
        else:
            print('No transactions found.')

    elif args.command == 'budget':
        set_budget(args.category, args.amount)
        print(f'Budget set for category "{args.category}" to ${args.amount:.2f}.')

    elif args.command == 'view_budget':
        budgets = get_budgets()
        if budgets:
            from tabulate import tabulate
            table = []
            for budget in budgets:
                table.append(budget)
            print(tabulate(table, headers=['Category', 'Budget Amount'], tablefmt='pretty'))
        else:
            print('No budgets set.')

    elif args.command == 'summary':
        generate_summary(args.start, args.end)

    elif args.command == 'chart':
        generate_ascii_chart(args.start, args.end)

    else:
        parser.print_help()

if __name__ == '__main__':
    main()
