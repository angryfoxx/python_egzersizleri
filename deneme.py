class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addFront(self, value):
        newNode = Node(value)

        newNode.nextNode = self.head

        self.head = newNode

    def addRear(self, value):
        tmp = self.head
        while tmp.nextNode:
            tmp = tmp.nextNode

        newNode = Node(value)

        tmp.nextNode = newNode

    def insert_with_sort(self, value):
        tmp = self.head

        if tmp.value >= value:
            self.addFront(value)
            return

        lastVal = self.head
        while lastVal.nextNode:
            lastVal = lastVal.nextNode

        if lastVal.value <= value:
            self.addRear(value)
            return

        while tmp.nextNode.value <= value:
            tmp = tmp.nextNode

        newNode = Node(value)

        newNode.nextNode = tmp.nextNode

        tmp.nextNode = newNode

    def delRear(self):
        tmp = self.head
        while tmp.nextNode.nextNode:
            tmp = tmp.nextNode

        tmp.nextNode = None

    def delFront(self, value):
        tmp = self.head
        if tmp.value == value:
            self.head = tmp.nextNode
            return

        while tmp.nextNode.value != value:
            tmp = tmp.nextNode

        tmp.nextNode = tmp.nextNode.nextNode

    def printLinkedlist(self):
        tmp = self.head
        while tmp:
            print(tmp.value)
            tmp = tmp.nextNode

link = LinkedList()
link.addFront(15)
link.addFront(13)
link.addFront(12)
link.addFront(11)
link.insert_with_sort(5)
link.insert_with_sort(14)
link.insert_with_sort(9)
link.insert_with_sort(20)
link.insert_with_sort(18)
link.insert_with_sort(2)
link.insert_with_sort(2)
link.insert_with_sort(1.2)
link.printLinkedlist()
"""print("*-")
link.delete(11)
link.delete(15)
link.printLinkedlist()"""
"""link.pop()
link.pop()
print("*-")
link.printLinkedlist()"""