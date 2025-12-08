# weather_fetcher.py
import os
import requests

class WeatherFetcher:
    """
    Simple OpenWeather current weather fetcher.
    Usage:
        wf = WeatherFetcher()          # reads OPENWEATHER_API_KEY from env
        data = wf.fetch("Mumbai")
    Returns dict: {city, temp, humidity, condition, raw}
    """

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv("OPENWEATHER_API_KEY")
        if not self.api_key:
            raise RuntimeError("OPENWEATHER_API_KEY required — set it in .env or environment")
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def fetch(self, city: str, units: str = "imperial", timeout: int = 10):
        """Fetch current weather for `city` (name or 'city,country')."""
        params = {"q": city, "appid": self.api_key, "units": units}
        resp = requests.get(self.base_url, params=params, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()

        # defensive parsing
        main = data.get("main", {})
        weather = data.get("weather", [{}])
        return {
            "city": data.get("name"),
            "temp": main.get("temp"),
            "humidity": main.get("humidity"),
            "condition": (weather[0].get("description") if weather else None),
            "raw": data
        }
