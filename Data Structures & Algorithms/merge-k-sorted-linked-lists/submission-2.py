# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        def mergeTwoLists(l1, l2):
            dummy = ListNode()
            curr = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 if l1 else l2 
            return dummy.next

        while len(lists) > 1:
            merged = list()
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    merged.append(mergeTwoLists(lists[i], lists[i+1]))
                else:
                    merged.append(lists[i])
            lists = merged
        return lists[0] if lists else None