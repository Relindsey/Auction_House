# Auction_House
Analysis of WoW Auction House Prices

Fetch and process new data, run: ./process_new_data.sh

get new data steps:

terminal: aws s3 sync s3://{bucket-name} ./raw-data
run: get_unique_item_ids.py
run: get_item_details.py
run: add_timestamp_and_details.py
merge all files to create commodities_data.csv: process_all_to_csv.ipynb
