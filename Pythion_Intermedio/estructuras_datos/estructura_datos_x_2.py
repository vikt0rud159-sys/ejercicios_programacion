class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def delete(self, data):
        current_node = self.head
        if current_node is not None:
            if current_node.data == data:
                self.head = current_node.next_node
            else:
                while current_node.next_node is not None:
                    if current_node.next_node.data == data:
                        current_node.next_node = current_node.next_node.next_node
                        break
                    current_node = current_node.next_node

    def print_all(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node


ll = LinkedList()
ll.insert_front(10)
ll.insert_front(20)
ll.insert_back(30)
ll.print_all()
print("\n[DELETE]")
ll.delete(10)
ll.print_all()