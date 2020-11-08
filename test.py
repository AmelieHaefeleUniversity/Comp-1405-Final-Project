from main import getGameData, normal_bad_guys_turn, setTestRolls


def testEnemyMustRest():
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


def testPlayerHealthWhenTwoDamageRolls():
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
    testPlayerHealthWhenTwoDamageRolls()
    testEnemyMustRest()