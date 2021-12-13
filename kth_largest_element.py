'''
Given an integer array, find k’th largest element in the array where k is a positive integer less than or equal to the length of array.

'''
def kth_largest(lista,k):
    return sorted(lista, reverse = True)[k-1]

li =  [7, 4, 6, 3, 9, 1]
k = 2
print(kth_largest(li,k))