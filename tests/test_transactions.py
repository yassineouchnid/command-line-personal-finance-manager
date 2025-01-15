# tests/test_transactions.py
import unittest
from finance_manager.transactions import add_transaction, view_transactions
from finance_manager.db import initialize_db, get_connection

class TestTransactions(unittest.TestCase):
    def setUp(self):
        initialize_db()
        # Clear the transactions table before each test
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM transactions')
        conn.commit()
        conn.close()

    def test_add_transaction(self):
        add_transaction('Income', 'Salary', 3000, 'Monthly salary')
        transactions = view_transactions()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0][2], 'Income')
        self.assertEqual(transactions[0][3], 'Salary')
        self.assertEqual(transactions[0][4], 3000)

    def test_view_transactions_with_filters(self):
        add_transaction('Expense', 'Groceries', 150)
        add_transaction('Income', 'Freelance', 500)
        transactions = view_transactions(transaction_type='Expense')
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0][2], 'Expense')

if __name__ == '__main__':
    unittest.main()
