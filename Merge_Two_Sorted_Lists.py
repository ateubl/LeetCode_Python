# Clear ubuntu terminal with bash line "clear"
import os
os.system('clear')

# As the name implies, this program takes two sorted lists and merges them
# See LeetCode Problem 21: https://leetcode.com/problems/merge-two-sorted-lists/
# This code was written by Andrew Teubl with help from Patrick Gregory during a pairing session on May 2, 2023

def mergeTwoLists(self, list1, list2):
    
    sorted_LL = ListNode()
    p1 = list1
    p2 = list2
    dummy_node = ListNode()
    p_LL = dummy_node
    
    # As long as our node isn't empty, continue
    while p1 != None and p2 != None:
        if p1.val > p2.val:
            p_LL.next = p2
            p2 = p2.next
        else:
            p_LL.next = p1
            p1 = p1.next
            
        p_LL = p_LL.next
    
    # If one of the lists is empty, add on the rest of the list to our sorted list
    if p1:
        p_LL.next = p1
    else:
        p_LL.next = p2
        
    return dummy_node.next

            
        