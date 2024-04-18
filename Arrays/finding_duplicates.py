# finding duplicate integers in an array in a linear time complexity

def find_duplicates(nums):

    for num in nums:
        # convert index into its absolute value
        # if the value in that index is positive, flip the value to negative
        if nums[abs(num)] >= 0: 
            nums[abs(num)] = -nums[abs(num)]
        # else, it is a duplicate
        else:
            print(abs(num))


nums = [1, 2, 3, 1, 3, 6, 6]
find_duplicates(nums)


