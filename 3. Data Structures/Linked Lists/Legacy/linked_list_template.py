class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"

class LinkedList:

    def __init__(self):
       self.head = None
       self.tail = None

    def __str__(self):
        to_print = ""
        curr = self.head

        while curr is not None:
            to_print += str(curr.data) + "->"
            curr = curr.next
        if to_print:
            return '[' + to_print[:-2] + ']'

        return '[]'

    def append_val(self, x):

        if not isinstance(x, Node):
            x = Node(x)

        if self.head == None:
            self.head = x
        else:
            self.tail.next = x

        self.tail = x


    def add_to_start(self, x):
        if not isinstance(x, Node):
            x = Node(x)

        temp = self.head        
        x.next = temp    
        self.head = x




    def search_val(self, x):
 
        current = self.head 
        i = 0
   
        while current != None: 
            if current.data == x: 
                print (f"{x} value found at index {i}")
              
            current = current.next
            i += 1
        print (f"{x} value not found")




    def remove_val_by_index(self, key):

        temp = self.head 
 
        if (temp is not None): 
            if (temp.data == key): 
                self.head = temp.next
                temp = None
                return
  
        while(temp is not None): 
            if temp.data == key: 
                break
            prev = temp 
            temp = temp.next
 
        
        if(temp == None): 
            return
 
        
        prev.next = temp.next
 
        temp = None

    def length(self):
        temp = self.head 
        count = 0 
   
        while (temp): 
            count += 1
            temp = temp.next
        return count 

    def reverse_list_recur(self, current, previous):
        if self.head == None:
            return
        elif current.next == None:
            self.tail = self.head
            current.next = previous
            self.head = current
        else:
            next = current.next
            current.next = previous
            self.reverse_list_recur(next, current)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

my_list = LinkedList()

my_list.append_val(node1)
my_list.append_val(node2)
my_list.append_val(node3)
my_list.append_val(node4)
my_list.append_val(node5)
my_list.append_val(6)
my_list.add_to_start(9)
my_list.search_val(3)

print(my_list)