import requests


def get_temperature_forecast(forecast_days, latitude, longitude):
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&forecast_days={forecast_days}"
    # Send the API request
    response = requests.get(api_url)
    # Process the response
    if response.status_code == 200:
        data = response.json()
        if "hourly" in data and "temperature_2m" in data["hourly"]:
            temperature_data = data["hourly"]["temperature_2m"]
            # Extract the temperature forecast for the last date
            last_date_temperatures = temperature_data[-24:]
            temperature = last_date_temperatures[-1]
            return temperature
        else:
            return None
    else:
        print("API request failed with status code:", response.status_code)
        return None


def geocode_location(address):
    api_url = "http://api.positionstack.com/v1/forward"
    access_key = "1db69d9dca8eec0e7f916c78f7bc0f65"
    # Define the parameters for your API request
    params = {
        "access_key": access_key,
        "query": address,
    }
    # Send the API request
    response = requests.get(api_url, params=params)
    # Process the response
    if response.status_code == 200:
        data = response.json()
        if data["data"]:
            # Extract the latitude and longitude from the response
            latitude = data["data"][0]["latitude"]
            longitude = data["data"][0]["longitude"]
            return latitude, longitude
        else:
            print("No results found.")
    else:
        print("API request failed with status code:", response.status_code)
    return None, None


# Example usage
query = "1600 Pennsylvania Ave NW, Washington DC"
latitude, longitude = geocode_location(query)
if latitude and longitude:
    print(f"Latitude: {latitude}, Longitude: {longitude}")

# Example usage
forecast_days = 1  # Specify the number of days to forecast (1 for the last date)
latitude = 52.52  # Specify the latitude
longitude = 13.41  # Specify the longitude
temperature = get_temperature_forecast(forecast_days, latitude, longitude)
if temperature:
    print(f"Temperature: {temperature}°C")
else:
    print("No results found.")
