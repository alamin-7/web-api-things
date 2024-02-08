import requests


api_url = 'http://parentNodeIP:19999/api/v1/alarms'

try:
    
    response = requests.get(api_url)

    print("response")

    
    if response.status_code == 200:
        print("sucessfull status code")
        
        alert_info = response.json()  # convert json or text
        print("Alert Information:", alert_info)
    else:
        
        print("Error:", response.status_code)
except Exception as e:
    # Print an error message if an exception occurs during the request
    print("An error occurred:", str(e))
