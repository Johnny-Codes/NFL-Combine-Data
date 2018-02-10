# NFL-Combine-Data
Scraping NFL Combine data and writing a CSV file. Come join the small but growing Python Scraping Discord channel.

# nflcombine.py
Completed; gathers all available NFL combine data.

# getnfldata.py
Initial commit 10 Feb 18; needs improvement. I encourage you to branch and work on it.

# Updates:
10 Feb 18: Uploaded getnfldata.py. This file creates a list of names of the player's that went to the combine. It searches www.pro-football-reference.com for their data. Quite a few issues at the moment. I'm creating this in a seperate file at the moment but the idea is to merge it with the nflcombine file in order to write all the header data together on the first row of the CSV. Note to self: split offense and defense players up because they pull different statistics which might mess with the CSV formatting? 

8 Feb 18: Now that this script is complete and the data is scraped correctly the next phase is to gather more data on these players. Data of interest is what number a player was drafted and NFL production. It would be nice to be able to gather this data and append it to the same CSV file created by the combine script.

7 Feb 18: Initial commit

# Goal
The goal of this project is to scrape all available data for NFL Combine participants from www.nflcombineresults.com and export the data into a CSV file. The purpose of the project is to gain basic knowledge and skills utilizing Python and supporting Modules, namely BeautifulSoup. This project is part of the Python Scraping Discord channel.

# Objectives
Scrape all available NFL Combine data available from www.nflcombineresults.com. The data of interest is the expanded table to gather as much information of participants of the NFL Combine.

The data available:

<code>Year | Name | College | POS | Height | Weight | Hand Size | Arm Length | Wonderlic | 40 Yard | Bench Press | Vert Leap | Broad Jump | Shuttle | 3Cone | 60Yd Shuttle</code>

Furthermore, scrape combine players NFL data, if it exists.

# Future
Fix getnfldata.py and merge with nflcombine.py to pull all combine and NFL statistics for combine participants 

Ideally, this information can be gathered and then with another script, gather NFL production data for each player for further data analysis. (updated with 10 Feb 18 commit)

# Current Issues (8 Feb 18)
[] (getnfldata.py) The try statements need refining.

[] (getnfldata.py) The write to CSV function needs to work so we can see what the data looks like in a CSV file to help inform writing decisions in other functions.

[] (getnfldata.py) How can this be merged to nflcombine.py to run at the same time and have all the data in one CSV?

# Fixed Issues
[X] FIXED: (nflcombine.py) the for loop containing each URL link only returns the last page of data (2017). The for loop goes through (verified with print()), however, the data for the previous pages are lost somewhere. (Thanks to @Maelstrom)

[X] FIXED: (nflcombine.py) Pulls all the data and saves them in the CSV, however, if there is an empty cell on the site, it doesn't return an empty cell in the CSV, therefore, all the empty cells are at the end of each row instead of leaving an empty cell.

[X] FIXED: (nflcombine.py) I'm sure there is a way to condense the url list since only the date in the URL is changed. (Thanks to @Maelstrom)

[X] FIXED: (nflcombine.py) Not really an issue, however, between each row in the CSV file is a blank row, I would like to eventually remove it so that there are no blank rows. (Thanks to @Maelstrom)
