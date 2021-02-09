# Michael Koerwer

import requests
import matplotlib.pyplot as plt

def getURLdata(url,options=''):
    try:
        response = requests.get(url,options)
        if response.status_code != 200:
            raise
        data = response.json()
        return data
    except:
        print("API call was not successful.")
        return None

# global variables
apiKey = 'c284367c1c672382b28916233cda16b5'
alphaURL = 'http://api.openweathermap.org/data/2.5/weather'
betaURL = 'http://api.openweathermap.org/data/2.5/forecast'

# gather zip code from user and create options
while True:
    zipCode = input('Enter zip code: ')
    if 9999< int(zipCode) < 100000:
        break
    else:
        print("Invalid zip code.")
opts = {'zip':zipCode, 'units':'imperial', "appid":apiKey}

cityWeatherData = getURLdata(alphaURL, opts)

if cityWeatherData != None:
# display current weather data
    description = cityWeatherData['weather'][0]['description']
    cityName = cityWeatherData['name']
    temperature = cityWeatherData['main']['temp']
    print("Weather description in ", cityName, ": ", description, ".  Temperature is ", temperature, " degrees Fahrenheit.", sep ="")

    futureWeatherData = getURLdata(betaURL, opts).get('list')

    threeHour=[]
    mainTemp=[]

    for increment in futureWeatherData:
        threeHour.append(increment['dt_txt'])
        mainTemp.append(increment['main']['temp'])

#graph temperatures for next 5 days
    plt.plot(threeHour, mainTemp)
    plt.xlabel("Time")
    plt.ylabel("Degrees Fahrenheit")
    plt.xticks([threeHour[0], threeHour[len(threeHour)//2], threeHour[-1]])
    plt.show()
else:
    print("Invalid zip code.")