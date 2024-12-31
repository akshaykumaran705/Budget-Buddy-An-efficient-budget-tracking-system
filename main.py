"""
main.py
Processes a bank statement CSV file to categorize transactions, analyze spending against a budget, 
and generate a spending summary. Provides options to view the file, calculate budget impact, 
and display categorized spending details.
"""
import csv

description_to_category = {
    "starbucks": "Food & Beverages",
    "amc": "Entertainment",
    "macys": "Clothing",
    "xfinity": "Utilities",
    "star osco": "Groceries",
    "target": "Shopping",
    "walmart": "Groceries",
    "nike": "Clothing",
    "shell": "Gas",
    "chevron": "Gas",
    "apple": "Electronics",
    "best buy": "Electronics",
    "netflix": "Subscriptions",
    "spotify": "Subscriptions",
    "gym": "Health & Fitness",
    "restaurant": "Food & Beverages",
    "cvs": "Health & Wellness",
    "walgreens": "Health & Wellness",
    "amazon": "Shopping",
    "electric bill": "Utilities",
    "uber": "Transportation",
    "lyft": "Transportation",
    "place": "Rent",
    "fossil":"Clothing",
    "zelle":"Bank Transfer",
}

def categorize_description(description):
    """Categorize a purchase description."""
    normalized_desc = description.lower()
    for keyword, category in description_to_category.items():
        if keyword.lower() in normalized_desc:
            return category
    return "Other"

def load_bank_statement(file_name):
    """Load bank transactions from a CSV file."""
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            transactions = []
            for row in csv_reader:
                description = row['Description']
                amount = float(row['Amount'])
                if amount < 0:  # Filter debited transactions
                    category = categorize_description(description)
                    transactions.append((category, abs(amount)))
            return transactions
    except FileNotFoundError:
        print("Bank statement file not found!")
        return []
    except UnicodeDecodeError as e:
        print(f"Error reading file: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def display_file_content(file_name):
    """Display the content of the uploaded file."""
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            print("\nUploaded File Content:")
            print(file.read())
    except FileNotFoundError:
        print("Bank statement file not found!")

def calculate_budget(transactions, budget):
    """Calculate if the total spending exceeds the budget."""
    total_expenses = sum(amount for _, amount in transactions)
    print(f"\nTotal Expenses: ${total_expenses:.2f}")
    
    if total_expenses > budget:
        print(f"You have exceeded your budget by ${total_expenses - budget:.2f}")
    else:
        print(f"You are within your budget. Remaining budget: ${budget - total_expenses:.2f}")

def display_spending_summary(transactions, file_name):
    """Display spending summary by category and additional details."""
    category_totals = {}
    credited_amount = 0.0

    # Categorize transactions and calculate totals
    with open(file_name, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            description = row['Description']
            amount = float(row['Amount'])
            if amount < 0:  # Debited transactions
                category = categorize_description(description)
                if category in category_totals:
                    category_totals[category] += abs(amount)
                else:
                    category_totals[category] = abs(amount)
            else:  # Credited transactions
                credited_amount += amount

    # Display spending summary
    print("\nSpending Summary:")
    for category, total in category_totals.items():
        print(f"  - {category}: ${total:.2f}")
    total_expenses = sum(category_totals.values())
    print(f"Total Expenses: ${total_expenses:.2f}")

    # Find highest and lowest spending
    if category_totals:
        highest_category = max(category_totals, key=category_totals.get)
        lowest_category = min(category_totals, key=category_totals.get)
        print(f"Highest Spending: {highest_category} - ${category_totals[highest_category]:.2f}")
        print(f"Lowest Spending: {lowest_category} - ${category_totals[lowest_category]:.2f}")

    # Display total credited amount
    print(f"Total Credited Amount: ${credited_amount:.2f}")


def main():
    # Set default file path
    file_name = "/Users/akshaykumaran/Documents/Python Project/bank_statement.csv"  

    # Check if file exists before proceeding
    try:
        with open(file_name, 'r', encoding='utf-8'):
            pass
    except FileNotFoundError:
        print(f"Default file '{file_name}' not found. Please ensure the file exists at the specified path.")
        return

    while True:
        print("\nOptions:")
        print("1. View uploaded statement file")
        print("2. Enter budget and check expenses")
        print("3. View spending summary")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            display_file_content(file_name)

        elif choice == "2":
            try:
                budget = float(input("Enter your budget: "))
                transactions = load_bank_statement(file_name)
                calculate_budget(transactions, budget)
            except ValueError:
                print("Invalid input. Please enter a numeric value for the budget.")

        elif choice == "3":
            transactions = load_bank_statement(file_name)
            display_spending_summary(transactions, file_name)

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
