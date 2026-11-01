# Personal Command-Line Assistant

This code is for anyone really. It is a personal command-line assistant that gets inputs from the user and has an expense tracker, to-do list, password generator, and weather forecast.

## Features
- **Expense Tracker:**
    + add expenses with category and note
    + delete expense entry
    + show total spent
    + show total spent in a specific category
    + show a monthly summary of spending
    + save and load expenses onto a separate file
- **To-Do List:**
    + add tasks
    + mark tasks as done
    + delete tasks
    + save and load tasks onto a separate file
- **Password Generator:**
    + generate strong passwords
    + check the strength of passwords
    + save password to favorites
- **Weather:** 
    + show a three-day forecast of a city
        * temperature, condition, and advice
    + save city to favorites
    + check weather for all favorite cities
    + give clothing suggestions

## Requirements
- Python 3
- The `requests` library: `pip install requests`
- A free OpenWeatherMap API key

## Setup
You first need to give the program an API key to check the weather.
So in your terminal, enter:
`export OPENWEATHER_API_KEY="your_key_here"`

FYI: export only lasts for the current terminal window

## How to run
First input `cd wk8-Add_Git+Clean-up`. Then enter `python3 "Add Git + Clean-up.py"` into the terminal to run the code.
Then this will pop up:
```
=== MENU ===
1. Expense Tracker
2. To-do List
3. Password Generator
4. Weather
5. Exit
Choose an option (1-5): 
```
Enter a number 1 to 5, then it will lead you to another menu page for the different functions: expense tracker, to-do list, password generator, and weather forecast. Enter another number based on that menu system and enter anything that the code asks.

## Example
To add a task, choose 2 (To-do List), then 1 (Add task), then type your task, like Buy milk.

## Notes
Expenses and tasks will be saved in a separate json file. However favorite cities and passwords will be saved in a list, so once you close the program, your favorites will be deleted.