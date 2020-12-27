#do it by your own this is the link list both insertion operations

# linked list : insertion deletion and traversal
# traversal
# create a node
class Node:
    def __init__(self, data):   # this is a single node which contain data and reference
        self.data = data
        self.ref = None
# now create a empty linked list
class linkedlist:
    def __init__(self):
        self.head = None
    def printll(self):
        if self.head == None:
            print("Linked list is empty")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.ref
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

l = linkedlist()
l.add_begin(10)
l.add_begin(40)
l.add_end(20)
l.add_end(80)
print(l.printll())