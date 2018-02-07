# NFL-Combine-Data
Scraping NFL Combine data and writing a CSV file

# Goal
The goal of this project is to scrape all available data for NFL Combine participants from www.nflcombineresults.com and export the data into a CSV file. The purpose of the project is to gain basic knowledge and skills utilizing Python and supporting Modules, namely BeautifulSoup. This project is part of the Python Scraping Discord channel.

# Objectives
Scrape all available NFL Combine data available from www.nflcombineresults.com. The data of interest is the expanded table to gather as much information of participants of the NFL Combine.

The data available:

<code>Year | Name | College | POS | Height | Weight | Hand Size | Arm Length | Wonderlic | 40 Yard | Bench Press | Vert Leap | Broad Jump | Shuttle | 3Cone | 60Yd Shuttle</code>

# Future
Ideally, this information can be gathered and then with another script, gather NFL production data for each player for further data analysis.

# Current Issues (7 Feb 18)
[] the for loop containing each URL link only returns the last page of data (2017). The for loop goes through (verified with print()), however, the data for the previous pages are lost somewhere.

[] I'm sure there is a way to condense the url list since only the date in the URL is changed.

[] Not really an issue, however, between each row in the CSV file is a blank row, I would like to eventually remove it so that there are no blank rows.
