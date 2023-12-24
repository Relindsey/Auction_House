import json
import os
from datetime import datetime

def load_item_details(item_details_file):
    if os.path.exists(item_details_file):
        with open(item_details_file, 'r') as file:
            return json.load(file)
    else:
        print(f"Item details file {item_details_file} not found.")
        return {}

def process_files(raw_data_folder, processed_data_folder, item_details):
    for filename in os.listdir(raw_data_folder):
        if filename.endswith(".json"):
            processed_file_path = os.path.join(processed_data_folder, filename)
            if os.path.exists(processed_file_path):
                print(f"Skipping already processed file: {filename}")
                continue

            date_str = filename.replace('commodities_data_', '').replace('.json', '')
            date_obj = datetime.strptime(date_str, '%m-%d-%Y-%H%M')
            formatted_date_str = date_obj.strftime('%Y-%m-%d %H:%M')

            with open(os.path.join(raw_data_folder, filename), 'r') as file:
                data = json.load(file)

            if 'auctions' in data:
                auctions_data = data.pop('auctions')

                for auction in auctions_data:
                    item_id = str(auction.get('item', {}).get('id', ''))
                    item_details_for_id = item_details.get(item_id, {})

                    # Inserting 'name' and 'class' under 'item'
                    auction['item'].update({
                        'name': item_details_for_id.get('name', 'Unknown'),
                        'class': item_details_for_id.get('class', 'Unknown')
                    })

                new_data = {'file_date': formatted_date_str, 'auctions': auctions_data}
                new_data.update(data)
            else:
                new_data = {'file_date': formatted_date_str}

            new_filename = os.path.join(processed_data_folder, filename)
            with open(new_filename, 'w') as file:
                json.dump(new_data, file, indent=4)

# Folder paths
raw_data_folder = 'raw-data'
processed_data_folder = 'data'
item_details_file = 'item_details.json'

# Ensure the processed data folder exists
os.makedirs(processed_data_folder, exist_ok=True)

# Load item details
item_details = load_item_details(item_details_file)

# Process the files
process_files(raw_data_folder, processed_data_folder, item_details)
