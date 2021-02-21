class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """迭代"""
        pre = None
        cur = head
        while cur:
            temp = cur.next   # 先把原来cur.next位置存起来
            cur.next = pre  # 指向pre
            pre = cur  # pre-step
            cur = temp  # back
        return pre
