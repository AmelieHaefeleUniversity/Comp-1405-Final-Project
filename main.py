from random import *
import copy

TEST_ROLLS = []


# The d20 dice
def d20():
    global TEST_ROLLS
    if len(TEST_ROLLS) > 0:
        return TEST_ROLLS.pop(0)
    return randint(0, 20)


# Allows tests to specify test rolls. Needed python globals are not shared across modules.
def setTestRolls(to_roll):
    global TEST_ROLLS
    TEST_ROLLS = to_roll


# clears the screen
def clear():
    print("\n" * 100)


# waits for the user input, which can be anything, to move onto another screen
def user_move_on():
    user_action = input()
    clear()


# adds the given string to the output file
def add_to_file(string):
    fight_info_file = open("fight_info.txt", "a")
    fight_info_file.write(string)
    fight_info_file.close()


# Goes through the given team and prints out their stats
def print_teams(team):
    for key in team:
        print("\n" + str(key) + "\n HP:" + str(team[key]['health']) + "\nAP:" + str(
            team[key]['action_points']) + "\n")


# Prints out how each team is doing at the beginning of each turn to help inform the player
def the_standings(good_guys_team, bad_guys_team):
    print("-" * 79 + "\n The Standings\n" + "-" * 79 + "\n")
    print("Your Team:")
    # Prints out each member on your team's, health and action points
    print_teams(good_guys_team)
    print("-" * 79 + "\n The Enemy Team\n" + "-" * 79)
    # Prints out each member on the enemy team's, health and action points
    print_teams(bad_guys_team)
    return True


# What gets printed out when the player or an NPC misses
def print_miss_action(name, action, roll, target):
    to_print = (name + " used their " + action + " and rolled a(n) " + str(roll) + " missing " + target + "\n")
    # prints it then adds it to the output file
    print(to_print)
    add_to_file(to_print)


# What gets printed out when the player or an NPC heals a target
def print_heal_action(name, action, roll, target, effect):
    to_print = (name + " used " + action + " and rolled a(n) " + str(
        roll) + " succeeding healing " + target + " for " + str(
        effect) + " health\n")
    # prints it then adds it to the output file
    print(to_print)
    add_to_file(to_print)


# What gets printed out when the player or an NPC harms a target
def print_harm_action(name, action, roll, target, effect):
    to_print = (name + " used their " + action + " and rolled a(n) " + str(
        roll) + " hitting " + target + " for " + str(
        effect) + " damage\n")
    # prints it then adds it to the output file
    print(to_print)
    add_to_file(to_print)


# What gets printed out when the player or an NPC rests
def print_rest(name):
    to_print = (name + " rested regaining 2 Action Points\n")
    # prints it then adds it to the output file
    print(to_print)
    add_to_file(to_print)


# What gets printed out when an NPC's health is 0 or less and will not be able to fight
def print_person_down(name):
    to_print = (name + " has fallen and is unable to fight\n")
    # prints it then adds it to the output file
    print(to_print)
    add_to_file(to_print)


def lowest_health_target(team):
    # initializing variables
    lowestHealth_NPC = ""
    for i in team:
        lowestHealth = team[i]['health']
        lowestHealth_NPC = str(i)
        break
    # checks which player on the good guys team has the lowest health and saves it
    for key in team:
        # Checks it they're dead
        if lowestHealth > team[key]['health'] > 0:
            lowestHealth_NPC = str(key)
            lowestHealth = team[key]['health']
    return lowestHealth_NPC


# I wanted the boss to taunt you and be purely based on luck so this code is not general on purpose
def boss_fight(good_guys_team, bad_guys_team):
    # initializing variables
    target = lowest_health_target(good_guys_team)
    roll = d20()
    if roll == 20:
        good_guys_team[target]["health"] = good_guys_team[target]["health"] - 20
        print_harm_action("Officium", "random", roll, target, 20)
        print("A perfect roll how about that!\n")
        return good_guys_team
    if roll > 18:
        good_guys_team[target]['health'] = good_guys_team[target]['health'] - 8
        print_harm_action("Officium", "random", roll, target, 8)
        print("Wow good luck doing better than that\n")
        return good_guys_team
    if roll > 16:
        bad_guys_team["Officium"]["health"] = bad_guys_team["Officium"]["health"] + 10
        print_heal_action("Officium", "heal", roll, "Officium", 10)
        print("Hmm full health, don't mind if I do\n")
        return good_guys_team
    if roll > 12:
        good_guys_team[target]["health"] = good_guys_team[target]["health"] - 6
        print_harm_action("Officium", "random", roll, target, 6)
        print("A normal attack? Huh I guess that'll do\n")
        return good_guys_team
    if roll > 6:
        print_miss_action("Officium", "random", roll, target)
        print("Damn it\n")
        return good_guys_team
    if roll > 4:
        good_guys_team[target]["action_points"] = good_guys_team[target]["action_points"] - 4
        print_harm_action("Officium", "action drain", roll, target, 4)
        print("You can't do anything right\n")
        return good_guys_team
    if roll > 2:
        bad_guys_team["Officium"]["health"] = bad_guys_team["Officium"]["health"] + 10
        print_heal_action("Officium", "heal", roll, "Officium", 10)
        print("Nothing you do can stop me\n")
        return good_guys_team
    if roll == 0:
        good_guys_team[target]["action_points"] = good_guys_team[target]["action_points"] - 2
        print_harm_action("Officium", "action drain", roll, target, 2)
        print("You're alone\n")
        return good_guys_team


# Gets the action the user wants to preform, it also prints out the actions the player can do, what they do,
# and how many action points it costs
def get_user_action(good_guys_team, player_name):
    value_incorrect = True
    print("Player Turn!")
    # Prints out the users health and action points
    print("-" * 79 + "\n" + str(player_name) + "  HP: " + str(good_guys_team[player_name]['health']) + " AP: " + str(
        good_guys_team[player_name]['action_points']) + "\n" + "-" * 79)
    # Prints out each action, what it does, and how many action points it costs
    for key, value in (good_guys_team[player_name]['inventory']).items():
        print(str(key.capitalize()) + ", " + str(
            (good_guys_team[player_name]['inventory'])[key]['explanation']) + ", Cost: " + str(
            (good_guys_team[player_name]['inventory'])[key]['ap_cost']) + " Action Point(s)" + "\n")
    # While the value is incorrect
    while value_incorrect:
        # Asks what action the user wants to do
        action = input("What would you like to do/use?\n")
        # Checks if they can preform that action
        for key, value in (good_guys_team[player_name]['inventory']).items():
            if action == str((good_guys_team[player_name]['inventory'])[key]['name']):
                # Returns the action
                return key.lower()
        # Prints out letting the user know they entered and incorrect value
        else:
            # Else it tells the player what to do and continues asking into a valid actions inputted
            print("Please enter a proper value(ie enter 'heal', if you want to heal) refer to the listed actions "
                  "above for other options")


def player_turn(good_guys_team, bad_guys_team, action, player_name, experience_points):
    # checks if the player has enough action points to preform the given action
    if good_guys_team[player_name]["inventory"][action]["ap_cost"] > good_guys_team[player_name]['action_points']:
        print("Error you only have " + str(
            good_guys_team[player_name]['action_points']) + " action point(s) please heal or "
                                                            "chose an action that costs less")
        return -1
    # If the player chooses a harmful attack they will target the enemy team
    if good_guys_team[player_name]["inventory"][action]['type'] == "damage":
        print("Who do you want to target?\n")
        # Printing out the name of each enemy
        for enemy_names in bad_guys_team:
            print(enemy_names + "\n")
        # Capitalizing it in cause the player didn't
        target = (input("Enter your Target here:\n")).capitalize()
        # Removes the number of action points the attack costs
        good_guys_team[player_name]['action_points'] = good_guys_team[player_name]['action_points'] - \
                                                       good_guys_team[player_name]["inventory"][action]["ap_cost"]
        # Rolling the dice
        roll = d20()
        # If it hits
        if roll >= 10:
            # The amount of damaged is removed from the targets health
            bad_guys_team[target]["health"] = bad_guys_team[target]["health"] - \
                                              good_guys_team[player_name]["inventory"][action][
                                                  'effect']
            # Add experience points for the hit
            experience_points = experience_points + 50
            # Print out what happened
            print_harm_action(player_name, action, roll, target, good_guys_team[player_name]["inventory"][action][
                'effect'])
        # If it does not hit
        elif roll < 10:
            # Prints out what happened
            print_miss_action(player_name, action, roll, target)

    # If the player chooses a helpful attack it will ask which person on their team to target
    if good_guys_team[player_name]["inventory"][action]['type'] == "help":
        # The player can only rest themselves and it will always been successful
        if action == "rest":
            good_guys_team[player_name]["action_points"] = good_guys_team[player_name]["action_points"] + \
                                                           good_guys_team[player_name]["inventory"][action]['effect']
            # Print out what happened
            print_rest(player_name)
            return experience_points
        # Printing out all players on their team
        print("Who do you want to target?\n")
        for ally_names in good_guys_team:
            print(ally_names + "\n")
        # Get the targets name
        target = (input("Enter your Target here:\n")).capitalize()
        # Taking away the action point cost
        good_guys_team[player_name]['action_points'] = good_guys_team[player_name]['action_points'] - \
                                                       good_guys_team[player_name]["inventory"][action]["ap_cost"]
        # Rolling the dice
        roll = d20()

        # if its a healing action
        if action == 'heal':
            # If it succeeds
            if roll >= 10:
                # Heals the target
                good_guys_team[target]["health"] = good_guys_team[target]["health"] + \
                                                   good_guys_team[player_name]["inventory"][action]['effect']
                # Add experience points for the hit
                experience_points = experience_points + 50
                # Print out what happens
                print_heal_action(player_name, action, roll, target, good_guys_team[player_name]["inventory"][action][
                    'effect'])

            # If it fails
            if roll < 10:
                # Prints out what happened
                print_miss_action(player_name, "heal", roll, target)
            # If it fails terribly
            if roll < 4:
                # Takes the heal away
                good_guys_team[target]["health"] = good_guys_team[target]["health"] - \
                                                   good_guys_team[player_name]["inventory"][action]['effect']
                to_print = (player_name + " used " + action + " and rolled a(n) " + str(
                    roll) + " failing horribly " + target + " hurting them for " +
                            str(good_guys_team[player_name]["inventory"][action]['effect']) + " damage")
                print(to_print)
                add_to_file(to_print)

    return experience_points


def do_allies_need_healing(team, player_name):
    lowestHealth_Ally = "-1"
    lowestHealth = team[player_name]['health']
    for key in team:
        # Checks if anyone needs to be healed
        if team[key]["health"] <= 10:
            if team[key]["health"] <= lowestHealth:
                lowestHealth_Ally = str(key)
                lowestHealth = team[key]['health']

    return lowestHealth_Ally


def highest_health_target(team):
    # initializing variables
    highest_health_NPC = ""
    highestHealth = 0
    # Checks which enemy has the highest health and saves it
    for i in team:
        highestHealth = team[i]['health']
        highest_health_NPC = str(i)
        break
    # checks which player on the good guys team has the lowest health and saves it
    for key in team:
        # Checks it they're dead
        if highestHealth < team[key]['health'] > 0:
            highest_health_NPC = str(key)
            highestHealth = team[key]['health']
    return highest_health_NPC


def good_guys_NPC_turn(good_guys_team, bad_guys_team, player_name, experience_points):
    target = highest_health_target(bad_guys_team)
    # Checks if Danielle is still alive
    if good_guys_team["Danielle"]['health'] <= 0:
        print_person_down("Danielle")
        # Danielle's battle AI
    else:
        # If Danielle has less than 2 AP points she will choose to rest
        if good_guys_team["Danielle"]['action_points'] < 2:
            good_guys_team["Danielle"]['action_points'] = good_guys_team["Danielle"]['action_points'] + 2
            return experience_points
        # If Danielle is above 4 ap then use their strongest attack to attack the bad guy NPC with the most health
        elif good_guys_team["Danielle"]['action_points'] > 4:
            # Removes the number of action points it takes to use her bow
            good_guys_team["Danielle"]['action_points'] = good_guys_team["Danielle"]['action_points'] - 2
            # Rolling the dice
            roll = d20()
            # If her roll succeeds
            if roll >= 10:
                # Remove health from the enemy she targets for amount of damage she does (at her current level)
                bad_guys_team[target]['health'] = bad_guys_team[target]['health'] - (
                        4 + good_guys_team["Danielle"]["level"])
                # Add experience points for the hit
                experience_points = experience_points + 50
                # Prints out what happens
                print_harm_action("Danielle", "bow", roll, target,
                                  4 + good_guys_team["Danielle"]["level"])
            # If her roll fails
            elif roll < 10:
                # Prints out what happens
                print_miss_action("Danielle", "bow", roll, target)

        # If she is below 4 ap or below and less than or equal to 2 AP point she will attack the strongest enemy with
        # her knife
        elif good_guys_team["Danielle"]['action_points'] >= 2:
            #  Removes the number of action points it takes to use her knife
            good_guys_team["Danielle"]['action_points'] = good_guys_team["Danielle"]['action_points'] - 1
            # Rolling the dice
            roll = d20()
            # If her roll succeeds
            if roll >= 10:
                # Remove health from the enemy she targets for amount of damage she does (at her current level)
                bad_guys_team[target]['health'] = bad_guys_team[target]['health'] - (
                        2 + good_guys_team["Danielle"]["level"])
                # Add experience points for the hit
                experience_points = experience_points + 50
                # Prints out what happens
                print_harm_action("Danielle", "knife", roll, target,
                                  2 + good_guys_team["Danielle"]["level"])
            # If her roll fails
            elif roll < 10:
                # Prints out what happens
                print_miss_action("Danielle", "knife", roll, target)

    # Checks if Peter is still alive
    if good_guys_team['Peter']['health'] <= 0:
        print_person_down("Peter")
    else:
        # Peter's battle AI

        # If he has less than 4 action points he will chose to rest
        if good_guys_team['Peter']['action_points'] < 4:
            good_guys_team['Peter']['action_points'] = good_guys_team['Peter']['action_points'] + 2
            print_rest("Peter")
            return experience_points
        # Checks if any of the members on his team are 10 health or below
        lowestHealth_Ally = do_allies_need_healing(good_guys_team, player_name)
        if lowestHealth_Ally != "-1":
            # Rolls the dice
            roll = d20()
            # If it succeeds
            if roll >= 10:
                # Heals the player the correct amount for his current level
                good_guys_team[lowestHealth_Ally]['health'] = good_guys_team[lowestHealth_Ally]['health'] + (
                        2 + good_guys_team['Peter']['level'])
                # Prints out what happens
                # Add experience points for the hit
                experience_points = experience_points + 50
                print_heal_action("Peter", "heal", roll, str(lowestHealth_Ally),
                                  2 + good_guys_team['Peter']['level'])
                # Returns  here so that he doesn't heal more than 1 person per turn
                return experience_points
            # If the roll fails
            elif roll < 10:
                print_miss_action("Peter", "heal", roll, str(lowestHealth_Ally))
                #  Returns  here so that he doesn't heal more than 1 person per turn
                return experience_points
            # He is too good to fail tremendously (I don't want him accidentally killing the player)
        else:
            good_guys_team['Peter']['action_points'] = good_guys_team['Peter']['action_points'] - 3
            roll = d20()
            if roll >= 10:
                # Add experience points for the hit
                experience_points = experience_points + 50
                bad_guys_team[target]['health'] = bad_guys_team[target]['health'] - (
                        4 + good_guys_team["Peter"]["level"])
                print_harm_action("Peter", "fireball", roll, target,
                                  4 + good_guys_team["Peter"]["level"])
                return experience_points
            if roll < 10:
                print_miss_action("Peter", "fireball", roll, target)
    return experience_points


def normal_bad_guys_turn(good_guys_team, bad_guys_team):
    # Goes through each bad guy so they have a chance to attack
    target = lowest_health_target(good_guys_team)
    for bad_guy in bad_guys_team:
        if bad_guys_team[bad_guy]['health'] <= 0:
            print_person_down(bad_guy)
        else:
            # If their action points are less than 2 they choose to rest
            if bad_guys_team[bad_guy]["action_points"] <= 2:
                bad_guys_team[bad_guy]['action_points'] = bad_guys_team[bad_guy]['action_points'] + 2
                # Prints out what happens
                print_rest(bad_guy)
            # If their action points are above 2 they choose to attack
            elif bad_guys_team[bad_guy]["action_points"] > 2:
                roll = d20()
                # If their roll succeeds
                if roll >= 10:
                    # calculates their damage based on their level
                    damage = bad_guys_team[bad_guy]["level"] + 3
                    # removes the health from the target they attack
                    good_guys_team[target]['health'] = good_guys_team[target]['health'] - (
                            bad_guys_team[bad_guy]["level"] + 3)
                    # Prints out what happens
                    print_harm_action(bad_guy, "slashed", roll, target, damage)
                # If their roll fails
                elif roll < 10:
                    # Prints out what happens
                    print_miss_action(str(bad_guy), "slashed", roll, target)
    return good_guys_team, bad_guys_team


# The fight function that takes the people fighting as arguments
def fight(good_guys_team, bad_guys_team, player_name, experience_points):
    keep_going = True
    number_dead = 0
    while keep_going:
        # Checks if the player has died
        if good_guys_team[player_name]['health'] <= 0:
            return -1
        # Goes through each enemy in the list (regular indexing doesn't work cause dictionaries)

        for key in bad_guys_team:
            # Adds 1 to the number of dead if the enemies health has reached 0
            if bad_guys_team[key]['health'] <= 0:
                number_dead += 1
            # If all of the enemies are dead then the good guys have won and it returns true
            if number_dead == len(bad_guys_team) + 1:
                return experience_points

        user_move_on()
        the_standings(good_guys_team, bad_guys_team)
        user_move_on()

        action = (get_user_action(good_guys_team, player_name)).lower()

        outcome = player_turn(good_guys_team, bad_guys_team, action, player_name, experience_points)
        experience_points = experience_points + outcome
        # checks if the player has enough action-points to do their chosen action
        while outcome == -1:
            # keeps checking until it gets a valid action
            action = (get_user_action(good_guys_team, player_name)).lower()
            outcome = player_turn(good_guys_team, bad_guys_team, action, player_name, experience_points)
            # if it gets a valid input it breaks out of the while loop
            if outcome != -1:
                break
        # The good guys turn
        experience_points = good_guys_NPC_turn(good_guys_team, bad_guys_team, player_name,
                                               experience_points) + experience_points

        # Checks if it's a normal bad guys turn or the boss fight
        for key in bad_guys_team:
            if key == "Officium":
                boss_fight(good_guys_team, bad_guys_team)
        else:
            normal_bad_guys_turn(good_guys_team, bad_guys_team)


def level_up_Peter(good_guys):
    # Increases Peter's health first then his action points, in order
    if good_guys['Peter']['level'] % 2 == 0:
        good_guys['Peter']['health'] = good_guys['Peter']['health'] + 15
        print(str(good_guys['Peter']['health']))
    else:
        good_guys['Peter']['action_points'] = good_guys['Peter']['action_points'] + 15
        print(str(good_guys['Peter']['action_points']))
    return good_guys


def level_up_Danielle(good_guys):
    if good_guys["Danielle"]['level'] % 2 != 0:
        good_guys["Danielle"]['health'] = good_guys["Danielle"]['health'] + 15
        print(str(good_guys["Danielle"]['health']))
    else:
        good_guys["Danielle"]['action_points'] = good_guys["Danielle"]['action_points'] + 15
        print(str(good_guys["Danielle"]['action_points']))
    return good_guys


def level_up(good_guys, player_name):
    # Checks if the input is valid
    incorrect_value = True
    while incorrect_value:
        # Asks the player which stat they want to increase
        want_to_increase = input("Would you like to increase your health or action points by 15?\n")
        # If they want to increase health it increases by 15
        if want_to_increase == 'health':
            good_guys[player_name]['health'] = good_guys[player_name]['health'] + 15
            print(str(good_guys[player_name]['health']))
            # breaks out because the value entered was correct
            break
        # If they want to increase action points it increases by 15
        if want_to_increase == 'action points':
            good_guys[player_name]['action_points'] = good_guys[player_name]['action_points'] + 15
            print(str(good_guys[player_name]['action_points']))
            # breaks out because the value entered was correct
            break
        # Give the player an example of what to input if they got it wrong
        print("Please enter health or action points\n")
    level_up_Peter(good_guys)
    level_up_Danielle(good_guys)
    return good_guys


def leveled_loot_system(good_guys, player_inventory):
    if good_guys[p_name]["level"] >= 2:
        print("Congrats you found a firework spell!")
        firework_stats = {"name": "firework", "explanation": "Deals 6 damage", "type": "damage", "effect": 6,
                          "ap_cost": 3}
        player_inventory["firework"] = firework_stats
    if good_guys[p_name]["level"] >= 3:
        print("Congrats you found a holy hand grenade")
        holy_hand_grenade_stats = {"name": "firework", "explanation": "Deals 8 damage", "type": "damage", "effect": 8,
                                   "ap_cost": 4}
        player_inventory["holy hand grenade"] = holy_hand_grenade_stats


def print_text_from_file(start_line, end_line, lines):
    # Plays the first scene
    i = start_line
    while i <= end_line:
        print(lines[i])
        i += 1
    user_move_on()
    return


def getGameData(player_name):
    # Giving each item an explanation, if it helps your team or deals damage, and how much effect it has
    knife_stats = {"name": "knife", "explanation": "Deals 2 damage", "type": "damage", "effect": 2, "ap_cost": 1}
    bow_stats = {"name": "bow", "explanation": "Deals 4 damage", "type": "damage", "effect": 3, "ap_cost": 2}
    fireball_stats = {"name": "fireball", "explanation": "Deals 5 damage", "type": "damage", "effect": 5, "ap_cost": 4}
    rest_stats = {"name": "rest", "explanation": "Returns 2 Action Points", "type": "help", "effect": 2, "ap_cost": 0}
    heal_stats = {"name": "heal", "explanation": "Heals for 4 HP", "type": "help", "effect": 3, "ap_cost": 2}

    # The player inventory holding all the items
    player_inventory = {"knife": knife_stats, "bow": bow_stats, "fireball": fireball_stats, "rest": rest_stats,
                        "heal": heal_stats}
    # The good guys stats
    player_stats = {"health": 20, "action_points": 10, "level": 1, "inventory": player_inventory}
    peter_stats = {"health": 20, "action_points": 10, "level": 1}
    danielle_stats = {"health": 20, "action_points": 10, "level": 1}
    # The good guys list
    good_guys = {player_name: player_stats, "Peter": peter_stats, "Danielle": danielle_stats}
    # Your experience points
    experience_points = 0

    # Bad Guys and their stats
    alastair_stats = {"health": 10, "action_points": 15, "level": 1}
    prescott_stats = {"health": 15, "action_points": 15, "level": 2}
    officium_stats = {"health": 20, "action_points": 10, "level": 1}
    Fluffy_stats = {"health": 10, "action_points": 10, "level": 1}
    Hoppy_stats = {"health": 15, "action_points": 12, "level": 2}
    Cinnabun_stats = {"health": 20, "action_points": 8, "level": 3}

    # What fight consists of what bad guys
    fight_one = {"Alastair": alastair_stats, "Prescott": prescott_stats}
    fight_two = {"Fluffy": Fluffy_stats, "Hoppy": Hoppy_stats, "Cinnabun": Cinnabun_stats}
    final_fight = {"Officium": officium_stats}

    # Information that is included in each stage that it needs to have in order to run
    stages_list = [{"StageName": "First Fight", "TextLineToPrint": (10, 23), "bad_guys": fight_one},
                   {"StageName": "Second Fight", "TextLineToPrint": (28, 43), "bad_guys": fight_two},
                   {"StageName": "Boss Fight", "TextLineToPrint": (45, 56), "bad_guys": final_fight}]

    return good_guys, stages_list, experience_points


def play_game(player_name):
    read_file = open("text.txt", "r")
    lines = read_file.readlines()
    read_file.close()

    good_guys, stages_list, experience_points = getGameData(player_name)

    # Opens the fight intro file so you can appened to it instead of writing
    fight_info = open("fight_info.txt", "w")
    fight_info.write("This is a Print out of your fight information. Which moves you and everyone else made are "
                     "recorded here.\n")
    fight_info.close()
    # Starts at stage 0
    stage_counter = 0

    # Reads out the Intro text
    print_text_from_file(1, 7, lines)
    user_move_on()

    bad_guys = stages_list[0]["bad_guys"]
    while stage_counter < len(stages_list):

        # Saves stats so they don't get rest
        # If you want to heal after every fight so it's easier set saved_good_guys = saved_good_guys
        # this is helping when debugging
        saved_good_guys = copy.deepcopy(good_guys)
        saved_bad_guys = copy.deepcopy(bad_guys)
        start_line, end_line = stages_list[stage_counter]["TextLineToPrint"]

        print_text_from_file(start_line, end_line, lines)
        # Do the fight
        experience_points = fight(good_guys, bad_guys, player_name, experience_points)
        if experience_points < 0:
            good_guys = saved_good_guys
            bad_guys = saved_bad_guys
            print("You Died. Don't lose hope!\n")
            add_to_file("You died\n")
            continue_playing = input("Do you want to continue(Yes/No)\n")
            if continue_playing.lower() == "no":
                break
        else:
            stage_counter += 1
            bad_guys = stages_list[stage_counter]["bad_guys"]
            # Leveling up
            print("Congrats you won! You gained " + str(experience_points) + " experience points and " + str(
                int(experience_points / 3)) + " coins.")
            if experience_points >= 2000:
                level_up(good_guys, player_name)
                experience_points = experience_points - 2000
            # Leveled loot system
            leveled_loot_system(good_guys, good_guys[player_name]["inventory"])
            user_move_on()
    # reads out the ending text
    print_text_from_file(58, 63, lines)
    user_move_on()
    return True


# Will only run when someone runs main.py to allow for simulated test
if __name__ == "__main__":
    p_name = "Amelie"
    # player_name = input("What is your name?")
    play_game(p_name)
