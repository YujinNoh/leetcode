# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        ans1, ans2 = 0, 0
        i, j = 0, 0
        
        while temp1:
            ans1 += temp1.val * (10 ** i)
            temp1 = temp1.next
            i += 1
        
        while temp2:
            ans2 += temp2.val * (10 ** j)
            temp2 = temp2.next
            j += 1
        
        total = ans1 + ans2
        
        for i, val in enumerate(str(total)[::-1]):
            globals()['node{}'.format(i)] = ListNode(val = int(val), next = None)
        
        
        for k in range(len(str(total))-1):
            globals()['node{}'.format(k)].next = globals()['node{}'.format(k + 1)]
            print(globals()['node{}'.format(k)])
        
        
        return node0
