import requests
import json

api_url = 'http://13.208.128.137:19999/api/v2/alerts?options=summary,instances,values,minify&status=raised'

try:

    response = requests.get(api_url)

   # print("response", response)

    
    if response.status_code == 200:
        print("sucessfull status code")
        
        alert_info = response.json() # Convert JSON response to Python dictionary

        print(type(alert_info))

       # print("after alert got the response", alert_info)

        #data = alert_info

        print("After")

       # warning_entries = [entry for entry in alert_info if entry.get('st') == 'WARNING']

        print("after waring filtering")
       # for entry in warning_entries:
        #    print(entry)

        print("data printing")
        for data in alert_info:
            for key, value in data.items():
                print(key, value)

      #  print("Alert Information:", alert_info)
    else:
        # Print an error message if the request was not successful
        print("Error:", response.status_code)
except Exception as e:
    
    print("An error occurred:", str(e))

