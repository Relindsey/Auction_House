import os
import pandas as pd
import json
from datetime import datetime

json_file_count=0
files_to_add=[]
all_dataframes = []
csv_file_name = 'Auction_House/commodities_data.csv' # due to my setup
# csv_file_name = 'commodities_data.csv'
print("Opening csv file")                           # For presentation only
csv=pd.read_csv(csv_file_name)
csv['datetime']=pd.to_datetime(csv['datetime'])
last_date_in_csv=csv['datetime'].max().date()

print(os.getcwd())
folder_path='Auction_House/data'
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        if datetime.strptime(filename[17:27], '%m-%d-%Y').date()>last_date_in_csv: # only files with newer dates than the last in the csv
            files_to_add.append(filename)
            json_file_count+=1

print(f"{json_file_count} files to read/add")       # For presentation only
current_file=0
# for filename in os.listdir(folder_path):          # replaced this with the files in the list
for filename in files_to_add:
    current_file+=1
    file_path = os.path.join(folder_path, filename)

    # Load JSON data
    with open(file_path, 'r') as file:
        print(F"{datetime.datetime.now()} Loading file {current_file}/{json_file_count}")   # For presentation only
        data = json.load(file)

        # Convert JSON data to DataFrame
        if 'auctions' in data:
            df = pd.json_normalize(data, 'auctions')

                # Add the file_date as a new column
            df['datetime'] =pd.to_datetime(data['file_date'], format='%Y-%m-%d %H:%M')


            # Append this DataFrame to the csv
            df.to_csv(csv_file_name, mode='a',index=False,header=False)
            # all_dataframes.append(df)
            print(f"{datetime.datetime.now()} {len(df)} rows added \n")         # For presentation only

# No need to concat dataframes

# Combine all DataFrames into one
# final_dataframe = pd.concat(all_dataframes, ignore_index=True)

# final_dataframe['datetime'] = pd.to_datetime(final_dataframe['datetime'], format='%Y-%m-%d %H:%M')

# # Save as a CSV file
# csv_file_name = 'commodities_data.csv'
# final_dataframe.to_csv(csv_file_name, mode='a',index=False,header=False)
# print(f"Data saved to {csv_file_name}")