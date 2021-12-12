'''ou are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# printing the linked list
def print_list(lista):
    while lista != None:
        print(lista.val, end=' ')
        lista = lista.next
    print()

#merging two linked lists
def merge_sort(L1=None,L2=None):
    #base cases
    if L1 == None: return L2
    if L2 == None: return L1
    
    final = ListNode()
    real_final = final

    while L1 != None and L2 != None:
        if L1.val <= L2.val:
            final.next = L1
            final = final.next
            L1 = L1.next
        else:
            final.next = L2
            final = final.next
            L2 = L2.next
    
    if L1 == None:
        final.next = L2
    else:
        final.next = L1
        
    return real_final.next


    
def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    if len(lists) == 0: return None
    if len(lists) == 1: return lists[0]

    #merge firsts 2 lists
    n = merge_sort(lists[0],lists[1])
    #pop 1st list
    lists.pop(0)
    #replace 2nd list with the new merged list
    lists[0] = n
    #keep merging
    mergeKLists(lists)

    return lists[0]




l1 = ListNode(1,ListNode(2,ListNode(3)))   
l2 = ListNode(1,ListNode(2,ListNode(3))) 
l3 = ListNode(1,ListNode(5)) 

lists = [l1,l2,l3]
mergeKLists(lists)
print_list(lists[0])

