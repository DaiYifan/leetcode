# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#注意链表的定义方式，通过定义节点 如上所示，定义一个val和next就行
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        r = result
        t = 0
        while(l1 or l2 or t):
            if l1:
                x = l1.val
            else:
                x = 0
            if l2:
                y = l2.val
            else:
                y = 0
            r.next = ListNode((x+y+t)%10)
            
            if x + y + t >= 10:
                t = 1
            else:
                t = 0
            if l1 != None:l1 = l1.next
            if l2 != None:l2 = l2.next
            r = r.next
            
        return result.next
    
            
            
        