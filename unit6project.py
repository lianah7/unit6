# by Liana Hill
# last updated November 5, 2019
# unit 6 project - option one

import random


def are_duplicates(nums):
    """
    This function finds duplicate birthdays by comparing values in a list
    :param nums: the list
    :return: True or false depending on if there is a duplicate
    """
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] == nums[y]:
                return True
    return False


def main():
    num_runs = int(input("How many times would you like to run this simulation?"))
    duplicate_birthday = 0
    for x in range(num_runs):
        birthdays = []
        for y in range(23):
            ran_num = random.randint(1, 365)
            birthdays.append(ran_num)
        if are_duplicates(birthdays) is True:
            duplicate_birthday = duplicate_birthday + 1
    print("There were duplicate birthdays", duplicate_birthday / num_runs * 100, "% of the time.")
    print(duplicate_birthday, "of the simulations run had duplicate birthdays.")


main()
