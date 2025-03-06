import json

# Load existing expenses from file
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save expenses to file
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

# Add an expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    
    expense = {"date": date, "amount": amount, "category": category, "description": description}
    expenses.append(expense)
    save_expenses()
    print("Expense added successfully!\n")

# List all expenses
def list_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. {expense['date']} - {expense['category']} - ${expense['amount']} ({expense['description']})")

# Main menu
def main():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

# Run the program
expenses = load_expenses()
main()