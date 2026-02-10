class Node:
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node

    def delete(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node == self.head:
                    self.head = current_node.next_node
                    self.head.prev_node = None
                elif current_node == self.tail:
                    self.tail = current_node.prev_node
                    self.tail.next_node = None
                else:
                    current_node.prev_node.next_node = current_node.next_node
                    current_node.next_node.prev_node = current_node.prev_node
                break
            current_node = current_node.next_node

    def print_forward(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node
        print()

    def print_backward(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev_node
        print()


dll = DoublyLinkedList()
dll.append("A")
dll.append("B")
dll.append("C")
print("(print_forward):")
dll.print_forward()
print("(print_backward):")
dll.print_backward()
dll.prepend("X")
print("(print_forward)(prepend)(X):")
dll.print_forward()
print("(print_backward)(prepend):")
dll.print_backward()
dll.delete("B")
print("(print_forward)(delete)(B):")
dll.print_forward()
print("(print_backward)(delete):")
dll.print_backward()