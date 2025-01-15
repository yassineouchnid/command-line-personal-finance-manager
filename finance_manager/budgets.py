from .db import get_connection

def set_budget(category, amount):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO budgets (category, amount)
        VALUES (?, ?)
        ON CONFLICT(category) DO UPDATE SET amount=excluded.amount
    ''', (category, amount))
    conn.commit()
    conn.close()

def get_budgets():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT category, amount FROM budgets')
    budgets = cursor.fetchall()
    conn.close()
    return budgets
