class Solution:
    def mergeTwoLists(self, list1, list2):
        result = ListNode()
        tail = result
        l1_curr = list1
        l2_curr = list2

        while l1_curr is not None and l2_curr is not None:
            if l1_curr.val <= l2_curr.val:
                tail.next = ListNode(l1_curr.val)
                l1_curr = l1_curr.next
            else:
                tail.next = ListNode(l2_curr.val)
                l2_curr = l2_curr.next
            tail = tail.next

        # attach whatever's left of the non-exhausted list directly —
        # no need to copy node-by-node, just link the remaining chain
        while l1_curr is not None:
            tail.next = ListNode(l1_curr.val)
            l1_curr = l1_curr.next
            tail = tail.next

        while l2_curr is not None:
            tail.next = ListNode(l2_curr.val)
            l2_curr = l2_curr.next
            tail = tail.next

        return result.next   # skip the dummy node