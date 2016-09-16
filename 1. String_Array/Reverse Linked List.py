# Reverse Linked List
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def reverse(self, head):
        if head == None:
            return None
        curt = None
        while head != None:
            temp = head
            head = head.next
            temp.next = curt
            curt = temp
        return curt

    def reverse_recursive(self, head):
        if head == None or head.next == None:
            return head
        newhead = reverse_recursive(head.next)
        head.next.next = head
        head.next = None
        return newhead