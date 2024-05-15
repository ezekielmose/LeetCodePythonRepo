class ListNode:
    pass


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = tail = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = sum // 10
            tail.next = ListNode(sum % 10)
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next

if __name__ == '__main__':
    l1=[3,5,7]
    l2=[3,5,6]
    addTwoNumbers(l1, l2)

