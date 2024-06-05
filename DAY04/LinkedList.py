class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
class sll:
    def __init__(self,data) -> None:
        self.head = Node(data)
    def display(self):
        t = self.head
        while (t!=None):
            print(t.data,end="->")
            t = t.next
        print()
    def add_back(self,data):
        t = self.head
        while t.next!= None:
            t = t.next
        t.next = Node(data)
    def add_front(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
l1 = sll(10)
l2 = sll(50)
l1.add_back(12)
l1.add_back(14)
l1.add_back(16)
l1.add_back(18)
l1.add_back(20)
l1.display()
l2.add_front(22)
l2.add_front(2243)
l2.add_back(12)
l2.add_back(14)
l2.add_back(16)
l2.add_back(18)
l2.add_back(20)
l2.display()