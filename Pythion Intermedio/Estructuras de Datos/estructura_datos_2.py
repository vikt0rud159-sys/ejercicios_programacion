class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class DoubleEndedQueue:
    def __init__(self, head):
        self.head = head
        self.tail = head

    def print_structure(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push_left(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def push_right(self, new_node):
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head is not None:
            self.head = self.head.next

    def pop_right(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head is not None:
            current_node = self.head
            while current_node.next is not self.tail:
                current_node = current_node.next
            current_node.next = None
            self.tail = current_node


first_node = Node("A")
my_dequeue = DoubleEndedQueue(first_node)
second_node = Node("B")
my_dequeue.push_right(second_node)
third_node = Node("C")
my_dequeue.push_left(third_node)

my_dequeue.print_structure()
print("\n[POP LEFT]")
my_dequeue.pop_left()
my_dequeue.print_structure()
print("\n[POP RIGHT]")
my_dequeue.pop_right()
my_dequeue.print_structure()