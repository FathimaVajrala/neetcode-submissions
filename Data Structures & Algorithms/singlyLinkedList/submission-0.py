
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for _ in range(index):
            curr = curr.next

        return curr.val

    def insertHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head
        self.head = node

        if self.tail is None:
            self.tail = node

        self.size += 1

    def insertTail(self, val: int) -> None:
        node = ListNode(val)

        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False

        if index == 0:
            self.head = self.head.next
            self.size -= 1

            if self.size == 0:
                self.tail = None

            return True

        curr = self.head
        for _ in range(index - 1):
            curr = curr.next

        if curr.next == self.tail:
            self.tail = curr

        curr.next = curr.next.next
        self.size -= 1

        return True

    def getValues(self) -> list:
        values = []
        curr = self.head

        while curr:
            values.append(curr.val)
            curr = curr.next

        return values

