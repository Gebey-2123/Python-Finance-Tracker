import json
import os
from datetime import datetime

class FinanceTracker:
    def __init__(self):
        self.filename = "expenses.json"
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.expenses = json.load(file)
        else:
            self.expenses = []

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, category, amount):
        entry = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "category": category,
            "amount": float(amount)
        }
        self.expenses.append(entry)
        self.save_data()
        print(f"✅ Successfully added {amount} ETB to {category}.")

    def show_summary(self):
        if not self.expenses:
            print("📭 No expenses recorded yet.")
            return

        total = sum(item['amount'] for item in self.expenses)
        print("\n--- 📊 Finance Summary ---")
        print(f"Total Spent: {total} ETB")
        
        categories = {}
        for item in self.expenses:
            cat = item['category']
            categories[cat] = categories.get(cat, 0) + item['amount']
        
        for cat, amt in categories.items():
            percentage = (amt / total) * 100
            print(f"- {cat}: {amt} ETB ({percentage:.1f}%)")
        print("--------------------------\n")

def main():
    tracker = FinanceTracker()
    while True:
        print("💰 Personal Finance Tracker")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            cat = input("Enter category (e.g. Food, Transport, Internet): ")
            amt = input("Enter amount: ")
            try:
                tracker.add_expense(cat, amt)
            except ValueError:
                print("❌ Invalid amount. Please enter a number.")
        elif choice == '2':
            tracker.show_summary()
        elif choice == '3':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()