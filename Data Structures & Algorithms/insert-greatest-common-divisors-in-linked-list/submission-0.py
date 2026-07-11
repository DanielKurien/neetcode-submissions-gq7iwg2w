# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            divisor = 0

            for i in range(min(curr.val, curr.next.val), 0, -1):
                if curr.val % i == 0 and curr.next.val % i == 0:
                    divisor = i
                    break

            temp = curr.next
            curr.next = ListNode(divisor, temp)

            curr = temp   # or curr = curr.next.next

        return head

