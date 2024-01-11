# Auction_House
Analysis of WoW Auction House Prices

## Initial Findings and bumps on the road
- The API allows you to pull a list of 246 realms.
- The Auction data seems to have different columns.
- Auctions have different amounts of id's, but certain amounts repeat.

## Work Done
- Modifications to the initial API call :
  - added some "Progress" indicators ( cosmetic ),
  - added a cycle to pull for different realms,
  - temporarily changed to create a file for each realm to figure out the different data in different columns,
  - added instruction to rearrange the columns in a specific order,
- The Auction data so far has the same columns, but not always in the same order

## Redirection
- Michael has been downloading information from the commodities API since Dec 22 2023, this is supposed to have the information from all the realms
- by Jan 03, 2024 Michael had obtained 79.8 million records
- The API returned the following columns:
  - id,
  - quantity,
  - unit_price,
  - time_left,
  - item.id,
  - item.name,
  - item.class
  - datetime
- There was not much to clean ( depending on each one's point of view )

 ## Work Done
 - Changed "id" columns from int to str
 - Changed datetime from object to datetime64
 - For certain analysis paths date and time columns where added with information from datetime
 - Ran value_counts() and value_counts().plot() for most columns
 - Attempted to analyze auction duration and item amount by auction id. This was canceled after some attempts and calculating the estimated time with the current code (19M seconds to complete)
 
## Results Obtained ( What was learned from the data )
### "id" column : this column was used to determine the duration of the auctions
- by plotting the value_counts() results it is easy to see:
  - how only a few ( comparatively speaking ) lasted **50 hours** (319),
  - there is short slope before stabilizing again, this slope is for the 17,684 that lasted **49 hrs**,
  - this stable part of the graph is for the 468,105 that lasted **48 hrs**
  - the graph shows declining values and then stabilizing again for a bit at 24,12,2 and 1 hours
  - 43.64% of the auctions appeared 1-2 times, meaning they lasted 2 hours of less
### "quantity" column : 
  - 1678 different quantities where found ranging from 1 to 20,189,464
  - only 176,586 auction records had quantities above 100 units
  - **Sample checked the quantity in the longest lasting auctions and no change was recorded**
  - *Could try to do additional research by dividing the records by class and then by auction id*

### "unit_price" column : 
  - most of the items seem to be priced the same across all auctions
  - **66,443** different prices where found ranging from 100 to 99,999,999,900
  - 21,090 records showed a unit_price over 10,000,000
  - 27,309 records showed a unit_price between 2,000,000 and 10,000,000
  - the rest are priced bellow 2,000,000

### "datetimn" column : 
  - Plotting this column showed a hill like decreasing graph
  - Divided this datetime column into date and time columns
  - **date column**
    - a value_count() and plot of this column showed auction counts between 6.3M and 6.99M except for the first and last date the data was collected, this shows that on any given day there are 271,583 auctions live
  - **time column**
    - a value_count() and plot of this column showed auction counts per hour to be between 3.28M and 3.45M at 21 of the 24 hrs
    - between 16:41 and 17:41 pulls the count goes down to between 3M and 3.01M
    - at the 23:41 pull the count was 3.12M

### - "item.class" column: The game classifies the items by Item Classes these classes are:
  - Trade Goods
  - Consumables
  - Unknown
  - Miscellaneous
  - Gems
  - Glyphs
  - Armor
  - Recipes 
- After reviewing some of the items in the "Unknown" classification, it looks like it is a place holder for Unclassified Items.
- Trade Goods constitute 54.4% of the records pulled, Consumables constitute 24.1%. Adding these two we get to 78.5% of records pulled.
- *Could try to do additional research by dividing the records by class and then by auction id*

### - "time_left" column shows different values apparently based on the time left before the auction ends:
 - **SHORT** when ending **less than 3 hrs**
 - **MEDIUM** when ending in **3-4 hrs**
 - **LONG** when ending in **4-12 hrs**
 - **VERY-LONG** when ending in **12-50 hrs**
 - *Could do additional research on how many Auctions appear as MEDIUM to VERY-LONG and disappear before changing to SOON*
