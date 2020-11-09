from main import getGameData, normal_bad_guys_turn, setTestRolls, good_guys_NPC_turn, highest_health_target, \
    lowest_health_target


def test_Peter_fight_AI():
    test_player_name = "Test1"
    global TEST_ROLLS
    good_guys, stages_list, experience_points = getGameData(test_player_name)
    bad_guys = stages_list[0]["bad_guys"]
    setTestRolls([0, 10])

    good_guys_NPC_turn(good_guys, bad_guys, test_player_name, experience_points)
    assert bad_guys["Prescott"]["health"] == 10

    setTestRolls([0, 10])
    good_guys["Danielle"]["health"] = 10
    good_guys_NPC_turn(good_guys, bad_guys, test_player_name, experience_points)
    assert good_guys["Danielle"]["health"] == 13


def test_Danielle_fight_AI():
    test_player_name = "Test1"
    global TEST_ROLLS
    good_guys, stages_list, experience_points = getGameData(test_player_name)
    bad_guys = stages_list[0]["bad_guys"]
    setTestRolls([10, 0])

    good_guys_NPC_turn(good_guys, bad_guys, test_player_name, experience_points)
    assert bad_guys["Prescott"]["health"] == 10

    bad_guys["Prescott"]["health"] = 15

    setTestRolls([10, 0])
    good_guys["Danielle"]["action_points"] = 3
    good_guys_NPC_turn(good_guys, bad_guys, test_player_name, experience_points)
    assert bad_guys["Prescott"]["health"] == 12


def test_lowest_health_target():
    test_player_name = "Test1"
    global TEST_ROLLS
    good_guys, stages_list, experience_points = getGameData(test_player_name)
    bad_guys = stages_list[0]["bad_guys"]
    assert lowest_health_target(bad_guys) == "Alastair"

    good_guys["Peter"]["health"] = 10
    assert lowest_health_target(good_guys) == "Peter"


def test_highest_health_target():
    test_player_name = "Test1"
    global TEST_ROLLS
    good_guys, stages_list, experience_points = getGameData(test_player_name)
    assert highest_health_target(good_guys) == "Test1"

    bad_guys = stages_list[0]["bad_guys"]
    assert highest_health_target(bad_guys) == "Prescott"

    good_guys["Peter"]["health"] = 25
    assert highest_health_target(good_guys) == "Peter"


def test_peter_rest():
    test_player_name = "Test1"
    global TEST_ROLLS
    good_guys, stages_list, experience_points = getGameData(test_player_name)
    bad_guys = stages_list[0]["bad_guys"]

    good_guys["Peter"]["action_points"] = 1  # Needs to rest
    # Both bad guys do damage
    setTestRolls([15, 10])
    good_guys_NPC_turn(good_guys, bad_guys, test_player_name, experience_points)
    # Did this work as expect
    assert good_guys["Peter"]["action_points"] == 3


def test_danielle_rest():
    test_player_name = "Test1"
    global TEST_ROLLS
    good_guys, stages_list, experience_points = getGameData(test_player_name)
    bad_guys = stages_list[0]["bad_guys"]

    good_guys["Danielle"]["action_points"] = 1  # Needs to rest
    # Both bad guys do damage
    setTestRolls([15, 10])
    good_guys_NPC_turn(good_guys, bad_guys, test_player_name, experience_points)
    # Did this work as expect
    assert good_guys["Danielle"]["action_points"] == 3


def test_enemy_rest():
    test_player_name = "Test1"
    global TEST_ROLLS
    good_guys, stages_list, experience_points = getGameData(test_player_name)

    good_guys[test_player_name]["health"] = 9
    bad_guys = stages_list[0]["bad_guys"]
    bad_guys["Prescott"]["action_points"] = 1  # Needs to rest
    # Both bad guys do damage
    setTestRolls([15, 10])

    normal_bad_guys_turn(good_guys, bad_guys)
    # Did this work as expect
    assert good_guys[test_player_name]["health"] == 6
    assert bad_guys["Prescott"]["action_points"] == 3


def test_player_can_be_damaged():
    test_player_name = "Test1"
    global TEST_ROLLS
    good_guys, stages_list, experience_points = getGameData(test_player_name)

    good_guys[test_player_name]["health"] = 9
    bad_guys = stages_list[0]["bad_guys"]
    # Both bad guys do damage
    setTestRolls([15, 10])

    normal_bad_guys_turn(good_guys, bad_guys)
    # Did this work as expect
    assert good_guys[test_player_name]["health"] == 0


if __name__ == "__main__":
    test_player_can_be_damaged()
    test_enemy_rest()
    test_peter_rest()
    test_danielle_rest()
    test_highest_health_target()
    test_lowest_health_target()
    test_Peter_fight_AI()
    test_Danielle_fight_AI()
