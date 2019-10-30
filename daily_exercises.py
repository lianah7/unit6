# by Liana Hill
# last updated October 28, 2019
# unit 6 daily exercises

# problem one
names = ["Abigail", "Brenda", "Chad", "Doug", "Emma", "Francis", "George", "Harold", "Imogen",
         "Jackie", "Kurt", "Linda"]
print(names[3:4])
print(names[1:6])
print(names[5:12])
print(names[5:])
print(names[11])
print(names[-1])
print(names[1:8:2])
print(names[0:11:2])
print(names[:11:2])
print(names[11:8:-1])
print(names[11:0:-1])
print(names[:0:-1])

# problem two


def are_duplicates(nums):
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] == nums[y]:
                return True
    return False


print(are_duplicates([100, 2, 3, 4, 101]))

# problem three


def add_numbers(nums):
    total = 0
    for x in nums:
        total += x
    return total


print(add_numbers([9, 5, 11, 6, 1, 15]))

# problem four


def has22(nums):
    for x in range(len(nums)-1):
        if nums[x] == 2 and nums[x + 1] == 2:
            return True
    return False


print(has22([1, 2, 3, 4, 5, 2, 2]))

# problem five


def is_sorted(nums):
    for x in range(len(nums)-1):
        if nums[x + 1] > nums[x]:
            return True
    return False


print(is_sorted([1, 2, 2, 3, 5]))

# problem six


def remove_duplicates(nums):
    removed = []
    for x in nums:
        if x not in removed:
            removed.append(x)
    return removed


print(remove_duplicates([1, 2, 2, 3, 4, 5, 6, 6, 7, 7, 7]))


# problem seven


def get_max(nums):
    maximum = nums[0]
    for x in nums:
        if x > maximum:
            maximum = x
    return maximum


print(get_max([-6, -89, 2, 45, 19]))


# problem eight


def get_max(nums):
    minimum = nums[0]
    for x in nums:
        if x < minimum:
            minimum = x
    return minimum


print(get_max([89, 70, -34, -5]))
