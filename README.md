# Auction_House
Analysis of WoW Auction House Prices



get new data steps:
terminal: aws s3 sync s3://{bucket-name} ./raw-data
run: add_timestamp_and_details.py
check with: data_to_df_example.ipynb
run: get_unique_item_ids.py