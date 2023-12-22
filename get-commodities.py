import pandas as pd
import requests
import os

CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

response = requests.post('https://oauth.battle.net/token',
                         auth=(CLIENT_ID, CLIENT_SECRET),
                         data={'grant_type': 'client_credentials'})
if response.status_code == 200:
    access_token = response.json()['access_token']
else:
    print('Failed to retreive access token')
    print("status code:", response.status_code)
    print('Response:', response.text)

namespace = "dynamic-us"  # Adjust as necessary
locale = "en_US"  # Locale can be adjusted as needed

headers = {
    'Authorization': f'Bearer {access_token}',
    'Battlenet-Namespace': namespace,
    'locale': locale
}

params = {
    'namespace': namespace,
    'locale': locale
}

# Commodities

api_url = f'https://us.api.blizzard.com/data/wow/auctions/commodities'


# Making the GET request
response = requests.get(api_url, headers=headers, params=params)

# Checking the response
if response.status_code == 200:
    data = response.json()
    df = pd.json_normalize(data, record_path=['auctions'])

    # Save DataFrame to CSV
    df.to_csv('./commodities_data_12_21.csv', index=False)
    print("Data saved to 'commodities_data_12_21.csv'")

else:
    print('Failed to retrieve auction data')
    print("Status Code:", response.status_code)
    print('Response:', response.text)
