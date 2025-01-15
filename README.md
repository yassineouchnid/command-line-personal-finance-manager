# Command-Line Personal Finance Manager

A powerful and user-friendly **Command-Line Personal Finance Manager** built with Python. This tool allows you to track your income, expenses, set budgets, and generate insightful financial reports—all directly from your terminal. Perfect for managing your finances efficiently without the need for complex software.

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
  - [Add a Transaction](#add-a-transaction)
  - [View Transactions](#view-transactions)
  - [Set a Budget](#set-a-budget)
  - [View Budgets](#view-budgets)
  - [Generate Summary Report](#generate-summary-report)
  - [Generate ASCII Chart](#generate-ascii-chart)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [License](#license)

---

## Features

- **Transaction Tracking:** Easily add, view, and categorize your income and expenses.
- **Budgeting:** Set monthly budgets for different categories and monitor your spending.
- **Reports:** Generate detailed summaries and visual (ASCII) reports to analyze your financial habits.
- **Data Persistence:** Securely store your data using SQLite for reliable and efficient storage.
- **User-Friendly CLI:** Intuitive command-line interface for seamless interaction.

---

## Technology Stack

- **Programming Language:** Python 3.x
- **Database:** SQLite (via Python's `sqlite3` module)
- **Libraries:**
  - `argparse` for parsing command-line arguments
  - `tabulate` for formatted table outputs
  - `colorama` for colored terminal text (optional)
  
---

## Installation

### Prerequisites

- **Python 3.x** installed on your system. [Download Python](https://www.python.org/downloads/)
  
### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yassineouchnid/command-line-personal-finance-manager.git
   cd command-line-personal-finance-manager
   ```

   *Alternatively, you can download the repository as a ZIP file and extract it.*

2. **Create a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   ```

   > **Note:** If `python` points to Python 2.x on your system, use `python3` instead:

   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

   After activation, your terminal prompt should be prefixed with `(venv)`.

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   *If you encounter issues, ensure that `pip` is updated:*

   ```bash
   pip install --upgrade pip
   ```

5. **Initialize the Database**

   The database will be automatically initialized when you run the application for the first time.

---

## Usage

Once installed, you can use the tool via the command line. Below are the available commands and how to use them.

### General Syntax

```bash
python main.py <command> [options]
```

### Commands

#### Add a Transaction

Add a new income or expense transaction.

**Syntax:**

```bash
python main.py add <Type> <Category> <Amount> [--description "Description"]
```

**Parameters:**

- `<Type>`: `Income` or `Expense`
- `<Category>`: The category of the transaction (e.g., Groceries, Salary)
- `<Amount>`: The amount of the transaction
- `--description`: (Optional) A brief description of the transaction

**Example:**

```bash
python main.py add Expense Groceries 150.75 --description "Weekly supermarket shopping"
```

#### View Transactions

View your transactions with optional filters.

**Syntax:**

```bash
python main.py view [--start YYYY-MM-DD] [--end YYYY-MM-DD] [--category Category] [--type Type]
```

**Options:**

- `--start`: (Optional) Start date in `YYYY-MM-DD` format
- `--end`: (Optional) End date in `YYYY-MM-DD` format
- `--category`: (Optional) Filter by category
- `--type`: (Optional) Filter by type (`Income` or `Expense`)

**Example:**

View all expenses in the "Groceries" category between January 1, 2025, and December 31, 2025:

```bash
python main.py view --start 2025-01-01 --end 2025-12-31 --category Groceries --type Expense
```

#### Set a Budget

Set a monthly budget for a specific category.

**Syntax:**

```bash
python main.py budget <Category> <Amount>
```

**Parameters:**

- `<Category>`: The category to set a budget for
- `<Amount>`: The budget amount

**Example:**

```bash
python main.py budget Groceries 500
```

#### View Budgets

View all your set budgets.

**Syntax:**

```bash
python main.py view_budget
```

**Example:**

```bash
python main.py view_budget
```

#### Generate Summary Report

Generate a summary report of your finances.

**Syntax:**

```bash
python main.py summary [--start YYYY-MM-DD] [--end YYYY-MM-DD]
```

**Options:**

- `--start`: (Optional) Start date in `YYYY-MM-DD` format
- `--end`: (Optional) End date in `YYYY-MM-DD` format

**Example:**

Generate a summary for the year 2025:

```bash
python main.py summary --start 2025-01-01 --end 2025-12-31
```

#### Generate ASCII Chart

Generate an ASCII bar chart of your spending habits.

**Syntax:**

```bash
python main.py chart [--start YYYY-MM-DD] [--end YYYY-MM-DD]
```

**Options:**

- `--start`: (Optional) Start date in `YYYY-MM-DD` format
- `--end`: (Optional) End date in `YYYY-MM-DD` format

**Example:**

Generate an ASCII chart for the year 2025:

```bash
python main.py chart --start 2025-01-01 --end 2025-12-31
```

---

## Testing

Ensure that the application works as expected by running unit tests.

### Running Tests

Navigate to the project root directory and run:

```bash
python -m unittest discover -s tests
```

### Example Test Cases

The `tests/` directory contains test modules for different components of the application. Below is an example of a test case for transaction functionalities.


## Project Structure

Organizing your project well ensures maintainability and scalability.

```
personal_finance_manager/
│
├── finance_manager/
│   ├── __init__.py
│   ├── db.py
│   ├── transactions.py
│   ├── budgets.py
│   ├── reports.py
│   └── utils.py
│
├── tests/
│   ├── __init__.py
│   ├── test_db.py
│   ├── test_transactions.py
│   ├── test_budgets.py
│   └── test_reports.py
│
├── data/
│   └── finance.db
│
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

**Description:**

- **finance_manager/**: Core modules handling different functionalities.
  - `db.py`: Database connection and initialization.
  - `transactions.py`: Transaction management (add, view).
  - `budgets.py`: Budget management (set, view).
  - `reports.py`: Report generation (summary, ASCII charts).
  - `utils.py`: Utility functions (if needed).
  
- **tests/**: Contains unit tests for each module.
- **data/**: Stores the SQLite database file.
- **main.py**: Entry point of the application.
- **requirements.txt**: Lists all Python dependencies.
- **README.md**: Project documentation.
- **LICENSE**: Licensing information.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements

- Inspired by the need for simple yet effective financial management tools.
- Utilizes open-source libraries to enhance functionality and user experience.

---

## Contact

For any questions or suggestions, feel free to contact me at [ouchnidyassine@gmail.com](mailto:ouchnidyassine@gmail.com).

---

**Happy Managing Your Finances!**
