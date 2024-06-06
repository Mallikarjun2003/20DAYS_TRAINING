class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.prev =None
        self.next = None
class Dll:
        def __init__(self) -> None:
             self.head = None
             self.tail = None
        def addback(self,data):
            if not self.head:
                  self.head = self.tail = Node(data)
            else:
                 new_node = Node(data)
                 new_node.prev = self.tail
                 self.tail.next = new_node
                 self.tail = new_node
        def addfront(self,data):
            if not self.head:
                  self.head = self.tail = Node(data)
            else:
                new_node = Node(data)
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        def display(self):
             t= self.head
             while t:
                  print(t.data,end="->")
                  t =t.next
        def linear_search(self,data):
             t =self.head
             found = True
             while t:
                if t.data == data :
                       print("Found")
                       found = False
                t = t.next
                
             if found:
                  print("Not found")
        def lin_search(self,data):
            head = self.head
            tail = self.tail
            found = False
            while head != tail and  head != tail.next:
                if head.data == data or tail.data == data:
                      found = True
                head = head.next
                tail = tail.prev
            if not found and head.data != data:
                 print("Not Found")
            else:
                 print("Found")
        def length(self):
            head = self.head
            tail = self.tail
            count =0
            while head != tail and head != tail.next:
                 count +=2
                 head = head.next
                 tail = tail.prev
            if head != tail:
                 count +=1
            print("Even") if count%2 ==0 else print("Odd")
        def checkpal(self):
            head = self.head
            tail = self.tail
            while  head!= tail:
                if head.data != tail.data:
                      print("Not palindrome")
                      return
                head = head.next
                tail = tail.next
            print("palindrome")
                      
dll = Dll()
inp = int(input())
while inp != -1:
    if inp%2 :
          dll.addback(inp)
    else:
         dll.addfront(inp)
    inp = int(input())
dll.display()         
dll.linear_search(5) 
dll.lin_search(34)
dll.length()             
dll.checkpal()            
                  
                  