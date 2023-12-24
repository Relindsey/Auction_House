# Auction_House
Analysis of WoW Auction House Prices

The files in data each represent one day of hourly data from the WoW API. Run through 
process_all_to_csv.ipynb to combine the JSON files and create a new CSV
with all data for analysis and visualization. Please make sure to follow warning
in the first cell about adding the soon to be generated filename to your
.gitignore before running it the first time. The generated file is too large to
push to Github and forgetting to include the name in the gitignore before the file 
is generated is no fun.

All of the data in the data folder looks like:

```
{
    "id": 1876585297,
    "item": {
        "id": 198196,
        "name": "Arclight Capacitor",
        "class": "Trade Goods"
        },
    "quantity": 1,
    "unit_price": 5250000,
    "time_left": "SHORT"
},
```

As of now there are 49 hours worth of data, supposedly consisting of:

```
Total items: 13,811,935
Items missing name: 7
Items missing class: 1,403,125
Items missing both name and class: 7
```

If anyone finds any issues with the data please let me know!