# Auction_House
Analysis of WoW Auction House Prices

## Initial Findings and bumps on the road
- The API allows to pull a list of 246 realms.
- Not all realms return Auction data, only 71 on Jan1-3.
- The Auction data seems to have different columns.
- Auctions have different amount of id's, but certain amounts repeat.

## Work Done
- Modifications to the initial API call :
  - added some "Progress" indicators ( cosmetic ),
  - added a cycle to pull for different realms,
  - temporarily changed to create a file for each realm to figure out the different data in different columns,
  - added instruction to re-arrange the columns in a specific order,
- 
- The Auction data so far has the same columns, but not always in the same order
