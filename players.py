from response import responsePlayer


class Players: # Creates a dictionary of the searched players
    dictOfPlayers = {}
    name = input("Enter Player name or last name: ")
    for data in responsePlayer(name):
        height = data.get('height_feet')
        height_inches = data.get('height_inches')
        firstName = data.get('first_name')
        lastName = data.get('last_name')
        weight = data.get('weight_pounds')
        dictOfPlayers.setdefault(firstName + " " + lastName, []).append(weight)
        if height_inches is not None:
            dictOfPlayers.setdefault(firstName + " " + lastName, []).append(height + (height_inches / 10))
        else:
            dictOfPlayers.setdefault(firstName + " " + lastName, []).append(height)


def displatDictPlayer(): # searching from class Player and display the tallest and the heaviest player
    max_height = 0
    max_weight = 0
    player = None
    player2 = None
    largest = 0
    largest2 = 0
    for value, key in Players.dictOfPlayers.items():
        if key[1] is not None:
            max_height = max(max_height, key[1])
            if max(max_height, key[1]) > largest:
                largest = max_height

                player = value
    for value, key in Players.dictOfPlayers.items():
        if key[0] is not None:
            max_weight = max(max_weight, key[0])
            if max(max_weight, key[0]) > largest2:
                largest2 = max_weight
                player2 = value
    if max_height > 0 or max_weight > 0:
        height_to_str=str(max_height)
        split_height=height_to_str.split('.')
        feet=int(split_height[0])*30.48 # 1 feet = 30.48cm
        inch=int(split_height[1])*2.54 # 1 inch = 2.54cm
        converted_result=feet+inch
        print("The tallest player: " + player + " %.2f" % (converted_result / 100) + " meters")
        print("The heaviest player: " + player2 + " %.2f" % (max_weight * 0.45359237) + " kg") # 1 pound = 0.45359237 kg
    else:
        print("The heaviest player: Not found")
        print("The tallest player: Not found")


displatDictPlayer()
