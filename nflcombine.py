from bs4 import BeautifulSoup as bs
import requests
import re
import csv

url_list = []

### Can choose which years you want to scrape for
### Add one year to end (ex: range(1987-1990) will search 1987, 88, and 89)
for num in range(1987, 2018):
    url_list.append(f"http://nflcombineresults.com/nflcombinedata_expanded.php?year={num}&pos=&college=")

print(url_list)

filename = "playercombinedata.csv"

def openURL(input_list):
### Added a list to store the data from different pages
    new_list = []

    for url in input_list:
        r = requests.get(url)
        page_text = bs(r.content, 'html.parser')
        new_list.append(page_text)
    return new_list

def getHeaderData(soup):
### This function identifies the wanted table within the given and passed webpage from function openURL()
### After identification with beautifulsoup, it will load the table into the multidim. list data[]
    table = soup.find('table')
    table_header = table.find('thead')

    data = []

    rows = table_header.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols])

    for row in data:
        for elem in row:
            return data

def getPlayerData(soup):
### This function identifies the wanted table within the given and passed webpage from function openURL()
### After identification with beautifulsoup, it will load the table into the multidim. list data[]
    table = soup.find('table')
    table_body = table.find('tbody')

    data = []

    rows = table_body.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols])

    for row in data:
        for elem in row:
            return data

def ExportToCSV(data):
    ### Added a parameter to remove the newlines in the output file
    with open(filename, 'w', newline = '') as f:
        writer = csv.writer(f, delimiter=',')
        for row in data:
            # Writing to the csv column wise
            for column in row:
                writer.writerow(column)

soup = openURL(url_list)

### List to store the data from multiple pages
multi_pages = []

### For the list items in the list
### ExportToCSV

### This gets the header data only once
get_header_data = 0
for li in soup:
    get_header_data = get_header_data + 1
    if get_header_data == 1:
        header_data = getHeaderData(li)
        multi_pages.append(header_data)
    else:
        break

ExportToCSV(multi_pages)

### This gets the players and their data
for li in soup:
    player_data = getPlayerData(li)
    multi_pages.append(player_data)
ExportToCSV(multi_pages)
