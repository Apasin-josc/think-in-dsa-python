class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.value} --> {temp.next.value if temp.next else None}")
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            self.tail = temp
            self.tail.next = None
        self.length -= 1
        return popped_node
                


my_linked_list = LinkedList(13)
my_linked_list.append(20)
my_linked_list.pop()
my_linked_list.pop()
my_linked_list.pop()

my_linked_list.print_list()