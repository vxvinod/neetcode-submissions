# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # iterate till none if none reached return false else
        # store the next in list and check if it is again present return true

        current = head
        next_list = []
        while current is not None:
            #prev = current
            if current.next in next_list:
                return True
            next_list.append(current.next)
            current = current.next


        


        return False