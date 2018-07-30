# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return []
        if head.next == None:
            return [head.val]
        temp = head
        L = 0
        while temp:
            L = L + 1
            temp = temp.next

        mid = L/2

        for _ in xrange(0, mid):
            head = head.next

        results = []
        while head:
            results.append(head.val)
            head = head.next
        return results


if __name__ == "__main__":

    s = Solution()

    head = ListNode(10)
    head.next = ListNode(20)
    head.next.next = ListNode(15)
    head.next.next.next = ListNode(14)
    #head.next.next.next.next = ListNode(17)
    #head.next.next.next.next.next = ListNode(40)

    print s.middleNode(head)

