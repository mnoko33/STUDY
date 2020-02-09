def comb(s, r, selected):
    if sum(selected) == r:
        print(selected)
        return

    if s == len(nums):
        return

    selected[s] = 1
    comb(s+1,r,selected)
    selected[s] = 0
    comb(s+1,r,selected)
    
        
nums = [1, 2, 3, 4, 5, 6, 7, 8]
selected = [0] * len(nums)
comb(0, 4, selected)