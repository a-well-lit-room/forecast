import requests

def main():
    response = requests.get('https://api.weather.gov/gridpoints/OKX/36,38/forecast')
    data = response.json()

    times = data['properties']['periods']

    # only look at the first four time periods
    for time in times[:4]:
        print(time['name'])
        print(f"{time['temperature']} degrees")
        print(time['detailedForecast'])
        print('')

if __name__ == '__main__':
    main()