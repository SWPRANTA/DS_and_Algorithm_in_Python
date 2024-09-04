def maxDistance(arrays):
    curmin = arrays[0][0]
    curmax = arrays[0][-1]
    maxDist = 0
    for arr in arrays[1:]:
        a = abs(curmax-arr[0])
        b = abs(curmin-arr[-1])
        maxDist = max(a, b, maxDist)
        curmax = max(curmax, arr[-1])
        curmin = min(curmin, arr[0])
    return maxDist

arrays = [[1,4],[0,5]]
res = maxDistance(arrays)
print(res)