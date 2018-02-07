from bs4 import BeautifulSoup as bs
import requests
import re
import csv

url_list = [
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=1987&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=1988&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=1989&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=1990&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=1991&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=1992&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=1993&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=1994&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=1995&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=1996&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=1997&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=1998&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=1999&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=2000&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=2001&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=2002&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=2003&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=2004&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=2005&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=2006&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=2007&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=2008&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=2009&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=2010&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=2011&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=2012&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=2013&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=2014&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=2015&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=2016&pos=&college=",
"http://nflcombineresults.com/nflcombinedata_expanded.php?year=2017&pos=&college="
]

#r = requests.get(url_list[0])

filename = "playerdata2.csv"

def openURL(input_list):
# Added a list to store the data from different pages
    new_list = []
    for url in input_list:
        r = requests.get(url)
        page_text = bs(r.content, 'html.parser')
        # Appending the data to this list
        new_list.append(page_text)
    # print(new_list)
    return new_list

def getPlayerData(soup):
# This function identifies the wanted table within the given and passed webpage from function openPage()
# After identification with beautiful soup, it will loads the table into the multidim. list data[]
    table = soup.find('table')
    table_body = table.find('tbody')

    data = []
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    for row in data:
        for elem in row:
            return data

def ExportToCSV(data):
    # Added a parameter to remove the newlines in the output file
    with open(filename, 'w', newline = '') as f:
        writer = csv.writer(f, delimiter=',')
        for row in data:
            # Writing to the csv column wise
            for column in row:
                writer.writerow(column)
        # writer.writerows(data)
    print('Player Data data variable has been saved to file', filename)

soup = openURL(url_list)
# List to store the data from multiple pages
multi_pages = []
# For the list items in the list
for li in soup:
    player_data = getPlayerData(li)
    multi_pages.append(player_data)
ExportToCSV(multi_pages)
# ExportToCSV(player_data)
