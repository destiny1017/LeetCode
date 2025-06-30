# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, None)

        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val < list2.val:
            head = ListNode(list1.val, None)
            list1 = list1.next
        else:
            head = ListNode(list2.val, None)
            list2 = list2.next
        
        next_node = head
        
        while True:
            if list1 is None:
                next_node.next = list2
                break
            if list2 is None:
                next_node.next = list1
                break
            
            if list1.val < list2.val:
                next_node.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                next_node.next = ListNode(list2.val, None)
                list2 = list2.next
            next_node = next_node.next

        return head
        