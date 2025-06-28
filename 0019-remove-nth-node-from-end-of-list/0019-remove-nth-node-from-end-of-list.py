# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        firstHead = head
        cnt = 1
        lastNode = head
        while lastNode.next:
            cnt += 1
            lastNode = lastNode.next
        
        if cnt == 1 == n:
            return None
        elif n == cnt:
            return head.next

        for i in range(cnt - n - 1):
            head = head.next
        
        if head.next is not None:
            if head.next.next is not None:
                head.next = head.next.next
            else:
                head.next = None
        else:
            head.next = None

        print(head.val)
        print(firstHead.val)

        return firstHead