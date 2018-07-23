class Node:
    def __init__(self, data=None, prevp=None, nextp=None):
        self.data = data
        self.prevp = prevp
        self.nextp = nextp

class DoublyLinkedList:

    def __init__(self, head):
        self.head = head

    def insertlast(self, data):
        node = Node(data, None, None)

        current = self.head
        prevnode = None
        while current:
            prevnode = current
            current = current.nextp
        prevnode.nextp = node
        node.prevp = prevnode

    def printlist(self):
        current = self.head
        while current:
            print current.data
            current = current.nextp

    def printreverse(self):
        current = self.head
        prevnode = None
        while current:
            prevnode = current
            current = current.nextp
        print prevnode.data
        while prevnode:
            print prevnode.data
            prevnode = prevnode.prevp

if __name__ == "__main__":

    node = Node(9, None, None)

    dll = DoublyLinkedList(node)
    dll.insertlast(10)
    dll.insertlast(11)
    dll.insertlast(12)
    dll.insertlast(13)
    dll.insertlast(14)
    dll.insertlast(15)
    dll.insertlast(16)
    dll.insertlast(17)


    dll.printlist()

    print ""

    dll.printreverse()