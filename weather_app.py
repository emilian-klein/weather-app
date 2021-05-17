from tkinter import *
import requests, json
from tkinter import messagebox
from show_on_map import *

apiKey = '798ea5349c16c22a7abe55d8626bd50c'
apiUrl = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
degree_sign = u"\N{DEGREE SIGN}"
font = 'Bahnschrift'
label_border = 5 

#clearing entry widget when pressed with left mouse button
def clearEntry(event):
    cityEntry.delete(0, 'end')

#getting data from openweathermap api 
def getData(city):
    try:
        api_request = requests.get(apiUrl.format(city, apiKey))
        api = json.loads(api_request.content)
        longitude = api['coord']['lon'] 
        latitude = api['coord']['lat']
        temperature = api['main']['temp']
        pressure = api['main']['pressure']
        humidity = api['main']['humidity']
        weather_data = [longitude, latitude, temperature, pressure, humidity]
        return weather_data
    except Exception as e:
        api = 'No data found'
        return api

#getting city name from user and updating labels text based on recived data
def checkWeather():
    city = sv_cityEntry.get()
    weather = getData(city)
    if(weather != 'No data found'):
        cityLabel['text'] = 'Location: ' + city.title()
        longitudeLabel['text'] = 'Longitude: ' + str(weather[0])
        latitudeLabel['text'] = 'Latitude: ' + str(weather[1])
        temperatureLabel['text'] = 'Temperature: ' + str(weather[2]) + ' ' + degree_sign + 'C' 
        pressureLabel['text'] = 'Pressure: ' + str(weather[3]) + ' hPa'
        humidityLabel['text'] = 'Humidity: ' + str(weather[4]) + ' %'
        sv_cityEntry.set('Search for...')
        cityEntry.icursor(13)
    else:
        messagebox.showwarning('Error', "Cannot find weather for this location!")

#setting up application window
root = Tk()
root.title('Weather App')
root.iconbitmap('weather_app_icon.ico')
root.geometry('400x320+800+200')
root.resizable(False, False)

#label widgets
cityLabel = Label(root, text='Location: ', font=font, bd=label_border, bg='#3092d9')
longitudeLabel = Label(root, text='Longitude: ', font=font, bd=label_border)
latitudeLabel = Label(root, text='Latitude: ', font=font, bd=label_border)
temperatureLabel = Label(root, text='Temperature: ', font=font, bd=label_border)
pressureLabel = Label(root, text='Pressure: ',  font=font, bd=label_border)
humidityLabel = Label(root, text='Humidity: ', font=font, bd=label_border)

#entry widget
sv_cityEntry = StringVar()
sv_cityEntry.set('Search for...')
cityEntry = Entry(root, textvariable=sv_cityEntry, font=font)
cityEntry.bind("<Button-1>", clearEntry)

#buttons
searchButton = Button(root, text='Check weather', command=checkWeather, font=font, relief=GROOVE, width=20, bg='#3092d9')
mapButton = Button(root, text='See location on the map', command=lambda: showOnMap(longitudeLabel, latitudeLabel), font=font, relief=GROOVE, width=20, bg='#3092d9')

#placing widgets in application window
cityLabel.pack(fill='x')
longitudeLabel.pack(fill='x')
latitudeLabel.pack(fill='x')
temperatureLabel.pack(fill='x')
pressureLabel.pack(fill='x')
humidityLabel.pack(fill='x')
cityEntry.pack(pady=3)
searchButton.pack(pady=5)
mapButton.pack(pady=5)

root.mainloop()