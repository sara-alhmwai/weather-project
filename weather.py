import requests
import json
try:
    params={'latitude':35,'longitude':38,'current':'temperature_2m,wind_speed_10m'}
    r= requests.get('https://api.open-meteo.com/v1/forecast', params=params,timeout=4)
    r.raise_for_status()
    data= r.json()
    weather={
            "temperature":data['current']['temperature_2m'],
            'wind_speed':data['current']['wind_speed_10m']
            }

    with open('weather.json','w') as f: 
        json.dump(weather,f, indent=2)

        
except(requests.exceptions.Timeout):
    print('The requests timed out, the server did notrespond in time')
except(requests.exceptions.ConnectionError):
    print('No internet connection , please check your network')
except(requests.exceptions.HTTPError):
    print('The server returned an error')        

 