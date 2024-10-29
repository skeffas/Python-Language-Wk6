import urllib.request
import json
from django.shortcuts import render

# Create your views here.

def index(requests):
    if request.method == 'POST': 
        city = request.POST['city']
        source = urllib.request.urlopen('ttp://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=03b4bd5c2ff89bb91a2eaf5d627179fb').read()
        
        list_of_data = json.loads(source)

        data = {
            "country_code" : list_of_data['sys']['country'],
                        "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)

