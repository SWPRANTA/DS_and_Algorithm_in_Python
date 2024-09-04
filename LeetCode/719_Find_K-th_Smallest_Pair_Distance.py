# def smallestDistancePair(nums, k):
#     res = []
#     length = len(nums)
#     for i in range(length):
#         for j in range(i+1, length, 1):
#             res.append(abs(nums[i]-nums[j]))
#     res.sort()
#     return res[k-1]
def smallestDistancePair(nums, k):
    res = []
    length = len(nums)
    nums.sort()
    for i in range(length-1):
        res.append(abs(nums[i]-nums[i+1]))
        if len(res)==k:
            break
    return res

nums = [1,6,1]
k = 3

got = smallestDistancePair(nums, k)
print(got)