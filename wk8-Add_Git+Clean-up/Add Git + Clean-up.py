import requests, json, string, os, secrets
from datetime import datetime
API_KEY = os.getenv("OPENWEATHER_API_KEY")
favorite_passwords = []
favorite_cities=[]
TASK_FILE = "tasks.json"
EXPENSE_FILE = "expenses.json"
def load_json(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
       return []
def save_json(data, filename):
   with open(filename, "w") as file:
      json.dump(data, file, indent=2)
def expense_tracker():
    expense_tracker = load_json(EXPENSE_FILE)
    while True:
        choice = input("\n=== Expense Tracker ===\n1. Add Expense\n2. Show Total Spent\n3. Show Spending by Category\n4. Delete an Expense\n5. Show Monthly Summary\n6. Back to Main Menu\nChoose an option (1-6): ")
        if choice == "1":
            add_expense(expense_tracker)
        elif choice == "2":
            show_total(expense_tracker)
        elif choice == "3":
            show_total_by_specific_category(expense_tracker)
        elif choice == "4":
            delete_expense_item(expense_tracker)
        elif choice == "5":
            show_monthly_summary(expense_tracker)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid input.")
def add_expense(expense_tracker):
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
       print("Invalid amount. Please enter a number.")
       return
    category = input("Enter category: ").strip().lower()
    note = input("Enter any notes (optional): ").strip().lower()
    date_stamp = datetime.now().strftime("%m-%Y") 
    line_of_tracker1 = {"amount":amount, "category":category, "note":note, "date":date_stamp}
    expense_tracker.append(line_of_tracker1)
    save_json(expense_tracker, EXPENSE_FILE)
    print("Expense added and saved successfully!")
def show_total(expense_tracker):
   total = sum(item["amount"] for item in expense_tracker)
   print(f"Total spent is ${total:.2f}")
def show_total_by_specific_category(expense_tracker):
    specific_category = input("Enter category: ").strip().lower()
    total = sum(item["amount"] for item in expense_tracker if item["category"] == specific_category)
    if total == 0:
        print(f"No expenses found or recorded under '{specific_category}'.")
    else:
        print(f"Total spent in {specific_category} is ${total:.2f}")
def delete_expense_item(expense_tracker):
   print("\n=== Current Expenses ===\n")
   if not expense_tracker:
        print("No expenses to delete.")
        return expense_tracker
   for index, item in enumerate(expense_tracker):
      print(f"[{index+1}] ${item['amount']:.2f} | {item['category'].capitalize()} | {item['note']} ({item['date']})")
   try:
      choice = int(input("\nEnter which index of expense to delete: ")) - 1
      if 0<=choice<len(expense_tracker):
         removed = expense_tracker.pop(choice)
         save_json(expense_tracker, EXPENSE_FILE)
         print(f"Successfully deleted: ${removed['amount']:.2f} from '{removed['category'].capitalize()}'")
      else:
            print("Invalid selection number.")
   except ValueError:
        print("Please enter a valid tracking number.")
   return expense_tracker
def show_monthly_summary(expense_tracker):
   choice = input("Enter month and year (MM-YYYY, e.g., 09-2026): ").strip()
   total = sum(item["amount"] for item in expense_tracker if item["date"] == choice)
   if total == 0:
      print(f"No expenses recorded for {choice}.")
   else:
      print(f"Total spent in {choice}: ${total:.2f}")
def add_task(task_tracker):
    task = input("Enter task: ")
    completed_or_not = input("Is the task completed or not? (y/n): ").lower().strip()
    is_completed = completed_or_not in ["y", "yes"]
    line_of_tracker = {"task":task, "completed":is_completed}
    task_tracker.append(line_of_tracker)
    save_json(task_tracker, TASK_FILE)
    print("Task added and saved successfully!")
def print_list(task_tracker):
    print("\n=== Current Tasks ===")
    if not task_tracker:
        print("No tasks in to do list.")
        return task_tracker
    for index, item in enumerate(task_tracker):
      if item['completed'] == True:
          y_n = "done"
      else:
          y_n = "not yet done"
      print(f"[{index+1}] {item['task']}? {y_n}")
def mark_done(task_tracker):
    print_list(task_tracker)
    try:
        choice = int(input("Enter which index of task to mark as done? "))-1
        if 0<=choice<len(task_tracker):
            if task_tracker[choice]["completed"] == True:
                print("This task has already been completed!")
            else:
                task_tracker[choice]["completed"] = True
                save_json(task_tracker, TASK_FILE)
                print("Okay! Marked as done.")
        else:
            print("Invalid selection number.")
    except ValueError:
        print("Invalid selection number.")
    return task_tracker
def delete_task(task_tracker):
    print_list(task_tracker)
    try:
        choice = int(input("\nEnter which index of task to delete: ")) - 1
        if 0<=choice<len(task_tracker):
            removed = task_tracker.pop(choice)
            save_json(task_tracker, TASK_FILE)
            print(f"Successfully deleted: {removed['task']}")
        else:
            print("Invalid selection number.")
    except ValueError:
        print("Please enter a valid task number.")
def to_do_list():
    task_tracker = load_json(TASK_FILE)
    while True:
        choice = input("\n=== To-Do List ===\n1. Add task\n2. Mark task as done\n3. Delete task\n4. Back to Main Menu\nChoose an option (1-4): ")
        if (choice == "1"):
            add_task(task_tracker)
        elif (choice == "2"):
            mark_done(task_tracker)
        elif (choice == "3"):
            delete_task(task_tracker)
        elif (choice == "4"):
            print("Exiting...")
            break
        else:
            print("Invalid input.")
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password
def check_strength(password):
    length = len(password)
    has_lower = False
    has_capital = False
    has_punctuation = False
    has_digit = False
    for char in password:
        if char in string.ascii_lowercase:
            has_lower = True
        elif char in string.ascii_uppercase:
            has_capital = True
        elif char in string.punctuation:
            has_punctuation = True
        elif char in string.digits:
            has_digit = True
    score = sum([length>=8, has_lower, has_capital, has_punctuation, has_digit])
    if score <= 2:
        return "Weak"
    elif score <=4:
        return "Moderate"
    elif score == 5:
        return "Strong"
def offer_to_save(pwd):
    if input("Save to favourites? (y/n): ").lower() == "y":
        favorite_passwords.append(pwd)
        print("Saved successfully!\n")
def password_generator():
    while True:
        choice = input("\n=== Password Generator ===\n1. Generate Password\n2. Check Password's Strength\n3. View Favorites\n4. Back to Main Menu\nChoose an option (1-4): ")
        if choice == "1":
            pwd_len = input("Enter password length (default 12): ")
            if pwd_len.isdigit():
                length=int(pwd_len)
            else:
                length=12
            pwd = generate_password(length)
            print(f"\nGenerated Password: {pwd}")
            print(f"Strength: {check_strength(pwd)}")
            offer_to_save(pwd)
        elif choice == "2":
            pwd = input("Enter password to check: ")
            print(f"\nPassword assessment: {check_strength(pwd)}")
            offer_to_save(pwd)
        elif choice == "3":
            print("\n=== Saved Favorites ===")
            if not favorite_passwords:
                print("No passwords saved yet.")
            else:
                for index, password in enumerate(favorite_passwords):
                    print(f"{index+1}. {password}")
        elif choice == "4":
            print("Goodbye! Stay strong...")
            break
        else:
            print("Invalid choice! Please pick 1, 2, 3, or 4.")
def get_clothing_suggestions(temp, condition):
    if "rain" in condition or "drizzle" in condition:
        return "Take a raincoat or an umbrella."
    elif "snow" in condition:
        return "Wear a heavy coat, gloves, scarf and boots!"
    elif temp > 25:
        return "It's hot outside! Wear t-shirt, shorts, sunscreen and drink lots of water."
    elif temp < 12:
        return "It's chilly outside! Wear a warm jacket."
    else:
        return "Wear a light jacket or long sleeves."
def fetch_forecast(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        print("City not found. Please check the spelling and try again.")
        return None
    return response.json()
def show_3_day_forecast(city):
    data = fetch_forecast(city)
    if data is None:
        print("Could not retrieve forecast. Please try another city.")
        return
    city_name = data["city"]["name"]
    forecast_list = data["list"]
    temp_list=[]
    date_list=[]
    description_list=[]
    for item in forecast_list:
        if item["dt_txt"].endswith("12:00:00"):
            temp_list.append(item["main"]["temp"])
            description_list.append(item["weather"][0]["description"])
            part1, part2 = item["dt_txt"].split(" ")
            date_list.append(part1)
    labels = ["Today", "Tomorrow", "The Day After Tomorrow"]
    print(f"\n=== 3-Day Forecast for {city_name} ===")
    for i in range(3):
        advice = get_clothing_suggestions(temp_list[i], description_list[i])
        print(f"{labels[i]}:\n\tDate: {date_list[i]}\n\tTemperature: {temp_list[i]} °C\n\tWeather: {description_list[i]}\n\tAdvice: {advice}")
def weather_menu():
    while True:
        choice = input("\n=== Weather ===\n1. Show 3-day forecast\n2. Save to favorites\n3. View favorites\n4. Check weather for all favorites\n5. Back to Main Menu\nChoose: ")
        if choice == "1":
            city = input("Enter a city name: ")
            show_3_day_forecast(city)
        elif choice == "2":
            fav_city = input("Enter city name to add to favorites: ").strip().title()
            if fetch_forecast(fav_city) is not None:
                favorite_cities.append(fav_city)
        elif choice == "3":
            print("=== Favorite Cities ===")
            if not favorite_cities:
                print("The list is empty.")
            for indx, item in enumerate(favorite_cities):
                print(f"{indx+1}. {item}")
        elif choice == "4":
            for cty in favorite_cities:
                show_3_day_forecast(cty)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
def main():
    while True:
        choice = input("\n=== MENU ===\n1. Expense Tracker\n2. To-do List\n3. Password Generator\n4. Weather\n5. Exit\nChoose an option (1-5): ")
        if choice == "1":
            expense_tracker()
        elif choice == "2":
            to_do_list()
        elif choice == "3":
            password_generator()
        elif choice == "4":
            weather_menu()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()