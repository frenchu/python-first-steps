from bullsandcows import count_cows_and_bulls


def test_count_cows_and_bulls1():
    # given
    generated_list = list("8138")
    user_list = list("8138")

    # when
    cows, bulls = count_cows_and_bulls(generated_list, user_list)

    # then
    assert cows == 4
    assert bulls == 0


def test_count_cows_and_bulls2():
    # given
    generated_list = list("8138")
    user_list = list("8318")

    # when
    cows, bulls = count_cows_and_bulls(generated_list, user_list)

    # then
    assert cows == 2
    assert bulls == 2


def test_count_cows_and_bulls3():
    # given
    generated_list = list("8138")
    user_list = list("8381")

    # when
    cows, bulls = count_cows_and_bulls(generated_list, user_list)

    # then
    assert cows == 1
    assert bulls == 3
