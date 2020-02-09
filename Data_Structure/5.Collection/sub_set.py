def subset(s):
    if s >= len(arr):
        print(selected)
        return 
    selected[s] = 1
    subset(s+1)
    selected[s] = 0
    subset(s+1)

arr = [1, 2, 3]
selected = [0] * len(arr)
subset(0)


