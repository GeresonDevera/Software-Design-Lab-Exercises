class Node:

    # Class to create nodes of linked list
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def empty(self):
        if self.head == None:
            return True
        else:
            return False

    def rhey(self, data):

        if self.head == None:
            self.head = Node(data)

        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def gereson(self):

        if self.empty():
            return None

        else:

            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    def ben(self):

        if self.empty():
            return None

        else:
            return self.head.data

    # this will show or print the data
    def display(self):

        iternode = self.head
        if self.empty():
            print("Stack Underflow")

        else:

            while (iternode != None):
                print(iternode.data, "-", end=" ")
                iternode = iternode.next
            return



JStack = Stack()

JStack.rhey(1)
JStack.rhey(5)
JStack.rhey(10)
JStack.rhey(20)

JStack.display()


print("\nThe Top element is ", JStack.ben())


JStack.gereson()
JStack.gereson()


JStack.display()


print("\nThe Below element is ", JStack.ben())