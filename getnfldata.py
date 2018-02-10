from bs4 import BeautifulSoup as bs
import requests
import csv

filename = "idkwhatimdoing"

def openFile(file_name):
    string_data = open(file_name).read()
    string_list = string_data.split("\n")[1:]
    final_list = []

    for row in string_list:
        string_fields = row.split(",")
        int_fields = []
        for value in string_fields:
            int_fields.append(value)
        final_list.append(int_fields)
    return final_list

def ExportToCSV(data):
    ### Added a parameter to remove the newlines in the output file
    with open(filename, 'w', newline = '') as f:
        writer = csv.writer(f, delimiter=',')
        for row in data:
            # Writing to the csv column wise
            for column in row:
                writer.writerow(column)

combinedata = openFile("playercombinedata.csv")
filename = "playernfldata.csv"
#print(combinedata[0:10])

playernames = []

### Extracts players names from main combinedata to it's own list
### in order to conduct scraping/searches
for player in combinedata:
    while True:
        try:
            playernames.append(player[1])
            break
        except IndexError:
            break

#print(playernames) ### confirms list was created correctly


def getNFLData(data):
    playernfldata = []
    parsedHeader = []
    parsedStats = []
    headerText = []
    career_stats_list = []
    count = 0 ### for testing purposes // del to run all

    ### This loops through the football players that went to the combine
    ### and searches PFR for their page and saves it in the list
    for name in playernames:
        count += 1 ### this and the if/else statement need to be deleted to run full list
        if count < 15:
            #print(name)
            r = requests.get(f"https://www.pro-football-reference.com/search/search.fcgi?hint=&search={name}&pid=&idx=")
            print(f"requesting {name}'s page")
            #print(r)
            page_text = bs(r.content, 'html.parser')
            print("adding data to list")
            playernfldata.append(page_text)
        else:
            break

    ### while the page is loaded in this function it's time to scrape
    ### needs a try function because if there are multiple people with the
    ### same name or if they didn't play in the NFL it returns a generic
    ### search page which doesn't fit the format that BS is trying to scrape
    for page_text in playernfldata:
        try:   ### I'm sure there's a better way to do this ###
            ### This searches for the career HEADER data in the first field of the site
            ### which defaults to the players primary position or the POS
            ### they have the most stats for
            print("finding header data")
            thead = page_text.find('thead')
            headerdata = thead.tr.next_sibling.next_sibling

            ### Not sure this try statement is necessary as I'm not getting
            ### any errors for the career data below this... but I could
            ### be missing something in the page source, will need
            ### to dig deeper
            try:
                for row in headerdata:
                    cols = [ele.strip() for ele in row]
                    headerText.append([ele for ele in cols if ele])
            except TypeError:
                print("uh oh, type error")
                pass
            ### This searches for the career data (actual stats) in the first field of the site
            ### which defaults to the players primary position or the POS
            ### they have the most stats for
            print("finding career data")
            tfoot = page_text.find('tfoot')
            careerstats = tfoot.tr
            for row in careerstats:
                cols = [ele.strip() for ele in row]
                career_stats_list.append([ele for ele in cols if ele])



        ### This will run if the player wasn't found/lands on generic search page
        except AttributeError:
            print("haha") # have to have a sense of humor, AMIRITE?!
            pass

    print(parsedHeader)
    print(headerText)
    print(career_stats_list)

# def ExportToCSV(data):
#     ### Added a parameter to remove the newlines in the output file
#     with open(filename, 'w', newline = '') as f:
#         writer = csv.writer(f, delimiter=',')
#         for row in data:
#             # Writing to the csv column wise
#             for column in row:
#                 writer.writerow(column)

getNFLData(playernames)

### Having trouble with the CSV function at the moment.
