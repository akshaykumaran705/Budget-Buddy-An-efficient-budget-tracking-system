"""
ExpenseTracker.py
Defines an `ExpenseTracker` class for tracking categorized expenses. 

Attributes:
- name (public): Name of the expense tracker.
- expenses (public): Dictionary to store expenses by category.
- __total_expense (private): Tracks the total expense.

Methods:
- add_expense(category, amount): Adds an expense to the specified category and updates the total.
- __update_total(amount): Private method to update the total expense.
- get_total_expense(): Returns the total expense.
- display_expenses(): Displays a summary of all categorized expenses and the total expense.
- __repr__(): Provides a string representation of the class instance.
"""
class ExpenseTracker:
    def __init__(self, name):
        self.name = name  # Public attribute
        self.expenses = {}  # Public attribute (dictionary)
        self.__total_expense = 0.0  # Private attribute

    def add_expense(self, category, amount):
        """Public method: Adds an expense to the tracker."""
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
        self.__update_total(amount)

    def __update_total(self, amount):
        """Private method: Updates the total expense."""
        self.__total_expense += (amount)*(-1)

    def get_total_expense(self):
        """Public method: Returns the total expense."""
        return self.__total_expense

    def display_expenses(self):
        """Public method: Displays all expenses."""
        print("\nExpense Details:")
        for category, amount in self.expenses.items():
            print(f"  - {category}: ${amount:.2f}")
        print(f"  Total Expense: ${self.__total_expense:.2f}")

    def __repr__(self):
        """Representation of the class."""
        return f"ExpenseTracker(name='{self.name}', total_expense={self.__total_expense:.2f})"
