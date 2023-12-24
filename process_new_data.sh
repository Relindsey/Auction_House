#!/bin/bash

# Load environment variables from .env file
if [ -f .env ]; then
    while IFS='' read -r line || [[ -n "$line" ]]; do
        # Skip empty lines and lines starting with #
        if [[ -z $line || $line == \#* ]]; then
            continue
        fi

        # Use '=' as a delimiter and read key/value pairs
        IFS='=' read -r key value <<< "$line"

        # Trim leading and trailing whitespace from key and value
        key=$(echo $key | xargs)
        value=$(echo $value | xargs)

        # Remove leading and trailing quotes from value
        value="${value%\"}"
        value="${value#\"}"

        # Export the variable
        if [[ ! -z $key ]]; then
            export "$key=$value"
        fi
    done < .env
fi

# Check if BUCKET_NAME is set
if [ -z "$BUCKET_NAME" ]; then
    echo "BUCKET_NAME is not set. Please check your .env file."
    exit 1
fi

# Sync data from S3 bucket and capture the output
echo "Syncing data from S3 bucket..."
sync_output=$(aws s3 sync s3://$BUCKET_NAME ./raw-data)

# Check if new files were downloaded
if [[ $sync_output == *"download"* ]]; then
    echo "New data found. Proceeding with processing..."

    # Run Python scripts
    echo "Running get_unique_item_ids.py..."
    python get_unique_item_ids.py

    echo "Running get_item_details.py..."
    python get_item_details.py

    echo "Running add_timestamp_and_details.py..."
    python add_timestamp_and_details.py

    # Run Jupyter notebook
    echo "Merging files to create commodities_data.csv..."
    jupyter nbconvert --to notebook --execute process_all_to_csv.ipynb
else
    echo "There is no new data on S3."
    exit 0
fi
