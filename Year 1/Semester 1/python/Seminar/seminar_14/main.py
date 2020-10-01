data = [6,-2,-3,1,5,-2, -1, 2]

def maxSum(arr):
    #global = best sum possible
    #local  = best sum right now
    global_sum = arr[0]
    local_sum = arr[0]
    pozi = 0
    pozj = 0
    for i in range(1, len(arr)):
    #overlapping subproblems
       local_sum = max(arr[i], arr[i] + local_sum)
       if global_sum < local_sum:
           global_sum = local_sum

    return global_sum

def dcMiddle(arr, low, high):
    m = (low + high) // 2
    # for loop with partial sums between low and m
    # for loop with partial sums between m and high
    # add max partial sum in left half to right half and with arr[m] and return it
    pass

def dcMax(arr, low, high):
    if low == high:
        return  arr[0]
    m = (low + high) // 2
    return max(dcMax(arr, low, m), dcMax(arr, m + 1, high), dcMiddle(arr, low, high))

def dpMax(arr):
    maxSum(arr)

#print(maxSum(data))
#print(dcMax(data, 1, len(data)))

s1 = 'abcdefgh'
s2 = 'jklmnop'

#transform character by character, start from the end
def xform(s1,s2):
    #one string is empty
    if len(s1) == 0:
        return len(s2)
    elif len(s2) == 0:
        return len(s1)
    elif s1[-1] == s2[-1]:
        return xform(s1[:-1], s2[:-1])
    return 1 + min(
    xform(s1[:-1], s2), # delete last char of s1
    xform(s1[:-1], s2[:-1]), #replace last char of s1
    xform(s1, s2[:-1])) #insert at the end of s1

print(xform(s1,s2))