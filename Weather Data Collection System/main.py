# main.py
from dotenv import load_dotenv
load_dotenv()

from weather_fetcher import WeatherFetcher

def main():
    cities = ["Mumbai", "London", "New York"]  # change as needed
    wf = WeatherFetcher()  # will read OPENWEATHER_API_KEY from environment

    for city in cities:
        try:
            data = wf.fetch(city, units="imperial")
            print(f"{data['city']}: {data['temp']}°F, {data['humidity']}% — {data['condition']}")
        except Exception as e:
            print(f"Failed to fetch weather for {city}: {e}")

if __name__ == "__main__":
    main()
