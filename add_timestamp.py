import json
import os
from datetime import datetime

def process_files(raw_data_folder, processed_data_folder):
    for filename in os.listdir(raw_data_folder):
        if filename.endswith(".json"):
            # Check if file has already been processed
            processed_file_path = os.path.join(processed_data_folder, filename)
            if os.path.exists(processed_file_path):
                print(f"Skipping already processed file: {filename}")
                continue

            # Extract date from filename
            date_str = filename.replace('commodities_data_', '').replace('.json', '')

            # Convert the date string to a datetime object
            # Adjust the format to match 'MM-DD-YYYY-HHMM'
            date_obj = datetime.strptime(date_str, '%m-%d-%Y-%H%M')

            # Convert the datetime object to a string in your preferred format
            formatted_date_str = date_obj.strftime('%Y-%m-%d %H:%M')

            # Read the original JSON file
            with open(os.path.join(raw_data_folder, filename), 'r') as file:
                data = json.load(file)

            # Check if 'auctions' key exists
            if 'auctions' in data:
                auctions_data = data.pop('auctions')
                
                # Create a new dictionary with 'file_date' before 'auctions'
                new_data = {'file_date': formatted_date_str, 'auctions': auctions_data}
                
                # Add the rest of the original data
                new_data.update(data)
            else:
                new_data = {'file_date': formatted_date_str}

            # Write the modified data to a new file in the 'data' folder
            new_filename = os.path.join(processed_data_folder, filename)
            with open(new_filename, 'w') as file:
                json.dump(new_data, file, indent=4)

            # Uncomment to delete the original file
            # os.remove(os.path.join(raw_data_folder, filename))
            # print(f"Processed and moved: {filename}")

# Folder paths
raw_data_folder = 'raw-data'
processed_data_folder = 'data'

# Ensure the processed data folder exists
os.makedirs(processed_data_folder, exist_ok=True)

# Process the files
process_files(raw_data_folder, processed_data_folder)
