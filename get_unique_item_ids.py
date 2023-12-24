import json
import os

def process_json_files(folder_path):
    unique_item_ids = set()
    processed_files = set()

    # Check if './unique_item_ids.json' exists and load its contents if it does
    if os.path.exists('unique_item_ids.json'):
        with open('unique_item_ids.json', 'r') as file:
            previous_data = json.load(file)
            unique_item_ids = set(previous_data['unique_item_ids'])
            processed_files = set(previous_data['processed_files'])

    initial_unique_ids_count = len(unique_item_ids)
    files_processed = False  # Flag to check if any new file was processed

    print("Previously processed files:", processed_files)
    print("Files in the folder:")

    # Traverse through all files in the folder
    for filename in os.listdir(folder_path):
        print(filename)  # Print each filename in the folder
        if filename.endswith('.json') and filename not in processed_files:
            files_processed = True  # Mark that a new file is processed
            file_path = os.path.join(folder_path, filename)

            # Process each JSON file
            with open(file_path, 'r') as file:
                data = json.load(file)
                auctions = data.get('auctions', [])

                # Extract unique item IDs
                for auction in auctions:
                    item_id = auction.get('item', {}).get('id')
                    if item_id is not None:
                        unique_item_ids.add(item_id)

                # Add filename to processed files
                processed_files.add(filename)
        else:
            print(f"Skipping already processed file: {filename}")

    # Write to unique_item_ids.json
    output_data = {
        'unique_item_ids': list(unique_item_ids),
        'processed_files': list(processed_files)
    }
    with open('unique_item_ids.json', 'w') as output_file:
        json.dump(output_data, output_file, indent=4)

    # Print the number of new IDs found and the total number of unique item IDs
    new_ids_found = len(unique_item_ids) - initial_unique_ids_count
    total_unique_ids = len(unique_item_ids)
    print(f"New IDs found: {new_ids_found}")
    print(f"Total unique item IDs: {total_unique_ids}")

    # Print message if no new files were processed
    if not files_processed:
        print("All files in the data folder have been processed.")

    print("Data written to unique_item_ids.json")

# Replace 'data' with the path to your data folder
process_json_files('data')
