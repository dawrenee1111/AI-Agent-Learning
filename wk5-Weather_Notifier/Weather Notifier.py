import json
import requests
def main():
    city = input("Enter a city name: ")
    api_key = "c674a98c9d54acfbf852231b11ed5d74"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    data = requests.get(url).json()
    city_name = data["name"]
    temp = data["main"]["temp"]
    condition = data["weather"][0]["description"]

    if "rain" in condition or "drizzle" in condition:
        advice = "Take an umbrella!"
    elif "snow" in condition:
        advice = "Wear a heavy coat and boots!"
    elif temp > 28:
        advice = "It's hot outside! Wear sunscreen and drink lots of water."
    elif temp < 10:
        advice = "It's chilly outside. Wear a jacket."
    else:
        advice = "Enjoy the pleasant weather!"

    print(f"City name: {city_name}")
    print(f"Temperature: {temp} °C")
    print(f"Weather: {condition.title()}")
    print("Advice: {advice}")

main()