import random


'''
insert sort
    - insert each elementt into its correct place in a sorted list
    
'''

def insertSort(data):
    for i in range(1, len(data)): #data[0:i] is already sorted
        elem = data[i] # current element to move
        #figure out where to move elem
        j = i - 1
        while j >= 0 and data[j] > elem:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = elem

'''
WC:
    n - len(data)
    T(n) =  SUM(i = 1, n)(i)  = 1 + 2 + ... + n included in O(n^2) 
'''


'''
merge sort
    - divide the list into halves 
    - sort the halves 
    - merge the halves

T(n) = { 1, n = 1
       { 2 * T(n / 2) + n = nlog(n)
'''

def merge(data1, data2):
    pass

def mergeSort(data):
    m = len(data) // 2
    left = mergeSort(data[:m])  # extra list copying on the side
    right = mergeSort(data[:m])
    return merge(left, right)

'''
Binary Search

T(n) = { 1, n = 1
       { T(n / 2) + 1

T(n) = T(n / 2) + 1
     = T(n / (2^k)) + k , k = log(n) 
     = log(n)

'''

data = list(range(10))
random.shuffle(data)

print(data)
insertSort(data)
print(data)

