# Auction_House
Analysis of WoW Auction House Prices

The files in data each represent hourly data from the WoW API. Run through 
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
```
Total rows: 27,099,172
Rows missing name: 2,036
Rows missing class: 2,691,130
Rows missing both name and class: 2,036
```

If anyone finds any issues with the data please let me know!
