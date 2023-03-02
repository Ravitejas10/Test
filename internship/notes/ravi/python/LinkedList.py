class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def display(self):
        temp=self.head
        while(temp):
            print(temp.val)
            temp=temp.next

l1=LinkedList()
l1.head=Node(10)
two=Node(11)
three=Node(12)

l1.head.next=two
two.next=three
l1.display()