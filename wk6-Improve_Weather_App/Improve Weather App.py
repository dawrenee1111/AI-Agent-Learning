import json, requests
favorites = []
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
    print(f"=== 3-Day Forecast for {city} ===")
    print(f"Today:\n\tDate: {date_list[0]}\n\tTemperature: {temp_list[0]} °C\n\tWeather: {description_list[0]}\n\tAdvice: {get_clothing_suggestions(temp_list[0], description_list[0])}")
    print(f"Tomorrow:\n\tDate: {date_list[1]}\n\tTemperature: {temp_list[1]} °C\n\tWeather: {description_list[1]}\n\tAdvice: {get_clothing_suggestions(temp_list[1], description_list[1])}")
    print(f"The Day After Tomorrow:\n\tDate: {date_list[2]}\n\tTemperature: {temp_list[2]} °C\n\tWeather: {description_list[2]}\n\tAdvice: {get_clothing_suggestions(temp_list[2], description_list[2])}")

def main():
    while True:
        choice = input("\n=== MENU ===\n1. Show 3-day forecast\n2. Save to favorites\n3. View favorites.\n4. Check weather for all favorites.\n5. Exit\nChoose an option (1-5): ")
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
                favorites.append(fav_city)
        elif choice == "3":
            print("=== Favorite Cities ===")
            if not favorites:
                print("The list is empty.")
            for indx, item in enumerate(favorites):
                print(f"{indx+1}. {item}")
        elif choice == "4":
            for cty in favorites:
                show_3_day_forecast(cty)
        elif choice == "5":
            print("Exiting...")
            break
main()