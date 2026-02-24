class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def print_structure(self):
        self._print_tree(self.root)

    def _print_tree(self, current_node):
        if current_node:
            print(current_node.data)
            self._print_tree(current_node.left)
            self._print_tree(current_node.right)


node_f = Node("F")
node_g = Node("G")
node_c = Node("C", node_f, node_g)

node_d = Node("D")
node_e = Node("E")
node_b = Node("B", node_d, node_e)

node_a = Node("A", node_b, node_c)
my_binary_tree = BinaryTree(node_a)
my_binary_tree.print_structure()