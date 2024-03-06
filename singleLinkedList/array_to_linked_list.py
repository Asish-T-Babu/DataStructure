a=[1,2,3,4,5]

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
    
    def array_to_linked_list(self,array):
        new_node = None
        for i in array:
            node = Node(i)
            if not new_node:
                self.head = node
                new_node = node
            else:
                new_node.next = node
                new_node = node
    
    def traverse_sll(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next

sll = SLL()
sll.array_to_linked_list(a)
sll.traverse_sll()