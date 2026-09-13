from datetime import datetime
FILENAME = "/Users/Renee/Python/AI Agent Learning/wk2-Improve_Expense_Tracker/Expenses.txt"
def load_data():
    tracker=[]
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                line=line.strip()
                if line:
                    parts = line.split("|")
                    line_to_tracker = {"amount": float(parts[0]), "category": parts[1], "note": parts[2], "date": parts[3]}
                    tracker.append(line_to_tracker)
    except FileNotFoundError:
       pass
    return tracker
def save_data(tracker):
   with open(FILENAME, "w") as file:
      for item in tracker:
         line = f"{item['amount']}|{item['category']}|{item['note']}|{item['date']}\n"
         file.write(line)
def add_expense(tracker):
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
       print("Invalid amount. Please enter a number.")
       return
    category = input("Enter category: ").strip().lower()
    note = input("Enter any notes (optional): ").strip().lower()
    date_stamp = datetime.now().strftime("%m-%Y") 
    line_of_tracker = {"amount":amount, "category":category, "note":note, "date": date_stamp}
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
def delete_expense_item(tracker):
   print("\n=== Current Expenses ===\n")
   for index, item in enumerate(tracker):
      print(f"[{index+1}] ${item['amount']:.2f} | {item['category'].capitalize()} | {item['note']} ({item['date']})")
   try:
      choice = int(input("\nEnter which index of expense: ")) - 1
      if 0<=choice<len(tracker):
         removed = tracker.pop(choice)
         save_data(tracker)
         print(f"Successfully deleted: ${removed['amount']:.2f} from '{removed['category'].capitalize()}'")
      else:
         print("Invalid selection number.")
   except ValueError:
      print("Please enter a valid tracking number.")
def show_monthly_summary(tracker):
   choice = input("Enter month and year (MM-YYYY, e.g., 09-2026): ").strip()
   total = sum(item["amount"] for item in tracker if item["date"] == choice)
   if total == 0:
      print(f"No expenses recorded for {choice}.")
   else:
      print(f"Total spent in {choice}: ${total:.2f}")
def main():
 tracker = load_data()
 while True:
    choice = input("\n=== Personal Expense Tracker ===\n1. Add Expense\n2. Show Total Spent\n3. Show Spending by Category\n4. Delete an Expense\n5. Show Monthly Summary\n6. Exit\nChoose an option (1-6): ")
    if choice == "1":
       add_expense(tracker)
    elif choice == "2":
       show_total(tracker)
    elif choice == "3":
       show_total_by_specific_category(tracker)
    elif choice == "4":
       delete_expense_item(tracker)
    elif choice == "5":
       show_monthly_summary(tracker)
    elif choice == "6":
       print("Exiting...")
       break
    else:
       print("Invalid input.")
main()