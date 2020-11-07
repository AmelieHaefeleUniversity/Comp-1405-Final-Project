from random import *


# The d20 dice
def d20():
    return randint(0, 21)


def clear():
    print("\n" * 100)


def user_move_on():
    user_action = input()
    clear()


# Text stored here so code is less jumbled
# ASCII art of mountains
def scene1():
    print("_    .  ,   .           .\n    *  / \_ *  / \_      _  *        *   /\\'__        *\n      /    \  /    \, "
          "  ((        .    _/  /  \  *'.\n .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.\n    /    \/  \  _/  "
          "\-'\      *    /.' ^_   \_   .'\  *\n  /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \n /  `-.__ ^   "
          "/ .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-\n/        `.  / /       `.~-^=-=~=^=.-'      '-._ `._")
    print("\n ")
    return True


# ASCII art of the boss
def boss_fight_intro():
    print(",--,  ,.-.\n               ,                   \,       '-,-`,'-.' |\n               ,                   "
          "\,       '-,-`,'-.' | ._\n             /|           \    ,   |\         }  )/  / `-,',\n              [ ,  "
          "        |\  /|   | |        /  \|  |/`  ,`\n              | |       ,.`  `,` `, | |  _,...(   (      .',"
          "\n              \  \  __ ,-` `  ,  , `/ |,'      Y     (   /_L\\\n              \  \_\,``,   ` , ,  "
          "/  |         )         _,/\n               \  '  `  ,_ _`_,-,<._.<        /         /\n                 ', "
          "`>.,`  `  `   ,., |_      |         /\n                   \/`  `,   `   ,`  | /__,.-`    _,   `\\\n        "
          "       -,-..\  _  \  `  /  ,  / `._) _,-\`       \\\n                \_,,.) /\    ` /  / ) (-,, ``    ,    "
          "    |\n               ,` )  | \_\       '-`  |  `(               \\\n              /  /```(   , --, ,"
          "' \   |`<`    ,            |\n             /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)\n       ,-, ,"
          "`   `   (_,\ \    |   /) / __/  /   `----`\n      (-, \           ) \ ('_.-._)/ /,`    /\n      | /  `     "
          "     `/ \\\\ V   V, /`     /\n   ,--\(        ,     <_/`\\\\     ||      /\n  (   ,``-     \/|         "
          "\-A.A-`|     /\n ,>,_ )_,..(    )\          -,,_-`  _--`\n(_ \|`   _,/_  /  \_            ,--`\n \( `   "
          "<.,../`     `-.._   _,-`\n")


# Prints the Rules of combat
def rules():
    print("game rules go here")
    return True


# Intro text to the fight
def fight_one_intro():
    print("You encountered: \n Goblin 1 HP:10 LV: 1 \n Goblin 2 HP:15 LV:2 \n They don't look too difficult \n")

    print("Goblin 2: Hey! My name's Alastair and this is my friend Prescott I think we deserve to actually have our "
          "names said!\n"
          "")
    user_move_on()
    print("Uhhh ok \n You encountered: \n Alastair HP:10 LV: 1 \n Prescott HP:15 LV:2 \n \n Alastair: Thank you, "
          "now prepare to die! \n")

    return True


def add_to_file(string):
    fight_info_file = open("fight_info.txt", "a")
    fight_info_file.write(string)
    fight_info_file.close()


# Prints out how each team is doing at the beginning of each turn to help inform the player
def the_standings(goodGuys_team, badGuys_team):
    print("-" * 79 + "\n The Standings\n" + "-" * 79 + "\n")
    print("Your Team:")
    # Prints out each member on your team's, health and action points
    for key in goodGuys_team:
        print("\n" + str(key) + "\n HP:" + str(goodGuys_team[key]['health']) + "\nAP:" + str(
            goodGuys_team[key]['action_points']) + "\n")
    print("-" * 79 + "\n The Enemy Team\n" + "-" * 79)
    # Prints out each member on the enemy team's, health and action points
    for key in badGuys_team:
        print("\n" + str(key) + "\n HP:" + str(badGuys_team[key]['health']) + "\nAP:" + str(
            badGuys_team[key]['action_points']) + "\n")
    return True


def print_miss_action(name, action, roll, target):
    to_print = (name + " used their " + action + " and rolled a(n) " + str(roll) + " missing " + target)
    print(to_print)
    add_to_file(to_print)


def print_heal_action(name, action, roll, target, effect):
    to_print = (name + " used " + action + " and rolled a(n) " + str(
        roll) + " succeeding healing " + target + " for " + str(
        effect) + " health")
    print(to_print)
    add_to_file(to_print)


def print_harm_action(name, action, roll, target, effect):
    to_print = (name + " used their " + action + " and rolled a(n) " + str(
        roll) + " hitting " + target + " for " + str(
        effect) + " damage")
    print(to_print)
    add_to_file(to_print)


def print_rest(name):
    to_print = (name + " rested regaining 2 Action Points")
    print(to_print)
    add_to_file(to_print)


def print_person_down(name):
    to_print = (name + " has fallen and is unable to fight")
    print(to_print)
    add_to_file(to_print)


# Gets the action the user wants to preform, it also prints out the actions the player can do, what they do,
# and how many action points it costs
def user_action(goodGuys_team, pname):
    value_incorrect = True
    print("Player Turn!")
    # Prints out the users health and action points
    print("-" * 79 + "\n" + str(pname) + "  HP: " + str(goodGuys_team[pname]['health']) + " AP: " + str(
        goodGuys_team[pname]['action_points']) + "\n" + "-" * 79)
    # Prints out each action, what it does, and how many action points it costs
    for key, value in (goodGuys_team[pname]['inventory']).items():
        print(str(key.capitalize()) + ", " + str(
            (goodGuys_team[pname]['inventory'])[key]['explanation']) + ", Cost: " + str(
            (goodGuys_team[pname]['inventory'])[key]['ap_cost']) + " Action Point(s)" + "\n")
    # While the value is incorrect
    while value_incorrect:
        # Asks what action the user wants to do
        action = input("What would you like to do/use?\n")
        # Checks if they can preform that action
        for key, value in (goodGuys_team[pname]['inventory']).items():
            if action == str((goodGuys_team[pname]['inventory'])[key]['name']):
                # Returns the action
                return key.lower()
        # Prints out letting the user know they entered and incorrect value
        else:
            print("Please enter a proper value(ie enter 'heal', if you want to heal)")


def player_turn_outcome(goodGuys_team, badGuys_team, action, pname, experience_points):
    # If the player chooses a harmful attack they will target the enemy team
    if goodGuys_team[pname]["inventory"][action]["ap_cost"] > goodGuys_team[pname]['action_points']:
        print("Error you only have " + str(goodGuys_team[pname]['action_points']) + "action point(s) please heal or "
                                                                                    "chose an action that costs less")
        return -1

    if goodGuys_team[pname]["inventory"][action]['type'] == "damage":
        print("Who do you want to target?\n")
        # Printing out the name of each enemy
        for enemy_names in badGuys_team:
            print(enemy_names + "\n")
        # Capitalizing it in cause the player didn't
        target = (input("Enter your Target here:\n")).capitalize()
        # Removes the number of action points the attack costs
        goodGuys_team[pname]['action_points'] = goodGuys_team[pname]['action_points'] - \
                                                goodGuys_team[pname]["inventory"][action]["ap_cost"]
        # Rolling the dice
        roll = d20()
        # If it hits
        if roll >= 10:
            # The amount of damaged is removed from the targets health
            badGuys_team[target]["health"] = badGuys_team[target]["health"] - \
                                             goodGuys_team[pname]["inventory"][action][
                                                 'effect']
            # Add experience points for the hit
            experience_points = experience_points + 50
            # Print out what happened
            print_harm_action(pname, action, roll, target, goodGuys_team[pname]["inventory"][action][
                'effect'])
        # If it does not hit
        elif roll < 10:
            # Prints out what happened
            print_miss_action(pname, action, roll, target)

    # If the player chooses a helpful attack it will ask which person on their team to target
    if goodGuys_team[pname]["inventory"][action]['type'] == "help":
        # The player can only rest themselves and it will always been successful
        if action == "rest":
            goodGuys_team[pname]["action_points"] = goodGuys_team[pname]["action_points"] + \
                                                    goodGuys_team[pname]["inventory"][action]['effect']
            # Print out what happened
            print_rest(pname)
            return goodGuys_team, badGuys_team, action, pname
        # Printing out all players on their team
        print("Who do you want to target?\n")
        for ally_names in goodGuys_team:
            print(ally_names + "\n")
        # Get the targets name
        target = (input("Enter your Target here:\n")).capitalize()
        # Taking away the action point cost
        goodGuys_team[pname]['action_points'] = goodGuys_team[pname]['action_points'] - \
                                                goodGuys_team[pname]["inventory"][action]["ap_cost"]
        # Rolling the dice
        roll = d20()

        # if its a healing action
        if action == 'heal':
            # If it succeeds
            if roll >= 10:
                # Heals the target
                goodGuys_team[target]["health"] = goodGuys_team[target]["health"] + \
                                                  goodGuys_team[pname]["inventory"][action]['effect']
                # Add experience points for the hit
                experience_points = experience_points + 50
                # Print out what happens
                print_heal_action(pname, action, roll, target, goodGuys_team[pname]["inventory"][action][
                    'effect'])

            # If it fails
            if roll < 10:
                # Prints out what happened
                print_miss_action(pname, "heal", roll, target)
            # If it fails terribly
            if roll < 4:
                # Takes the heal away
                goodGuys_team[target]["health"] = goodGuys_team[target]["health"] - \
                                                  goodGuys_team[pname]["inventory"][action]['effect']
                to_print = (pname + " used " + action + " and rolled a(n) " + str(
                    roll) + " failing horribly " + target + " hurting them for " +
                            str(goodGuys_team[pname]["inventory"][action]['effect']) + " damage")
                print(to_print)
                add_to_file(to_print)

    return goodGuys_team, badGuys_team, action, pname, experience_points


def good_guys_NPC_turn(goodGuys_team, badGuys_team, pname, experience_points):
    # initializing variables
    highestHealth_NPC = ""
    highestHealth = 0
    # Checks which enemy has the highest health and saves it
    for key in badGuys_team:
        if badGuys_team[key]['health'] >= highestHealth:
            highestHealth_NPC = key
            highestHealth = badGuys_team[key]['health']

    # Checks if Danielle is still alive
    if goodGuys_team["Danielle"]['health'] <= 0:
        print_person_down("Danielle")
        # Danielle's battle AI
    else:
        # If Danielle has less than 2 AP points she will choose to rest
        if goodGuys_team["Danielle"]['action_points'] < 2:
            goodGuys_team["Danielle"]['action_points'] = goodGuys_team["Danielle"]['action_points'] + 2

        # If Danielle is above 4 ap then use their strongest attack to attack the bad guy NPC with the most health
        elif goodGuys_team["Danielle"]['action_points'] > 4:
            # Removes the number of action points it takes to use her bow
            goodGuys_team["Danielle"]['action_points'] = goodGuys_team["Danielle"]['action_points'] - 2
            # Rolling the dice
            roll = d20()
            # If her roll succeeds
            if roll >= 10:
                # Remove health from the enemy she targets for amount of damage she does (at her current level)
                badGuys_team[highestHealth_NPC]['health'] = badGuys_team[highestHealth_NPC]['health'] - (
                        3 + goodGuys_team["Danielle"]["level"])
                # Add experience points for the hit
                experience_points = experience_points + 50
                # Prints out what happens
                print_harm_action("Danielle", "bow", roll, highestHealth_NPC,
                                  3 + goodGuys_team["Danielle"]["level"])
            # If her roll fails
            elif roll < 10:
                # Prints out what happens
                print_miss_action("Danielle", "bow", roll, highestHealth_NPC)

        # If she is below 4 ap and less than or equal to 2 AP point she will attack the strongest enemy with her knife
        elif goodGuys_team["Danielle"]['action_points'] >= 2:
            #  Removes the number of action points it takes to use her knife
            goodGuys_team["Danielle"]['action_points'] = goodGuys_team["Danielle"]['action_points'] - 1
            # Rolling the dice
            roll = d20()
            # If her roll succeeds
            if roll >= 10:
                # Remove health from the enemy she targets for amount of damage she does (at her current level)
                badGuys_team[highestHealth_NPC]['health'] = badGuys_team[highestHealth_NPC]['health'] - (
                        1 + goodGuys_team["Danielle"]["level"])
                # Add experience points for the hit
                experience_points = experience_points + 50
                # Prints out what happens
                print_harm_action("Danielle", "knife", roll, highestHealth_NPC,
                                  1 + goodGuys_team["Danielle"]["level"])
            # If her roll fails
            elif roll < 10:
                # Prints out what happens
                print_miss_action("Danielle", "knife", roll, highestHealth_NPC)

    # Checks if Peter is still alive
    if goodGuys_team['Peter']['health'] <= 0:
        print_person_down("Peter")
    else:
        # Peter's battle AI
        lowestHealth_Ally = pname
        # If he has less than 4 action points he will chose to rest
        if goodGuys_team['Peter']['action_points'] < 4:
            goodGuys_team['Peter']['action_points'] = goodGuys_team['Peter']['action_points'] + 2
        # Checks if any of the members on his team are 10 health or below
        for key in goodGuys_team:
            # Checks if anyone needs to be healed
            if goodGuys_team[key]["health"] <= 10:
                # He heals the one with the lowest health and they get set to lowestHealth_Ally
                if goodGuys_team['Danielle']['health'] <= goodGuys_team[pname]['health']:
                    lowestHealth_Ally = goodGuys_team['Danielle']
                    if goodGuys_team['Peter']['health'] <= goodGuys_team['Danielle']['health']:
                        lowestHealth_Ally = goodGuys_team['Peter']

                goodGuys_team['Peter']['action_points'] = goodGuys_team['Peter']['action_points'] - 2

                # Rolls the dice
                roll = d20()
                # If it succeeds
                if roll >= 10:
                    # Heals the player the correct amount for his current level
                    goodGuys_team[lowestHealth_Ally]['health'] = goodGuys_team[lowestHealth_Ally]['health'] + (
                            2 + goodGuys_team['Peter']['level'])
                    # Prints out what happens
                    # Add experience points for the hit
                    experience_points = experience_points + 50
                    print_heal_action("Peter", "heal", roll, str(lowestHealth_Ally)
                                      ,
                                      2 + goodGuys_team['Peter']['level'])
                    # Returns  here so that he doesn't heal more than 1 person per turn
                    return goodGuys_team, badGuys_team, experience_points
                # If the roll fails
                elif roll < 10:
                    print_miss_action("Peter", "heal", roll, str(lowestHealth_Ally))
                    #  Returns  here so that he doesn't heal more than 1 person per turn
                    return goodGuys_team, badGuys_team, experience_points
                # He is too good to fail tremendously (I don't want him accidentally killing the player)
        else:
            goodGuys_team['Peter']['action_points'] = goodGuys_team['Peter']['action_points'] - 3
            roll = d20()
            if roll >= 10:
                # Add experience points for the hit
                experience_points = experience_points + 50
                badGuys_team[highestHealth_NPC]['health'] = badGuys_team[highestHealth_NPC]['health'] - (
                        4 + goodGuys_team["Peter"]["level"])
                print_harm_action("Peter", "fireball", roll, highestHealth_NPC,
                                  4 + goodGuys_team["Peter"]["level"])
                return goodGuys_team, badGuys_team, experience_points
            if roll < 10:
                print_miss_action("Peter", "fireball", roll, highestHealth_NPC)
    return goodGuys_team, badGuys_team, experience_points


def normal_bad_guys_turn(goodGuys_team, badGuys_team, special_event):
    # initializing variables
    lowestHealth_NPC = ""
    highestHealth = 0
    # checks which player on the good guys team has the lowest health and saves it
    for key in goodGuys_team:
        if goodGuys_team[key]['health'] >= highestHealth:
            lowestHealth_NPC = key
            highestHealth = goodGuys_team[key]['health']
    # Goes through each bad guy so they have a chance to attack
    for bad_guy in badGuys_team:
        if badGuys_team[bad_guy]['health'] <= 0:
            print_person_down(bad_guy)
        else:
            if special_event == 1:
                if badGuys_team['Alastair']['health'] <= 5:
                    print("Add text Alistair where puts on a right he believes to be the one Ring from The Hobbit and "
                          "gets annoyed when it doesn't work ")
            # If their action points are less than 2 they choose to rest
            if badGuys_team[bad_guy]["action_points"] <= 2:
                badGuys_team[bad_guy]['action_points'] = badGuys_team[bad_guy]['action_points'] + 2
                # Prints out what happens
                print_rest(bad_guy)
            # If their action points are above 2 they choose to attack
            elif badGuys_team[bad_guy]["action_points"] > 2:
                roll = d20()
                # If their roll succeeds
                if roll >= 10:
                    # calculates their damage based on their level
                    damage = badGuys_team[bad_guy]["level"] * 3
                    # removes the health from the target they attack
                    goodGuys_team[lowestHealth_NPC]['health'] = goodGuys_team[lowestHealth_NPC]['health'] - damage
                    # Prints out what happens
                    print_harm_action(bad_guy, "slashed", roll, lowestHealth_NPC, damage)
                # If their roll fails
                elif roll < 10:
                    # Prints out what happens
                    print_miss_action(bad_guy, "slashed", roll, lowestHealth_NPC)
    return goodGuys_team, badGuys_team


# The fight function that takes the people fighting as arguments
def fight(goodGuys_team, badGuys_team, pname, experience_points, special_event):
    keep_going = True
    number_dead = 0
    while keep_going:
        # Checks if the player has died
        if goodGuys_team[pname]['health'] == 0:
            return -1
        # Goes through each enemy in the list (regular indexing doesn't work cause dictionaries)

        # Currently not working rn
        for key in badGuys_team:
            # Adds 1 to the number of dead if the enemies health has reached 0
            if badGuys_team[key]['health'] <= 0:
                number_dead += 1
            # If all of the enemies are dead then the good guys have won and it returns true
            if number_dead == len(badGuys_team):
                return experience_points

        user_move_on()
        the_standings(goodGuys_team, badGuys_team)
        user_move_on()

        action = (user_action(goodGuys_team, pname)).lower()
        outcome = player_turn_outcome(goodGuys_team, badGuys_team, action, pname, experience_points)
        while outcome == -1:
            action = (user_action(goodGuys_team, pname)).lower()
            outcome = player_turn_outcome(goodGuys_team, badGuys_team, action, pname, experience_points)
            if outcome != -1:
                break

        good_guys_NPC_turn(goodGuys_team, badGuys_team, pname, experience_points)
        normal_bad_guys_turn(goodGuys_team, badGuys_team, special_event)


def level_up(goodGuys, p_name):
    # Checks if the input is valid
    incorrect_value = True
    while incorrect_value:
        # Asks the player which stat they want to increase
        want_to_increase = input("Would you like to increase your health or action points by 5?\n")
        # If they want to increase health it increases by 5
        if want_to_increase == 'health':
            goodGuys[p_name]['health'] = goodGuys[p_name]['health'] + 5
            print(str(goodGuys[p_name]['health']))
            # breaks out because the value entered was correct
            break
        # If they want to increase action points it increases by 5
        if want_to_increase == 'action points':
            goodGuys[p_name]['action_points'] = goodGuys[p_name]['action_points'] + 5
            print(str(goodGuys[p_name]['action_points']))
            # breaks out because the value entered was correct
            break
        # Give the player an example of what to input if they got it wrong
        print("Please enter health or action points\n")

    # Increases each person on the good guys team's level
    for key in goodGuys:
        goodGuys[key]['level'] = goodGuys[key]['level'] + 1

    # Increases Peter's health first then his action points, in order
    if goodGuys['Peter']['level'] % 2 == 0:
        goodGuys['Peter']['health'] = goodGuys['Peter']['health'] + 5
        print(str(goodGuys['Peter']['health']))
    else:
        goodGuys['Peter']['action_points'] = goodGuys['Peter']['action_points'] + 5
        print(str(goodGuys['Peter']['action_points']))

    # Increases Danielle's action points first then her health, in order
    if goodGuys["Danielle"]['level'] % 2 != 0:
        goodGuys["Danielle"]['health'] = goodGuys["Danielle"]['health'] + 5
        print(str(goodGuys["Danielle"]['health']))
    else:
        goodGuys["Danielle"]['action_points'] = goodGuys["Danielle"]['action_points'] + 5
        print(str(goodGuys["Danielle"]['action_points']))


def leveledLootSystem(goodGuys, player_inventory):
    if goodGuys[p_name]["level"] >= 2:
        print("Congrats you found a firework spell!")
        firework_stats = {"name": "firework", "explanation": "Deals 6 damage", "type": "damage", "effect": 6,
                          "ap_cost": 3}
        player_inventory["firework"].append(firework_stats)
    if goodGuys[p_name]["level"] >= 3:
        print("Congrats you found a holy hand grenade")


def does_game_continue(fight_outcome):
    if fight_outcome != -1:
        return 1
    else:
        continue_playing = input("Do you want to continue(Yes/No)\n")
        if continue_playing.lower() == "no":
            return False
        if continue_playing.lower() == "yes":
            return True


def playGame(player_name):
    # Giving each item an explanation, if it helps your team or deals damage, and how much effect it has
    knife_stats = {"name": "knife", "explanation": "Deals 2 damage", "type": "damage", "effect": 2, "ap_cost": 1}
    bow_stats = {"name": "bow", "explanation": "Deals 4 damage", "type": "damage", "effect": 3, "ap_cost": 2}
    fireball_stats = {"name": "fireball", "explanation": "Deals 5 damage", "type": "damage", "effect": 5, "ap_cost": 4}
    rest_stats = {"name": "rest", "explanation": "Returns 2 Action Points", "type": "help", "effect": 2, "ap_cost": 0}
    heal_stats = {"name": "heal", "explanation": "Heals for 4 HP", "type": "help", "effect": 3, "ap_cost": 2}

    player_inventory = {"knife": knife_stats, "bow": bow_stats, "fireball": fireball_stats, "rest": rest_stats,
                        "heal": heal_stats}
    player_stats = {"health": 20, "action_points": 10, "level": 1, "inventory": player_inventory}
    peter_stats = {"health": 20, "action_points": 10, "level": 1}
    danielle_stats = {"health": 20, "action_points": 10, "level": 1}
    goodGuys = {player_name: player_stats, "Peter": peter_stats, "Danielle": danielle_stats}
    experience_points = 800

    alastair_stats = {"health": 22, "action_points": 12, "level": 2}
    prescott_stats = {"health": 20, "action_points": 10, "level": 1}
    officium_stats = {"health": 20, "action_points": 10, "level": 1}
    fight_one = {"Alastair": alastair_stats, "Prescott": prescott_stats}
    boss_fight = {"Officium": officium_stats}

    fight_info = open("fight_info.txt", "w")
    fight_info.write("This is a Print out of your fight information. Which moves you and everyone else made are "
                     "recorded here.\n")
    fight_info.close()

    playing = True

    while playing:
        special_event = 1
        # Playing the first scene
        # scene1()

        # Starts the first fight
        # fight_one_intro()
        # user_action(goodGuys, p_name)
        fight_outcome = fight(goodGuys, fight_one, player_name, experience_points, special_event)
        user_move_on()
        if does_game_continue(fight_outcome):
            playGame(player_name)
        if not does_game_continue(fight_outcome):
            playing = False
            break
        print("Congrats you won! You gained " + str(experience_points) + " experience points and " + str(
            int(experience_points / 3)) + " coins.")
        if experience_points >= 800:
            level_up(goodGuys, player_name)
            experience_points = 0
        leveledLootSystem(goodGuys, player_inventory)

    return True


p_name = "Amelie"
# player_name = input("What is your name?")
playGame(p_name)
