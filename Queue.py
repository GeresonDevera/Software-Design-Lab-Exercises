class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
#class to present queue

class JQueue:

    def __init__(self):
        self.front = self.rear = None

    def Empty(self):
        return self.front == None


    def EQueue(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def DQueue(self):

        if self.Empty():
            return
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None

if __name__ == '__main__':
    q = JQueue()
    q.EQueue(11)
    q.EQueue(88)
    q.DQueue()
    q.DQueue()
    q.EQueue(33)
    q.EQueue(44)
    q.EQueue(77)
    q.DQueue()
    print("The Queue in Front " + str(q.front.data))
    print("The Queue in Rear " + str(q.rear.data))