# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sorted_node = Optional[ListNode]
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        merged_node = ListNode()
        if list1.val <= list2.val:
            merged_node.val = list1.val
            list1 = list1.next
        else:
            merged_node.val = list2.val
            list2 = list2.next
        
        self.exec_merge(merged_node, list1, list2)
        
        return merged_node
    
    def exec_merge(self, node, list1, list2):
        if list1 is None and list2 is None:
            return

        less_node = self.compare_node(list1, list2)
        node.next = ListNode(val=less_node.val)

        if less_node == list1:
            list1 = list1.next
        elif less_node == list2:
            list2 = list2.next
        
        self.exec_merge(node.next, list1, list2)
    
    def compare_node(self, node1, node2):
        if node1 is None:
            return node2
        if node2 is None:
            return node1
        
        if node1.val <= node2.val:
            return node1
        else:
            return node2