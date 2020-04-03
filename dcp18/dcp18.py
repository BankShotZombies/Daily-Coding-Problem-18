
def maxOfSubarrays (k, arr):
    subArrays = getSubArrays(k, arr)
    maxArr = []
    for arr in subArrays:
        maxArr.append(max(arr))
    return maxArr

def getSubArrays (k, arr):
    i = 0
    subArrayAdd = 0
    subarrays = []
    for i in range (0, len(arr)):
        if subArrayAdd <= len(arr) - k:
            subarrays.append(arr[0 + subArrayAdd:k + subArrayAdd])
            subArrayAdd += 1
    return subarrays

print(maxOfSubarrays(1, [2, 3, 5, 6, 8, 10, 12, 13, 14, 15]))