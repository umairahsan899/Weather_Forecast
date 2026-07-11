import requests
Api_Key="92f7e30a4fdcd99bb9b30822a4a3a164"

def get_data(place,forecast_days,kind):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid={Api_Key}"
    response=requests.get(url)
    data=response.json()
    filtered_data=data["list"]
    nr_values=8*forecast_days
    filtered_data=filtered_data[:nr_values]
    if kind=="Temperature":
        filtered_data=[dict["main"]["temp"] for dict in filtered_data]

    if kind=="Sky":
        filtered_data=[dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data
if __name__=="__main__":
    get_data()

