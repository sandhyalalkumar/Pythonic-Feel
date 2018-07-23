class Node:
    def __init__(self, data=None, nextp=None):
        self.data = data
        self.nextp = nextp

class LinkedList:

    def __init__(self, head):
        self.head = head

    def insertlast(self, data):
        node = Node(data, None)

        current = self.head
        prev = None
        while current:
            prev = current
            current = current.nextp
        prev.nextp = node
    
    def insertfirst(self, data):
        node = Node(data, None)
        node.nextp = self.head
        self.head = node

    def size(self):
        current = self.head
        size = 0
        while current:
            size = size + 1
            current = current.nextp
        return size

    def insert(self, data, index):
        if self.size() < index:
            print "Index should not be beyond size of list"
        if index is 0:
            self.insertfirst(data)
        elif index is self.size():
            self.insertlast(data)
        else:
            current = self.head
            node = Node(data, None)
            prev = None
            while index > 0:
                index = index - 1
                prev = current
                current = current.nextp
            prev.nextp = node
            node.nextp = current

    def printlist(self):
        current = self.head
        while current:
            print current.data
            current = current.nextp

    def get_head(self):
        return self.head


if __name__ == "__main__":

    node = Node(15, None)
    lst = LinkedList(node)
    lst.insertlast(10)
    lst.insertlast(11)
    lst.insertlast(12)
    lst.insertlast(13)
    lst.insertlast(14)
    lst.insertfirst(8)
    lst.printlist()
    print lst.size()
    lst.insert(20, 7)
    lst.printlist()
