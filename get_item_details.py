# Get item names from wowhead.com and save them to item_names.json
# Based on this post: https://www.wowhead.com/forums/topic/wowhead-api-for-items-characters-etc-187530
# Calls the wowhead item page by id and scrapes the XML for the item name, saves all to item_names.json

import json
import requests
import os
import xml.etree.ElementTree as ET

def get_item_details(item_id):
    url = f"https://www.wowhead.com/item={item_id}&xml"
    print(f"Calling URL: {url}")  # Print each URL called
    response = requests.get(url)
    print(f"Fetching details for item ID {item_id}: Status Code {response.status_code}")  # Debugging output
    if response.status_code == 200:
        try:
            root = ET.fromstring(response.content)
            item_details = {}

            name_element = root.find('.//item/name')
            class_element = root.find('.//item/class')

            if name_element is not None and name_element.text:
                item_details['name'] = name_element.text.strip()
            if class_element is not None and class_element.text:
                item_details['class'] = class_element.text.strip()

            if item_details:
                return item_details
            else:
                print(f"No details found for item ID {item_id}")  # Debugging output
                return None
        except ET.ParseError as e:
            print(f"XML parsing error for item ID {item_id}: {e}")  # Debugging output
            return None
    else:
        print(f"Failed to fetch data for item ID {item_id}")  # Debugging output
        return None

def main():
    output_file = 'item_details.json'

    # Load unique item IDs
    try:
        with open('unique_item_ids.json', 'r') as file:
            data = json.load(file)
            unique_ids = data["unique_item_ids"]
    except Exception as e:
        print(f"Error reading unique_item_ids.json: {e}")
        return

    if not unique_ids:
        print("The unique_item_ids.json file is empty or not formatted correctly.")
        return

    # Check if item_details.json exists
    if os.path.exists(output_file):
        with open(output_file, 'r') as file:
            existing_details = json.load(file)
    else:
        existing_details = {}

    # Fetch details for new items
    for item_id in unique_ids:
        if item_id not in existing_details or not all(key in existing_details[item_id] for key in ['name', 'class']):
            details = get_item_details(item_id)
            if details:
                existing_details[item_id] = details

    # Save to item_details.json
    with open(output_file, 'w') as file:
        json.dump(existing_details, file, indent=4)
    print("Updated item_details.json successfully.")

if __name__ == "__main__":
    main()
