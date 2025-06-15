import requests #used to make HTTP(S) requests

import json 

url = "https://itunes.apple.com/search?term=Taylor+Swift&media=music&entity=song" #if there are spaces use a plus sign

response = requests.get(url)
print("status code:", response.status_code,". ","For additional information on this code, see mozilla docs" )

if response.status_code == 200:
    json_object = json.loads(response.text) 
    print(json_object)
    results_array = json_object["results"]
    
    for result in results_array: #why is this indented here?
        name = result['trackName']
        print("Song Title:", name)
         #try to extract song length in seconds
        length_in_milli = result["trackTimeMillis"]
        length_in_sec = length_in_milli/60
        length_in_sec = round(length_in_sec, 2)
        # print("length in seconds:", length_in_sec)
        length_in_min = length_in_milli / 60000
        length_in_min = round(length_in_min, 2)  # Round to two decimal places
        print("Length in minutes:", length_in_min)



## now working with api heroku app

