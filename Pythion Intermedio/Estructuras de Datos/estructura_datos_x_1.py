class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class Queue:
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        else:
            removed_node = self.head
            self.head = self.head.next_node
            if self.head is None:
                self.tail = None
            return removed_node.data

    def print_all(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node


q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.print_all()
print(f"\n[DEQUEUE] = {q.dequeue()}")
q.print_all()