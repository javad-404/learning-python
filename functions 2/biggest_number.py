def biggest_number (nums):
    biggest = nums[0]
    for i in nums:
        if i > biggest:
            biggest = i
    return biggest
    
my_nums = [1,5,99,63,69,45,2,3,999]
big = biggest_number(my_nums)
print (big)