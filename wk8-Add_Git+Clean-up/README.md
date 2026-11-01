# Personal Command-Line Assistant

This code is for anyone really. It is a personal command-line assistant that gets inputs from the user and has an expense tracker, to-do list, password generator, and weather forecast.

## Features
- **Expense Tracker:**
    + add expenses with category and note
    + delete expense entry
    + show total spent
    + show total spent in a specific category
    + show a montly summary of spending
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
export OPENWEATHER_API_KEY="your_key_here"

## How to run
[The command, in a code block. Your filename has spaces and a "+", so think
about whether the command needs quotation marks.]
Once you run the program, it will print this:
```=== MENU ===
1. Expense Tracker
2. To-do List
3. Password Generator
4. Weather
5. Exit
Choose an option (1-5): ```
Then just follow along and read the code. It's pretty explanatory.

## Example
If I wanted to make a task list for the day, I could just add my tasks in the morning then mark them done as I complete them throughout the day.

## Notes
Expenses and tasks will be saved in a separate json file. However favorite cities and passwords will be saved in a list, so once you close the program, your favorites will be deleted.