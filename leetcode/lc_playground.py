from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + " :: " + str(self.next)


class Solution:

    @staticmethod
    def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> List:
        walk_l1 = l1
        walk_l2 = l2
        l3 = []

        # while walk1 and walk2 are valid
        while walk_l1 and walk_l2:
            if walk_l1.val < walk_l2.val:
                l3.append(walk_l1.val)
                walk_l1 = walk_l1.next

            if walk_l2.val < walk_l1.val:
                l3.append(walk_l2.val)
                walk_l2 = walk_l2.next

            if walk_l2.val == walk_l1.val:
                l3.append(walk_l1.val)
                walk_l1 = walk_l1.next

        # iterate through the remaining items
        while walk_l2:
            l3.append(walk_l2.val)
            walk_l2 = walk_l2.next

        # iterate through the remaining items
        while walk_l1:
            l3.append(walk_l1.val)
            walk_l1 = walk_l1.next

        return l3
        

if __name__ == '__main__':

    l1 = ListNode(1, ListNode(2, ListNode(4, None)))
    l2 = ListNode(1, ListNode(3, ListNode(4, None)))
    s = Solution()

    print(s.merge_two_lists(l1, l2))
