class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) # starting point for the merged list
        current = dummy # initializes a pointer to track the end of the merged list.

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Append any remaining elements from either list
        current.next = list1 if list1 else list2

        return dummy.next