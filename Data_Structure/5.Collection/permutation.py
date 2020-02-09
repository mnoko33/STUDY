def perm(s, k, nums):
    if s == k:
        print(nums[:k])
        return
    
    for i in range(s, len(nums)):
        nums[i], nums[s] = nums[s], nums[i]
        perm(s+1,k,nums)
        nums[i], nums[s] = nums[s], nums[i]

nums = [4, 2, 9, 5, 6, 1]
perm(0, 4, nums)