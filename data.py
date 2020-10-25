import requests
from pandas import json_normalize
import json
import csv

"""
# Initialize the dataframe
    col_names = ['id','type']
    activities = pd.DataFrame(columns=col_names)
    
    auth code: a1f8da7896c3909ce7ee0dd3933a425320f21598


    access_token = "access_token=a9751d7b269bcd1e4239bf64f35005f08537eb15" # replace with your access token here
    url = "https://www.strava.com/api/v3/athlete/activities"

    page = 1

    while True:
        
        # get page of activities from Strava
        r = requests.get(url + '?' + access_token + '&per_page=50' + '&page=' + str(page))
        r = r.json()
        print('data',r)
        # if no results then exit loop
        if (not r):
            break
        
        # otherwise add new data to dataframe
        for x in range(len(r)):
            activities.loc[x + (page-1)*50,'id'] = r[x]['id']
            activities.loc[x + (page-1)*50,'type'] = r[x]['type']

        # increment page
        page += 1

    print('done')

"""


# Get the tokens from file to connect to Strava
with open('strava_tokens.json') as json_file:
    strava_tokens = json.load(json_file)
# Loop through all activities
url = "https://www.strava.com/api/v3/activities"
access_token = strava_tokens['access_token']
# Get first page of activities from Strava with all fields
r = requests.get(url + '?access_token=' + access_token)
r = r.json()
    
df = json_normalize(r)
df.to_csv('strava_activities_all_fields.csv')