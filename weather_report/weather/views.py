from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    data = {}
    city = ""
    error_message = ""
    
    if request.method == 'POST':
        city = request.POST.get('city', '').strip()
        
        if not city:
            error_message = "Please enter a city name"
        else:
            try:
                api_key = '52526fd4c64e39df9b07c44e9de8bdd9'
                url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
                res = urllib.request.urlopen(url, timeout=5).read()
                json_data = json.loads(res)
                
                data = {
                    "city": city,
                    "country_code": str(json_data['sys']['country']),
                    "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
                    "temp": str(json_data['main']['temp']) + 'k',
                    "pressure": str(json_data['main']['pressure']), 
                    "humidity": str(json_data['main']['humidity']),
                    "description": str(json_data['weather'][0]['description']),
                }
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    error_message = f"City '{city}' not found. Please check the spelling."
                else:
                    error_message = f"API Error: {e.code} - Unable to fetch weather data"
            except urllib.error.URLError:
                error_message = "Network error: Unable to connect to weather service"
            except json.JSONDecodeError:
                error_message = "Error parsing weather data"
            except Exception as e:
                error_message = f"An error occurred: {str(e)}"
    
    context = {
        "data": data,
        "city": city,
        "error_message": error_message
    }
    
    return render(request, 'index.html', context)
