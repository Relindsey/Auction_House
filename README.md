# Blizzard API Project
This project utilized the Blizzard Commodities Auction House API. My branch focused on creating visualizations that would aid a new or returning World of Warcraft player in selecting a profession for their character. 
# Code Source
I created a script to access the Blizzard Commodities Auction House and store data to a CSV file. Due to the size of the initial CSV files, I had to clean the data and narrow the scope to the profession items that were used for the visualization. Code for correlating the item ids to the item name was provided by team member Michael. I used VSC copilot and Google Colab's AI Assistant to help with errors and suggest fixes to code.
# Question
Which profession should a new or returning World of Warcraft player select for efficiency and profitability?
# Method
I identified an end-game profession commodity for each in-game profession and compared their market share (quantity) with the average auction sale price of each item.
The goal is to identify the profession with the most easily collected (grinded) consumable item with the best profit ratio. This identified the profession that is the easiest to play with the highest return on time invested.

I then ran a forecast with Prophet to provide a prospective outlook for the next thirty days.
# Results
Tailoring was identified as the current best profession for a new or returning World of Warcraft player to select. However, the forecast created by prophet showed that Enchanting would exhibit a strong upward value trend and overtake Tailoring to become the most profitable profession within the next thirty days.
# Use and License
This project was conducted in compliance with Blizzard Activision's Terms of Use.

The data retreived from the commodities auction house was used solely for an educational project to demonstrate an understanding of APIs and data analysis. 

No financial gain was received or solicited. 

The data and API access key were safeguarded.

No personal information was collected or stored for the project.

The code and data found in this repository is not intended for commercial activity. All data collected from the Blizzard Activision API is the intellectual property of Blizzard Activision. The code found within this repository is accessed "As Is" You shall not collect, use, store or disclose any player’s personal information or data in any manner that violates applicable laws, rules or regulations. If You do collect, use or store any player’s personal information, You must inform them of such use and that it is subject to Your privacy policy; (iii) You shall not collect, store or otherwise intercept a player’s Blizzard password; and (iv) You will strictly abide by Your privacy policy in handling the Data.

# Indemnity
Any persons or entities who use the code or data from this repository must adhere to the Terms and Use of Blizzard Activision's API access, found [here](https://www.blizzard.com/en-us/legal/a2989b50-5f16-43b1-abec-2ae17cc09dd6/blizzard-developer-api-terms-of-use). By accessing or using the code or data found within this repository, you expressly indemnify and hold harmless the creators of this repository for any damages resulting from its use or misuse. The code and data found within this repository shall not be used for financial gain or to undermine Blizzard Activision products or services.
