import requests

class Application:
    def get_producer(self):
        # Mocking a producer context manager for this example
        class Producer:
            def __enter__(self):
                print("Entering producer context")
                return self
            
            def __exit__(self, exc_type, exc_val, exc_tb):
                print("Exiting producer context")
        
        return Producer()

def get_weather():
    """
    Fetches current weather data for a specific location.
    Returns:
        dict: JSON response from the weather API.
    """
    try:
        response = requests.get(
            'https://api.open-meteo.com/v1/forecast',
            params={
                'latitude': 51.5,
                'longitude': -0.11,
                'current_weather': True
            }
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def main():
    """
    Main function that initializes the application and fetches weather data.
    """
    app = Application()
    with app.get_producer() as producer:
        weather_data = get_weather()
        if weather_data:
            print("Weather data fetched successfully:")
            print(weather_data)
        else:
            print("Failed to fetch weather data.")

if __name__ == "__main__":
    main()
