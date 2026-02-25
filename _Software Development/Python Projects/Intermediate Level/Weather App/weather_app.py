import requests

def get_weather(city, api_key):
    """
    Fetches weather data for a given city using the OpenWeatherMap API.
    
    Parameters:
        city (str): The name of the city.
        api_key (str): Your API key for the OpenWeatherMap API.
    
    Returns:
        dict: Weather data in JSON format if successful, otherwise None.
    """
    # API URL with query parameters: city, API key, and units (metric for Celsius)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Error: {err}")
    
    return None

def display_weather(data):
    """
    Displays weather information extracted from the API response.
    
    Parameters:
        data (dict): The weather data returned by the API.
    """
    # Extract required data with default fallbacks if key is missing
    city = data.get("name", "Unknown location")
    sys_data = data.get("sys", {})
    country = sys_data.get("country", "")
    weather_list = data.get("weather", [])
    weather_description = weather_list[0]["description"] if weather_list else "No description available"
    main_data = data.get("main", {})
    temperature = main_data.get("temp", "N/A")
    humidity = main_data.get("humidity", "N/A")
    wind_data = data.get("wind", {})
    wind_speed = wind_data.get("speed", "N/A")
    
    print(f"\nWeather in {city}, {country}:")
    print(f"  Description: {weather_description.capitalize()}")
    print(f"  Temperature: {temperature}°C")
    print(f"  Humidity: {humidity}%")
    print(f"  Wind Speed: {wind_speed} m/s")

def main():
    print("Welcome to the Weather App!")
    
    # Replace this with your actual API key from OpenWeatherMap
    api_key = "<YOUR_API_KEY>"
    
    if api_key == "<YOUR_API_KEY>":
        print("Error: Please replace <YOUR_API_KEY> with your actual OpenWeatherMap API key.")
        return
    
    city = input("Enter the city name: ").strip()
    
    if not city:
        print("City name cannot be empty.")
        return
    
    weather_data = get_weather(city, api_key)
    if weather_data:
        display_weather(weather_data)
    else:
        print("Failed to retrieve weather data. Please check the city name or your API key.")

if __name__ == "__main__":
    main()
