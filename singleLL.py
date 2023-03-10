#creating a node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

#print all the elements
    def print_LL(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->",end=" ")
                n = n.next

# adding an element at the begining
    def add_begin(self,data):
        new_node = Node(data)
        new_node.next= self.head
        self.head = new_node

#adding an element at the end
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

#adding an element after a given value
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n = n.next
        if n is None:
            print("node is not presesnt in LL")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

#adding an element before a given value
    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is empty!")
            return
        if self.head.data==x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            if n.next.data==x:
                break
            n = n.next        
        if n.next is None:
            print("Node is not found!")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node     

#delete the begining element
    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty can't delete!")
        else:
            self.head=self.head.next

#delete the last element
    def delete_last(self):
        if self.head is None:
            print("the linked list is empty..!")
        elif self.head.next is None:
            self.head=None

        else:
            n=self.head
            while n.next.next is not None:
                n=n.next
            n.next=None

#delete an element from LL
    def delete_by_value(self,value):
        if self.head is None:
            print ("LL is empty..!")
        elif self.head.data==value:
            self.head=self.head.next
        else:
            n=self.head
            while n.next is not None:
                if value==n.next.data:
                    break
                n=n.next
            if n.next is None:
                print("the value is not found")
            else:
                n.next=n.next.next





ll1=LinkedList()
ll1.add_begin(10)
ll1.add_end(8)
ll1.add_end(12)
ll1.add_after(8,1)
ll1.add_before(10,12)
ll1.add_before(12,111)
ll1.delete_by_value(12)
ll1.print_LL()


