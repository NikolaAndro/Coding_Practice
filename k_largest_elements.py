'''
Given an array of N positive integers, print k largest elements from the array. 

Input:
N = 5, k = 2
arr[] = {12,5,787,1,23}
Output: 787 23
Explanation: First largest element in
the array is 787 and the second largest
is 23.

Your Task:
Complete the function kLargest() that takes the array, N and K as input parameters and returns a list of k largest element in descending order. 


Approach: I'll try using queue.
'''

#Function to return k largest elements from an array.
def kLargest(lista,n,k):
    return sorted(lista, reverse = True)[:k]

l = [1, 23, 12, 9, 30, 2, 50]
n = 7
k = 2
ah = kLargest(l,n,k)

print(ah)