# nums = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

for i in range(len(nums)):
    if nums[i] == nums[i + 1]:
        nums.pop(i)
    print(nums)
