FILENAME = "/Users/Renee/Python/AI Agent Learning/wk3-To-Do_List/TaskList.txt"
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
def main():
    tracker = load_tasks()
    while True:
        choice = input("\n=== MENU ===\n1. Add task\n2. Mark task as done\n3. Delete task(s)\n4. Exit\n5. Print list\nChoose an option (1-4): ")
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
main()