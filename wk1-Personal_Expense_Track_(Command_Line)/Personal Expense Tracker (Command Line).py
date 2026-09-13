FILENAME = "/Users/Renee/Python/AI Agent Learning/wk1-Personal_Expense_Track_(Command_Line)/Expenses.txt"
def load_data():
    tracker=[]
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                line=line.strip()
                if line:
                    parts = line.split("|")
                    line_to_tracker = {"amount": float(parts[0]), "category": parts[1], "note": parts[2]}
                    tracker.append(line_to_tracker)
    except FileNotFoundError:
       pass
    return tracker
def save_data(tracker):
   with open(FILENAME, "w") as file:
      for item in tracker:
         line = f"{item['amount']}|{item['category']}|{item['note']}\n"
         file.write(line)
def add_expense(tracker):
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
       print("Invalid amount. Please enter a number.")
       return
    category = input("Enter category: ").strip().lower()
    note = input("Enter any notes (optional): ").strip().lower()
    line_of_tracker = {"amount":amount, "category":category, "note":note}
    tracker.append(line_of_tracker)
    save_data(tracker)
    print("Expense added and saved successfully!")
def show_total(tracker):
   total = sum(item["amount"] for item in tracker)
   print(f"Total spent is ${total:.2f}")
def show_total_by_specific_category(tracker):
    specific_category = input("Enter category: ").strip().lower()
    total = sum(item["amount"] for item in tracker if item["category"] == specific_category)
    if total == 0:
        print(f"No expenses found or recorded under '{specific_category}'.")
    else:
        print(f"Total spent in {specific_category} is ${total:.2f}")
def main():
 tracker = load_data()
 while True:
    choice = input("\n=== Personal Expense Tracker ===\n1. Add Expense\n2. Show Total Spent\n3. Show Spending by Category\n4. Exit\nChoose an option (1-4): ")
    if choice == "1":
       add_expense(tracker)
    elif choice == "2":
       show_total(tracker)
    elif choice == "3":
       show_total_by_specific_category(tracker)
    elif choice == "4":
       print("Exiting...")
       break
    else:
       print("Invalid input.")
main()
