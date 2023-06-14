from addTwoLists import ListNode


class RemovLinkDup:
    def removeDuplFLinkList(self, head: ListNode)-> ListNode:
        curr= head
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr.next= curr.next.next
            curr= curr.next
        return  head

if __name__=='__main__':
    c=RemovLinkDup()
    print(c.removeDuplFLinkList(11,11,7,10))