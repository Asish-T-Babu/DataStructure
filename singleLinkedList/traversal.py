class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head:
            node =self.head
            while node:
                print(node.data, end=' ')
                node = node.next
        else:
            print('Empty Single Linked List')

sll = SLL()
node1 = node(5)
sll.head = node1
node2 = node(6)
node1.next = node2
node3 = node(7)
node2.next = node3
sll.traversal()