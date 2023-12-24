# Get item names from wowhead.com and save them to item_names.json
# Based on this post: https://www.wowhead.com/forums/topic/wowhead-api-for-items-characters-etc-187530
# Calls the wowhead item page by id and scrapes the XML for the item name, saves all to item_details.json

import json
import requests
import os
import xml.etree.ElementTree as ET

def get_item_details(item_id):
    url = f"https://www.wowhead.com/item={item_id}&xml"
    response = requests.get(url)
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

            return item_details if item_details else None
        except ET.ParseError:
            return None
    else:
        return None

def main():
    output_file = 'item_details.json'

    # Load unique item IDs
    with open('unique_item_ids.json', 'r') as file:
        unique_ids = json.load(file)["unique_item_ids"]

    # Load existing item details
    if os.path.exists(output_file):
        with open(output_file, 'r') as file:
            existing_details = json.load(file)
    else:
        existing_details = {}

    # Counters for missing data
    missing_name = missing_class = missing_both = 0
    for item_id in unique_ids:
        item = existing_details.get(str(item_id), {})
        if 'name' not in item or not item['name']:
            missing_name += 1
        if 'class' not in item or not item['class']:
            missing_class += 1
        if ('name' not in item or not item['name']) and ('class' not in item or not item['class']):
            missing_both += 1

    print(f"Items missing name: {missing_name}")
    print(f"Items missing class: {missing_class}")
    print(f"Items missing both: {missing_both}")

    # Fetch details for new items
    api_calls = 0
    for item_id in unique_ids:
        if str(item_id) not in existing_details or not all(key in existing_details[str(item_id)] for key in ['name', 'class']):
            api_calls += 1

    print(f"Total API calls to make: {api_calls}")
    for item_id in unique_ids:
        if str(item_id) not in existing_details or not all(key in existing_details[str(item_id)] for key in ['name', 'class']):
            print(f"Adding {item_id}")
            details = get_item_details(item_id)
            if details:
                existing_details[str(item_id)] = details
            api_calls -= 1
            print(f"API calls remaining: {api_calls}")
        else:
            print(f"Skipping {item_id}")

    # Save to item_details.json
    with open(output_file, 'w') as file:
        json.dump(existing_details, file, indent=4)

    print("Updated item_details.json successfully.")

if __name__ == "__main__":
    main()
