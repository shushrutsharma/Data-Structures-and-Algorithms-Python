import time

class Node:

    def __init__(self, data=None):
        '''initialize node with data and next pointer'''
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        '''initialize queue with head and tail'''
        print("Queue created")
        self.head = None
        self.tail = None

    def add(self, x):
        '''append x to the tail of the queue'''
        if not isinstance(x, Node):
            x = Node(x)
        print(f"Appending {x.data} to the tail of the Queue")
        if self.is_empty():
            self.head = x
        else:
            self.tail.next = x
        self.tail = x

    def remove(self):
        '''remove and return the node at head of the queue'''
        if not self.is_empty():
            print(f"Removing node at head of the Queue")
            curr = self.head
            self.head = self.head.next
            curr.next = None
            return curr.data
        else:
            return "Queue is empty"

    def is_empty(self):
        '''return True if queue is empty, else return false'''
        return self.head == None

    def peek(self):
        '''look at the node at head of the queue'''
        if not self.is_empty():
            return self.head.data

    def __str__(self):
        print("Printing Queue state...")
        to_print = ""
        curr = self.head
        while curr is not None:
            to_print += str(curr.data) + "->"
            curr = curr.next
        if to_print:
            if len(to_print) > 4:
                print("Head", " "*(len(to_print)-9),"Tail")
                print(" |", " "*(len(to_print)-6), "|")
                print(" V", " "*(len(to_print)-6), "V")
                return "[" + to_print[:-2] + "]"
            else:
                print("Head & Tail")
                print(" |")
                print(" V")
                return "[" + to_print[:-2] + "]"
        return "[]"

my_queue = Queue()
print("Checking if Queue is empty:", my_queue.is_empty())
time.sleep(2)
my_queue.add(1)
print(my_queue)
time.sleep(2)
my_queue.add(2)
my_queue.add(3)
print(my_queue)
time.sleep(2)
my_queue.add(4)
my_queue.add(5)
time.sleep(2)
print("Checking node at head of Queue:", my_queue.peek())
time.sleep(2)
my_queue.add(6)
print(my_queue)
time.sleep(2)
print(my_queue.remove())
time.sleep(2)
print(my_queue.remove())
time.sleep(2)
print(my_queue)
time.sleep(2)
my_queue.add(4)
time.sleep(2)
print(my_queue)
