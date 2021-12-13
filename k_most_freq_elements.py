'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

'''

def topKFrequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_dict = {}

        #Create a dictionary with zeros and then fill it up with frequency of each number    
        for i in nums:
            freq_dict[i] = 0
        for i in nums:
            freq_dict[i] += 1

        # create a list of tuples from t he dictionary
        final = [(x, freq_dict[x]) for x in freq_dict]
        #sort the list by valu in reverse order
        final.sort(key = lambda x: x[1], reverse=True)
        #returning list will be the list of keys from the beginning of the list until kth element.
        fin = [x[0] for x in final[:k]]

        return fin
        
lista = [-5,-5,-5,-5,-5,1,1,1,2,3,4,5,5,5,5]
k=2
print(topKFrequent(lista,k))