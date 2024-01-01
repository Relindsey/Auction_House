# Auction_House
Analysis of WoW Auction House Prices

The files in data each represent hourly data from the WoW API. Run through 
process_all_to_csv.ipynb to combine the JSON files and create a new CSV
with all data for analysis and visualization. Please make sure to follow warning
in the first cell about adding the soon to be generated filename to your
.gitignore before running it the first time. The generated file is too large to
push to Github and forgetting to include the name in the gitignore before the file 
is generated is no fun.

The shape of the data in the data folder:

```
{
    "file_date": "2023-12-28 18:41",
    "auctions": [
        {
            "id": 1900316080,
            "item": {
                "id": 124107,
                "name": "Cursed Queenfish",
                "class": "Trade Goods"
            },
            "quantity": 16,
            "unit_price": 7400,
            "time_left": "SHORT"
        },
        {
            "id": 1900316101,
            "item": {
                "id": 130179,
                "name": "Eye of Prophecy",
                "class": "Trade Goods"
            },
            "quantity": 11,
            "unit_price": 79900,
            "time_left": "SHORT"
        },
    ]
}

Converting the csv to a dataframe, and then running: 
'df['datetime'] = pd.to_datetime(df['datetime'])' 
will give you this to work with:

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 40691536 entries, 0 to 40691535
Data columns (total 8 columns):
 #   Column      Dtype         
---  ------      -----         
 0   id          int64         
 1   quantity    int64         
 2   unit_price  int64         
 3   time_left   object        
 4   item.id     int64         
 5   item.name   object        
 6   item.class  object        
 7   datetime    datetime64[ns]
dtypes: datetime64[ns](1), int64(4), object(3)
memory usage: 2.4+ GB

```
```
As of 1/1 update:
Total rows: 66,131,836
Rows missing name: 4,691
Rows missing class: 6,156,711
Rows missing both name and class: 4,691
```

If anyone finds any issues with the data please let me know!
