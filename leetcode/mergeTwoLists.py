# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        """"""
        return str(self.val) + " :: " + str(self.next)

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        walk_l1 = l1
        walk_l2 = l2
        l3 = ListNode()
        front = l3

        # while walk1 and walk2 are valid
        while walk_l1 and walk_l2:
            if walk_l1.val < walk_l2.val:
                l3.next = walk_l1
                walk_l1 = walk_l1.next
            else:
                l3.next = walk_l2
                walk_l2 = walk_l2.next
            l3 = l3.next

        l3.next = walk_l1 or walk_l2

        return front.next


if __name__ == '__main__':

    l1 = ListNode(1, ListNode(2, ListNode(4, None)))
    l2 = ListNode(1, ListNode(3, ListNode(4, None)))
    s = Solution()

    print(str(s.mergeTwoLists(l1, l2)))