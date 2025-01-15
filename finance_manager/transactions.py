from .db import get_connection
from datetime import datetime

def add_transaction(transaction_type, category, amount, description=''):
    conn = get_connection()
    cursor = conn.cursor()
    date = datetime.now().strftime('%Y-%m-%d')
    cursor.execute('''
        INSERT INTO transactions (date, type, category, amount, description)
        VALUES (?, ?, ?, ?, ?)
    ''', (date, transaction_type, category, amount, description))
    conn.commit()
    conn.close()

def view_transactions(start_date=None, end_date=None, category=None, transaction_type=None):
    conn = get_connection()
    cursor = conn.cursor()
    query = 'SELECT id, date, type, category, amount, description FROM transactions WHERE 1=1'
    params = []
    if start_date:
        query += ' AND date >= ?'
        params.append(start_date)
    if end_date:
        query += ' AND date <= ?'
        params.append(end_date)
    if category:
        query += ' AND category = ?'
        params.append(category)
    if transaction_type:
        query += ' AND type = ?'
        params.append(transaction_type)
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows
