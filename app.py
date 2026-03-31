import pandas as pd
import os
from datetime import datetime

FILE = "data/expenses.csv"

def initialize_file():
    if not os.path.exists(FILE):
        df = pd.DataFrame(columns=["date", "amount", "category", "description"])
        df.to_csv(FILE, index=False)

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/etc): ")
    description = input("Enter description: ")

    df = pd.read_csv(FILE)

    new_entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "amount": amount,
        "category": category,
        "description": description
    }

    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(FILE, index=False)

    print("Expense added!")

def view_expenses():
    df = pd.read_csv(FILE)
    print(df)
    print("\nTotal Spending:", df["amount"].sum())
    
    print("\nSpending by Category:")
    print(df.groupby("category")["amount"].sum())
def main():
    initialize_file()

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
    