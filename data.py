import pandas as pd

# Initialize the dataframe
col_names = ['id','type']
activities = pd.DataFrame(columns=col_names)

access_token = "access_token=20a880dd4cb02eea54565bf2e84618f9a034ec3e" # replace with your access token here
url = "https://www.strava.com/api/v3/activities"

print('done')

