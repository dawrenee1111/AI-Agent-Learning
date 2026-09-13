def add_expense(tracker):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ").strip().lower()
    notes = input("Enter notes(optional): ").strip().lower()
    tracker.append({"amount": amount, "category": category, "notes": notes})
def show_total(tracker):
    allCatSum=0
    for item in tracker:
        allCatSum += item["amount"]
    print(f"Total amount spent: ${allCatSum:.2f}")
def show_by_category(tracker):

    specificCategory = input("Enter what category of expenses: ").strip().lower()
    specCatSum=0
    for item in tracker:
        if (item["category"] == specificCategory):
            specCatSum += item["amount"]
    print(f"Total expenses in {specificCategory}: ${specCatSum:.2f}")
def readFile():
    filename = f"Expenses.txt"
    with open(filename, "r") as file:
        lines = file.readLines()
def main():
    readFile()
    tracker=[]
    while True:
        choice = input("__MENU__\n1. Add Expense\n2. Show Total Spent\n3. Show Total Spent in Category\n4. Delete Expense\n5. Exit\n")
        if choice == "1":
            add_expense(tracker)
        elif choice == "2":
            show_total(tracker)
        elif choice == "3":
            show_by_category(tracker)
        elif choice == "4":
            for index, item in enumerate(tracker):
                print(f"{index}. Amount: ${item["amount"]} in {item["category"]}. Notes: {item["notes"]}")
            indx = int(input("Enter index of item to delete: "))
            with open("Expenses.txt", "r") as file:
                lines = file.readlines()
                with open("Expenses.txt", "w") as file:
                    file.write(lines.pop(indx))
        elif choice == "5":
            print("Your data has been saved. Exiting...")
            filename = f"Expenses.txt"
            with open(filename, "a") as file:
                for item in tracker:
                    file.write(f"Amount: {item['amount']}, Category: {item['category']}, Notes: {item['notes']}\n")
            break
        else:
            print("Sorry. Invalid input.")
main()