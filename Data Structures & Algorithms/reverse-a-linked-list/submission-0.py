# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        while head:
            # get next node 
            next_node_to_iterate = head.next 
            # link node.next to prev node 
            head.next = prev 
            # iterate on next node 
            prev = head 
            head = next_node_to_iterate

        return prev
        