# no parent pointer

class Node(object):
    def __init__(self, key, left = None, right = None, succ = None):
        self.key = key
        self.left = left
        self.right = right
        self.succ = succ

    def get_successor(self, parents_stack):
        current = self
        if current.right:
            current = current.right
            while current.left:
                current = current.left
            return current
        else:
            while len(parents_stack) > 0:
                current = parents_stack.pop()
                if current.key > self.key:
                    return current
            return None

    def get_parent(self, T):
        current = T.root
        last = None
        while(current and current != self):
            last = current
            if self.key < current.key:
                current = current.left
            elif self.key > current.key:
                current = current.right
        return last

class BinaryTree(object):
    def __init__(self, root = None):
        self.root = root

    def search(self, key):
        current = self.root
        while(current):
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current
        return current

    def parents_of_search_path(self, key):
        current = self.root
        stack = []
        while(current):
            if key == current.key:
                return stack
            else:
                stack.append(current)
                if key < current.key:
                    current = current.left
                else:
                    current = current.right
        return "Error: node not found"

    def insert(self, key):
        new_node = Node(key)
        if not self.root:
            self.root = new_node
            return None
        current = self.root
        last = None
        while current:
            last = current
            if key <= current.key:
                current = current.left
            else:
                current = current.right
        if key <= last.key:
            last.left = new_node
        else:
            last.right = new_node

    def load(self, array):
        for key in array:
            self.insert(key)

    def inorder_tree_walk_r(self, node):
        if node:
            self.inorder_tree_walk_r(node.left)
            print node.key,
            self.inorder_tree_walk_r(node.right)

    def preorder_tree_walk_r(self, node):
        if node:
            print node.key,
            self.preorder_tree_walk_r(node.left)
            self.preorder_tree_walk_r(node.right)

    def transplant(self, T, node_1, node_2):
        parent = node_1.get_parent(T)
        if parent and (node_1.key <= parent.key):
            parent.left = node_2
        elif parent and node_1.key > parent.key:
            parent.right = node_2
        else:
            T.root = node_2

    def delete(self, T, node):
        # case 1: no children
        if not (node.left or node.right):
            self.transplant(T, node, None)
        # case 2: one child only
        elif node.left and not node.right:
            self.transplant(T, node, node.left)
        elif node.right and not node.left:
            self.transplant(T, node, node.right)
        # case 3: 2 children
        else:
            successor = node.get_successor(self.parents_of_search_path(node.key))
            self.transplant(T, node, successor)
            successor.left = node.left
            # case 3.5: successor is not right child
            if successor != node.right:
                successor.right = node.right

tree = BinaryTree()

# A =  [5,7]
A =  [5,3,7,4,1,8,9,2,6]
tree.load(A)

# tree.insert(5)
# tree.insert(7)
# tree.insert(3)
# tree.insert(1)

tree.preorder_tree_walk_r(tree.root)

# print
# print tree.search(9)
# print
# print tree.parents_of_search_path(9)

print
tree.inorder_tree_walk_r(tree.root)

# print tree.root.left.left.right.key

# print
# print tree.search(5).successor(tree.parents_of_search_path(tree.search(5).key)).key

# print
# print tree.search(9).get_parent(tree).key

# tree.transplant(tree, tree.search(5), tree.search(9))

tree.delete(tree, tree.search(7))

print
tree.preorder_tree_walk_r(tree.root)
