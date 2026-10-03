# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        test = ListNode(0)
        test.next = head

        # count total node
        # find the deleted node
        # assign last node .next.next skip the node to be deleted.

        count = 0
        current = head
        while current is not None:
            count +=1
            current = current.next
        print(count)

        before_pos = count - n
        prev = test
        for i in range(before_pos):
            prev = prev.next 
        
        prev.next = prev.next.next

        return test.next