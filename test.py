from main import getGameData, normal_bad_guys_turn, setTestRolls, good_guys_NPC_turn, highest_health_target

def test_highest_health_target():
    test_player_name = "Test1"
    global TEST_ROLLS
    good_guys, stages_list, experience_points = getGameData(test_player_name)
    highest_health_target(good_guys)
    assert highest_health_target(good_guys) == "Test1"

    bad_guys = stages_list[0]["bad_guys"]
    highest_health_target(bad_guys)
    assert highest_health_target(bad_guys) == "Test1"


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