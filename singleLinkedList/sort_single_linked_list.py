a=[1,4,3,2,5]

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
    
    def sort_linked_list(self):
        node = self.head
        if node:
            swapped = True
            while swapped:
                swapped = False
                node= self.head
                while node.next:
                    if node.data > node.next.data:
                        node.data, node.next.data = node.next.data, node.data
                        swapped = True
                    node= node.next

    
    def traverse_sll(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next

sll = SLL()
sll.array_to_linked_list(a)
sll.traverse_sll()
print('\n')
sll.sort_linked_list()
sll.traverse_sll()