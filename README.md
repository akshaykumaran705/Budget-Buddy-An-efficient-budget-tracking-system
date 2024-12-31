# **Budget Tracker - README**

## **Overview**

The **Budget Tracker** is a Python-based application that helps users upload their bank statements, track expenses, set budgets, and categorize transactions. The program provides insights into financial habits and helps users stay within budget by comparing actual spending with set limits.

## **Project Structure**

- **main.py**: The main file that runs the program.
- **categories.py**: Contains predefined categories for transaction categorization.
- **test_data.csv**: Sample CSV file containing bank transaction data.
- **README.md**: This file containing instructions for running the program.

## **Steps to Run the Program**

### **Prerequisites**

- Python 3.x installed on your machine.
- A CSV file containing transaction data. You can use the **test_data.csv** file or upload your own.
  
### **Installation and Setup**

1. **Download the project files**:  
   Ensure you have all the files (**main.py**, **categories.py**, **test_data.csv**, and **README.md**) in a single folder.

### **Running the Program**

1. Ensure the **main.py** file is in the same directory as the CSV input file, or set the file path in the code.
   
2. Open a terminal or command prompt and navigate to the project folder (if not already there).
   
3. Execute the **main.py** file:
    ```bash
    python main.py
    ```

4. Follow the on-screen prompts to:
    - Upload your bank statement CSV file.
    - Set a budget limit.
    - View the spending summary and track your expenses.
    
### **Program Output**

- The program will display:
    - The list of transactions from the uploaded CSV file.
    - The total expenses and comparison with the set budget.
    - A categorized spending summary, including the highest and lowest spending categories.

## **Notes**

- Ensure your CSV file is formatted correctly with columns for description, amount, and date.
- If there are errors, check for formatting issues in the input file or invalid inputs.

## **Future Enhancements**

- Integration of bank API for real-time data.
- Visualization of expenses through charts.
- Multi-currency support.
  


This project is developed as part of the **Applied Data Analytics program** at **Boston University**.


