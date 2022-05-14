from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:

        pre_head = ListNode()
        prev = pre_head
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        prev.next = list1 if list1 is not None else list2
        return pre_head.next

    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i = j = 1
        while j < len(nums):
            if nums[j] == nums[j-1]:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1

        return i

    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        i = j = 0
        while j < len(nums):
            if nums[j] != val:
                if i != j:
                    nums[i] = nums[j]
                    nums[j] = val
                i += 1
            j += 1
        return i




