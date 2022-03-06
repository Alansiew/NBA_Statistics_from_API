import csv
import os
from collections import defaultdict
from response import *

# -----Dictionares------
visitorsPoints = {}
homePoints = {}
visitorsWon = {}
visitorsLose = {}
homeWon = {}
homeLose = {}
fieldnames = ['Team name', 'Won as a visitors', 'Won as a home', 'Lose as a visitors', 'Lose as a home'] # headers for csv file
listForSavingFile = defaultdict(list) # list for merge dictionaries
# ---------------------


def seasonStats(): # function get wanted data from api and create dictionaries with win, lose teams as a visitors and home teams
    season = input("Enter season year in YYYY format: ")
    print("\nWaiting...")
    response_API = requests.get(
        'https://www.balldontlie.io/api/v1/games?seasons[]={}'.format(season) + '&per_page=100&page=1')
    python_data = json.loads(response_API.text)
    all_meta = python_data['meta'] # get from api metadata which is needed for get total pages
    total_pages = all_meta.get('total_pages') # get total pages from current season
    score = 0
    for page in range(1, total_pages):
        response_API = requests.get(
            'https://www.balldontlie.io/api/v1/games?seasons[]={}'.format(season) + '&per_page=100&page={}'.format(
                page))
        python_data = json.loads(response_API.text)
        all_data = python_data['data'] # get data from api from current season and current page

        for data in all_data: # loop get data from previous loop and set points for win and lose team as a visitors and hosts
            visitor_team = data.get('visitor_team').get('full_name')
            visitor_team_score = data.get('visitor_team_score')
            home_team = data.get('home_team').get('full_name')
            home_team_score = data.get('home_team_score')
            visitorsPoints.setdefault(visitor_team, []).append(visitor_team_score)
            homePoints.setdefault(home_team, []).append(home_team_score)
            visitorsWon.setdefault(visitor_team, score)
            homeWon.setdefault(home_team, score)
            visitorsLose.setdefault(visitor_team, score)
            homeLose.setdefault(home_team, score)

            if visitor_team_score > home_team_score:
                visitorsWon[visitor_team] += 1
            else:
                visitorsLose[visitor_team] += 1
            if home_team_score > visitor_team_score:
                homeWon[home_team] += 1
            else:
                homeLose[home_team] += 1


def displayStats():  # merge dictionaries in one list and show them
    for d in (visitorsWon, homeWon, visitorsLose, homeLose):
        for key, value in d.items():
            listForSavingFile[key].append(value)

    for key, value in listForSavingFile.items():
        the_row = [key]  # Create the initial row with just key
        the_row.extend(value)  # Add the values, one by one, to the row
        a = 0 # index of header list
        print("-----------------")
        for i in the_row:
            print(str(fieldnames[a] + " " + str(i)))
            a += 1


def saveFile(): # function save file in .csv format, if file exist it overwriting it
    with open('output.csv', 'w+', newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"')
        writer.writerow(fieldnames)  # Write columns header
        for key, value in listForSavingFile.items():
            the_row = [key]  # Create the initial row with just key
            the_row.extend(value)  # Add the values, one by one, to the row
            writer.writerow(the_row)  # Write the full row


seasonStats()
displayStats()
ask=input("You want to save file? Y/N ")
ask=ask.lower()
while True:
    if ask != "y":
        print("You chose to not save a file")
        second_ask = input("Press enter to exit script ")
        if not second_ask or second_ask:
            break
    if ask == "y":
        saveFile()
        print("The file is saved in: "+os.getcwd())
        break
