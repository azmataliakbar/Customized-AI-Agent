import requests

def get_weather(city):
    try:
        # Define the custom format for wttr.in
        # %l: location, %c: condition, %t: temperature, %f: feels like,
        # %S: sunrise, %s: sunset, %w: wind speed and direction.
        # \n creates a newline in the output for better readability.
        # The spaces around the newlines are for formatting clarity.
        custom_format = "%l: %c %t (feels like %f) \nSunrise: %S \nSunset: %s \nWind: %w"

        # Construct the URL with the custom format
        url = f"https://wttr.in/{city}?format={custom_format}"

        # Make the request to wttr.in
        res = requests.get(url)

        # Get the text content and strip any leading/trailing whitespace
        weather_info = res.text.strip()

        # Return the formatted weather information
        return f"AI Agent, Opening Weather Of {city.title()}...\n\n{weather_info}"

    except requests.exceptions.RequestException as e:
        # Catch specific request exceptions for network-related issues
        return f"Failed to connect to weather service. Please check your internet connection: {e}"
    except Exception as e:
        # Catch any other unexpected errors
        return f"An unexpected error occurred: {e}"

# You can add a simple example of how to use it here for testing:
if __name__ == "__main__":
    # Test with a city
    weather_report = get_weather("Tokyo")
    print(weather_report)

    # Test with another city
    weather_report_2 = get_weather("London")
    print("\n" + weather_report_2)

    # Test with a city that might not exist or a network issue
    weather_report_error = get_weather("NonExistentCity123")
    print("\n" + weather_report_error)

