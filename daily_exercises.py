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
def add_numbers():
    for x in range():
        if

# problem four
def has22(nums):
    for x in range(len(nums)-1):
        if nums[x] == 2 and nums[x + 1] == 2:
            return True
    return False

print(has22([1, 2, 3, 4, 5, 2, 2]))


