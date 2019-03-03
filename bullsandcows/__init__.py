import random


def generate_number(no_digits):
    digits = "1234567890"
    number = ''
    for i in range(no_digits):
        number += random.choice(digits)
    return number


def count_cows_and_bulls(input_list1, input_list2):
    digit_list1 = input_list1.copy()
    digit_list2 = input_list2.copy()
    cows = []
    for i in range(len(digit_list1)):
        if digit_list1[i] == digit_list2[i]:
            cows.append(digit_list1[i])
    for cow in cows:
        digit_list1.remove(cow)
        digit_list2.remove(cow)
    bulls_count = 0
    for digit in digit_list1:
        if digit in digit_list2:
            bulls_count += 1
    return len(cows), bulls_count


def play_in_cows_and_bulls(number_to_guess_list):
    counter = 0
    while True:
        counter += 1
        print("Guess a number:")
        user_number_list = list(input())
        cows, bulls = count_cows_and_bulls(user_number_list, number_to_guess_list)
        print(f'cows: {cows:d}, bulls: {bulls:d}')
        if user_number_list == number_to_guess_list:
            print(f'You won in {counter:d}th round!')
            break
    return


play_in_cows_and_bulls(list(generate_number(4)))
