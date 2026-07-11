import requests

API_KEY = "92f7e30a4fdcd99bb9b30822a4a3a164"


def get_data(place, forecast_days):
    # Ensure /forecast endpoint is used
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    # Verify 'list' exists before accessing it
    if response.status_code != 200 or "list" not in data:
        error_msg = data.get("message", "Unknown API error")
        print(f"API Error ({response.status_code}): {error_msg}")
        return []

    # Extract forecast list and slice for requested number of days (8 readings per day)
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    return filtered_data[:nr_values]


if __name__ == "__main__":
    # Test run
    forecast = get_data("Tokyo", 1)
    print(f"Retrieved {len(forecast)} forecast items.")