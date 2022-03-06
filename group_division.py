
from response import responseTeam



class Teams: # create dictionary and categorizes teams into divisions
    dictOfTeams = {}
    for data in responseTeam():
        id = data.get('id')
        name = data.get('full_name')
        abbreviation = data.get('abbreviation')
        division = data.get('division')
        dictOfTeams.setdefault(division, []).append(name + " (" + abbreviation + ")")


def displayDictTeams(): # display teams from created dictionary
    for value, key in Teams.dictOfTeams.items():
        print(value, "\n", str(key).replace("[", "").replace("]", "").replace("'", ""), "\n")


displayDictTeams()
