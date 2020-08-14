### CodingBat Challenge 11-25-19 ###
#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers. #


# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4
#######################################################

# Solution 1 #
def sum67(nums):
    new_list = []
    indicator = 1
    for item in nums:
        if indicator:
            if item == 6:
                indicator = 0
            else:
                new_list.append(item)
        else:
            if item == 7:
                indicator = 1
    return sum(new_list)

# Solution 2 #
def sum67(nums):
    num_list = []
    skip = False
    for num in nums:
        if num == 6:
        skip = True
    if num == 7 and skip == False:
        num_list.append(num)
    elif num == 7:
        skip = False
    elif skip == False:
        num_list.append(num)
return sum(num_list)
