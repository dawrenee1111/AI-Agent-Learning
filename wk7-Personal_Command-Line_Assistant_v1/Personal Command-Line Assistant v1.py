import requests, json, string, random
favorite_cities=[]
favorite_passwords = []
FILENAME = "/Users/Renee/Python/AI Agent Learning/wk7-Personal_Command-Line_Assistant_v1/TaskList.txt"
FILENAME2 = "/Users/Renee/Python/AI Agent Learning/wk7-Personal_Command-Line_Assistant_v1/Expenses.txt"
def expense_tracker():
    tracker1 = load_data_4_expense_tracker()
    while True:
        choice = input("\n=== Expense Tracker ===\n1. Add Expense\n2. Show Total Spent\n3. Show Spending by Category\n4. Delete an Expense\n5. Show Monthly Summary\n6. Back to Main Menu\nChoose an option (1-6): ")
        if choice == "1":
            add_expense(tracker1)
        elif choice == "2":
            show_total(tracker1)
        elif choice == "3":
            show_total_by_specific_category(tracker1)
        elif choice == "4":
            delete_expense_item(tracker1)
        elif choice == "5":
            show_monthly_summary(tracker1)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid input.")
def load_data_4_expense_tracker():
    tracker1=[]
    try:
        with open(FILENAME2, "r") as file:
            for line in file:
                line=line.strip()
                if line:
                    parts = line.split("|")
                    line_to_tracker = {"amount": float(parts[0]), "category": parts[1], "note": parts[2]}
                    tracker1.append(line_to_tracker)
    except FileNotFoundError:
       pass
    return tracker1
def save_data(tracker1):
   with open(FILENAME2, "w") as file:
      for item in tracker1:
         line = f"{item['amount']}|{item['category']}|{item['note']}\n"
         file.write(line)
def add_expense(tracker1):
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
       print("Invalid amount. Please enter a number.")
       return
    category = input("Enter category: ").strip().lower()
    note = input("Enter any notes (optional): ").strip().lower()
    line_of_tracker1 = {"amount":amount, "category":category, "note":note}
    tracker1.append(line_of_tracker1)
    save_data(tracker1)
    print("Expense added and saved successfully!")
def show_total(tracker1):
   total = sum(item["amount"] for item in tracker1)
   print(f"Total spent is ${total:.2f}")
def show_total_by_specific_category(tracker1):
    specific_category = input("Enter category: ").strip().lower()
    total = sum(item["amount"] for item in tracker1 if item["category"] == specific_category)
    if total == 0:
        print(f"No expenses found or recorded under '{specific_category}'.")
    else:
        print(f"Total spent in {specific_category} is ${total:.2f}")
def delete_expense_item(tracker1):
   print("\n=== Current Expenses ===\n")
   for index, item in enumerate(tracker1):
      print(f"[{index+1}] ${item['amount']:.2f} | {item['category'].capitalize()} | {item['note']} ({item['date']})")
   try:
      choice = int(input("\nEnter which index of expense: ")) - 1
      if 0<=choice<len(tracker1):
         removed = tracker1.pop(choice)
         save_data(tracker1)
         print(f"Successfully deleted: ${removed['amount']:.2f} from '{removed['category'].capitalize()}'")
      else:
         print("Invalid selection number.")
   except ValueError:
      print("Please enter a valid tracking number.")
def show_monthly_summary(tracker1):
   choice = input("Enter month and year (MM-YYYY, e.g., 09-2026): ").strip()
   total = sum(item["amount"] for item in tracker1 if item["date"] == choice)
   if total == 0:
      print(f"No expenses recorded for {choice}.")
   else:
      print(f"Total spent in {choice}: ${total:.2f}")
def load_tasks():
    tracker = []
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                line=line.strip()
                if line:
                    parts = line.split("|")
                    line_to_tracker = {"task": parts[0], "completed": parts[1]}
                    tracker.append(line_to_tracker)
    except FileNotFoundError:
       pass
    return tracker
def save_tasks(tracker):
    with open(FILENAME, "w") as file:
        for item in tracker:
         line = f"{item['task']}|{item['completed']}\n"
         file.write(line)
def add_task(tracker):
    task = input("Enter task: ")
    completed_or_not = input("Is the task completed or not (y/n)? ").lower().strip()
    line_of_tracker = {"task":task, "completed":completed_or_not}
    tracker.append(line_of_tracker)
    save_tasks(tracker)
    print("Task added and saved successfully!")
def print_list(tracker):
    print("\n=== Current Tasks ===")
    for index, item in enumerate(tracker):
      print(f"[{index+1}] {item['task']}? {item['completed']}")
def mark_done(tracker):
    print_list(tracker)
    choice = int(input("Enter which index of task to mark as done? "))-1
    if 0<=choice<len(tracker):
        if tracker[choice]["completed"] == "y":
            print("This task has already been completed!")
        else:
            tracker[choice]["completed"] = "y"
            save_tasks(tracker)
            print("Okay! Marked as done.")
    else:
        print("Invalid selection number.")
def delete_task(tracker):
    print_list(tracker)
    try:
        choice = int(input("\nEnter which index of task to delete: ")) - 1
        if 0<=choice<len(tracker):
            removed = tracker.pop(choice)
            save_tasks(tracker)
            print(f"Successfully deleted: {removed['task']}")
        else:
            print("Invalid selection number.")
    except ValueError:
        print("Please enter a valid task number.")
def to_do_list():
    tracker = load_tasks()
    while True:
        choice = input("\n=== To-Do List ===\n1. Add task\n2. Mark task as done\n3. Delete task(s)\n4. Back to Main Menu\nChoose an option (1-4): ")
        if (choice == "1"):
            add_task(tracker)
        elif (choice == "2"):
            mark_done(tracker)
        elif (choice == "3"):
            delete_task(tracker)
        elif (choice == "4"):
            print("Exiting...")
            break
        else:
            print("Invalid input.")
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(length):
        password += random.choice(characters)
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
            save = input("Save to favourites? (y/n): ").lower()
            if save == "y":
                favorite_passwords.append(pwd)
                print("Saved successfully!\n")
        elif choice == "2":
            pwd = input("Enter password to check: ")
            print(f"\nPassword assessment: {check_strength(pwd)}")
            save = input("Save to favourites? (y/n): ").lower()
            if save == "y":
                favorite_passwords.append(pwd)
                print("Saved successfully!\n")
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
def show_3_day_forecast(city):
    api_key = "c674a98c9d54acfbf852231b11ed5d74"
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        print("City not found. Please check the spelling and try again.")
        return
    data = response.json()
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
    print(f"\n=== 3-Day Forecast for {city} ===")
    print(f"Today:\n\tDate: {date_list[0]}\n\tTemperature: {temp_list[0]} °C\n\tWeather: {description_list[0]}\n\tAdvice: {get_clothing_suggestions(temp_list[0], description_list[0])}")
    print(f"Tomorrow:\n\tDate: {date_list[1]}\n\tTemperature: {temp_list[1]} °C\n\tWeather: {description_list[1]}\n\tAdvice: {get_clothing_suggestions(temp_list[1], description_list[1])}")
    print(f"The Day After Tomorrow:\n\tDate: {date_list[2]}\n\tTemperature: {temp_list[2]} °C\n\tWeather: {description_list[2]}\n\tAdvice: {get_clothing_suggestions(temp_list[2], description_list[2])}")
def weather_menu():
    while True:
        choice = input("\n=== Weather ===\n1. Show 3-day forecast\n2. Save to favorites\n3. View favorites\n4. Check weather for all favorites\n5. Back to Main Menu\nChoose: ")
        if choice == "1":
            city = input("Enter a city name: ")
            show_3_day_forecast(city)
        elif choice == "2":
            fav_city = input("Enter city name to add to favorites: ").strip().title()
            api_key = "c674a98c9d54acfbf852231b11ed5d74"
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={fav_city}&appid={api_key}&units=metric"
            response = requests.get(url)
            if response.status_code != 200:
                print("City not found. Please check the spelling and try again.")
                continue
            else:
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
main()