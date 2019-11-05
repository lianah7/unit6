# by Liana Hill
# last updated November 5, 2019
# unit 6 project - option one

import random


def are_duplicates(nums):
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] == nums[y]:
                return True
    return False


num_runs = int(input("How many times would you like to run this simulation?"))
duplicate_birthday = 0
for x in range(num_runs):
    birthdays = []
    for y in range(23):
        ran_num = random.randint(1, 365)
        birthdays.append(ran_num)
    print(are_duplicates(birthdays))
    if are_duplicates(birthdays) is True:
        duplicate_birthday = duplicate_birthday + 1
print(duplicate_birthday/num_runs * 100)
print("There were", duplicate_birthday, "times when there were duplicate birthdays")