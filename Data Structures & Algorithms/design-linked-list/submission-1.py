# i am initialing a class ListNode as a doubly linked link as i have two pointers (next and prev)
# usage of __init__ method and self object constructor (more to study)
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
class MyLinkedList:

    def __init__(self):
        # using 2 dummy nodes(left and right) and our main LL is in the middle of these two 
        # a method to bypass some edges as now every insertion and deletion operation is of only one type ( in between, at ith index)
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
    

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.right and index == 0:
            return curr.val
        return -1


    def addAtHead(self, val: int) -> None:
        node, next, prev = ListNode(val), self.left.next, self.left
        next.prev = node
        prev.next = node
        node.next = next
        node.prev = prev
        

    def addAtTail(self, val: int) -> None:
        node, next, prev = ListNode(val), self.right, self.right.prev
        next.prev = node
        prev.next = node 
        node.next = next
        node.prev = prev

        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            node, next, prev = ListNode(val), curr, curr.prev
            next.prev = node
            prev.next = node
            node.next = next
            node.prev = prev
            
        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0 and curr != self.right:
            next , prev = curr.next, curr.prev
            next.prev = prev
            prev.next = next
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)