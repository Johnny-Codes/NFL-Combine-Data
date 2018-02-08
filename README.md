# NFL-Combine-Data
Scraping NFL Combine data and writing a CSV file. Come join the small but growing Python Scraping Discord channel.

# Updates:
8 Feb 18: Now that this script is complete and the data is scraped correctly the next phase is to gather more data on these players. Data of interest is what number a player was drafted and NFL production. It would be nice to be able to gather this data and append it to the same CSV file created by the combine script.

7 Feb 18: Initial post

# Goal
The goal of this project is to scrape all available data for NFL Combine participants from www.nflcombineresults.com and export the data into a CSV file. The purpose of the project is to gain basic knowledge and skills utilizing Python and supporting Modules, namely BeautifulSoup. This project is part of the Python Scraping Discord channel.

# Objectives
Scrape all available NFL Combine data available from www.nflcombineresults.com. The data of interest is the expanded table to gather as much information of participants of the NFL Combine.

The data available:

<code>Year | Name | College | POS | Height | Weight | Hand Size | Arm Length | Wonderlic | 40 Yard | Bench Press | Vert Leap | Broad Jump | Shuttle | 3Cone | 60Yd Shuttle</code>

# Future
Ideally, this information can be gathered and then with another script, gather NFL production data for each player for further data analysis. 

# Current Issues (8 Feb 18)
There are no current issues. The file allows to select ranges of years to scrape. It returns the header data and every player's data into one csv file for further data analysis. Thanks for all the help from the Python Scraping Discord channel. If you're interested in scraping and just starting, come join us. There are people of all experience levels that help out.

# Fixed Issues
[X] FIXED: the for loop containing each URL link only returns the last page of data (2017). The for loop goes through (verified with print()), however, the data for the previous pages are lost somewhere. (Thanks to @Maelstrom)

[X] FIXED: Pulls all the data and saves them in the CSV, however, if there is an empty cell on the site, it doesn't return an empty cell in the CSV, therefore, all the empty cells are at the end of each row instead of leaving an empty cell.

[X] FIXED: I'm sure there is a way to condense the url list since only the date in the URL is changed. (Thanks to @Maelstrom)

[X] FIXED: Not really an issue, however, between each row in the CSV file is a blank row, I would like to eventually remove it so that there are no blank rows. (Thanks to @Maelstrom)
