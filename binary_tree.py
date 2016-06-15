def inorder_tree_walk_r(node):
    if node.left:
        inorder_tree_walk_r(node.left)
    print node.data,
    if node.right:
        inorder_tree_walk_r(node.right)

# inorder_tree_walk_r(tree.root)

def preorder_tree_walk_r(node):
    print node.data,
    if node.left:
        preorder_tree_walk_r(node.left)
    if node.right:
        preorder_tree_walk_r(node.right)

# preorder_tree_walk_r(tree.root)

def postorder_tree_walk_r(node):
    if node.left:
        postorder_tree_walk_r(node.left)
    if node.right:
        postorder_tree_walk_r(node.right)
    print node.data,

# postorder_tree_walk_r(tree.root)

def preorder_tree_walk_nr_stack(node):
    stack = []
    current = node
    while True:
        print current.data,
        if current.right:
            stack.append(current.right)
        if current.left:
            current = current.left
        elif len(stack) > 0:
            current = stack.pop()
        else:
            break

# preorder_tree_walk_nr_stack(tree.root)

def inorder_tree_walk_nr_stack_1(node):
    stack = []
    current = node
    from_stack = False

    while True:
        if not from_stack:
            stack.append(current)
            if current.left:
                current = current.left
                from_stack = False
            else:
                current = stack.pop()
                from_stack = True
        else:
            print current.data,
            if current.right:
                current = current.right
                from_stack = False
            elif len(stack) > 0:
                current = stack.pop()
                from_stack = True
            else:
                break

def inorder_tree_walk_nr_stack_2(node):
    current = node
    stack = []
    while current or len(stack) > 0:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            print current.data,
            current = current.right

# inorder_tree_walk_nr_stack_1(tree.root)
# inorder_tree_walk_nr_stack_2(tree.root)

def inorder_tree_walk_nr(root):
    current = root
    previous = None

    while(current):
        if previous == current.parent or (current == root and previous == None):
            previous = current
            if current.left:
                current = current.left
            else:
                print current.data,
                if current.right:
                    current = current.right
                else:
                    current = current.parent
        elif previous == current.left:
            previous = current
            print current.data,
            if current.right:
                current = current.right
            else:
                current = current.parent
        else:
            previous = current
            current = current.parent

# inorder_tree_walk_nr(tree.root)

def tree_minimum(node):
    current = node
    while current.left:
        current = current.left
    print current.data

def tree_minimum_r(node):
    current = node
    if current.left:
        current = tree_minimum_r(current.left)
    return current

def tree_maximum(node):
    current = node
    while current.right:
        current = current.right
    print current.data

def tree_maximum_r(node):
    current = node
    if current.right:
        current = tree_maximum_r(current.right)
    return current

# tree_minimum(tree.root)
# print tree_minimum_r(tree.root).data
# tree_maximum(tree.root)
# print tree_maximum_r(tree.root).data

def tree_successor(node):
    current = node
    if current.right:
        current = current.right
        while current.left:
            current = current.left
        return current
    current = current.parent
    while current and current.data < node.data:
        current = current.parent
    return current

def tree_predecessor(node):
    current = node
    if current.left:
        current = current.left
        while current.right:
            current = current.right
        return current
    current = current.parent
    while current and current.data > node.data:
        current = current.parent
    return current

# B = [15,6,18,3,7,17,20,2,4,13,9]
# treeB = BinaryTree()
# load_tree(treeB, B)
#
# print tree_successor(treeB.root.left.right.right).data
# print tree_successor(treeB.root.right.right).data
# print treeB.root.left.right.right.left.data.
# print tree_predecessor(treeB.root.left.right.right.left).data


class Node(object):
    def __init__(self, data, parent = None, left = None, right = None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

    def set_parent(self, new_node):
        self.parent = new_node

    def set_left(self, new_node):
        self.left = new_node

    def set_right(self, new_node):
        self.right = new_node

class BinaryTree(object):
    def __init__(self, root = None):
        self.root = root

    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
        else:
            current = self.root
            while(True):
                if data < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.set_left(new_node)
                        new_node.set_parent(current)
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.set_right(new_node)
                        new_node.set_parent(current)
                        break

    def insert_r(self, data, current, last = None):
        if current:
            if data <= current.data:
                self.insert_r(data, current.left, current)
            else:
                self.insert_r(data, current.right, current)
        else:
            new_node = Node(data)
            new_node.parent = last
            if data <= last.data:
                last.left = new_node
            else:
                last.right = new_node

    # replaces subtree rooted at node_s with subtree rooted at node_t
    def transplant(self, tree, node_s, node_t):
        if not node_s.parent:
            tree.root = node_t
        elif node_s.parent.left == node_s:
            node_s.parent.set_left(node_t)
        else:
            node_s.parent.set_right(node_t)
        if node_t:
            node_t.set_parent(node_s.parent)

    def delete(self, tree, node_s):
        if not(node_s.left or node_s.right):
            self.transplant(tree, node_s, None)
        if node_s.left and not node_s.right:
            self.transplant(tree, node_s, node_s.left)
        elif not node_s.left and node_s.right:
            self.transplant(tree, node_s, node_s.right)

        # node_s has 2 children
        # if node_s's successor is node_s.right
        else:
            succ = tree_successor(node_s)
            if succ == node_s.right:
                self.transplant(tree, node_s, succ)
                succ.set_left(node_s.left)
                node_s.left.set_parent(succ)
            # else node_s's successor is not node_s.right
            else:
                succ_right = None
                succ_parent = succ.parent
                if succ.right:
                    succ_right = succ.right
                else:
                    transplant(tree, node_s, succ)
                    succ.set_right(node_s.right)
                    succ.right.set_parent(succ)
                    if node_s.left:
                        succ.set_left(node_s.left)
                        succ.left.set_parent(succ)
                    succ_right.set_parent(succ_parent)
                    succ_parent.set_left(succ_right)


    def search_1(self, key):
        current = self.root
        while True:
            if current.data == key:
                return current.data
            elif current.data > key:
                if current.left:
                    current = current.left
                else:
                    return "Error: not found"
            else:
                if current.right:
                    current = current.right
                else:
                    return "Error: not found"

    def search_2(self, key):
        current = self.root
        while current and current.data != key:
            if current.data > key:
                current = current.left
            else:
                current = current.right
        return current

def load_tree(T, A):
    for each in A:
        T.insert(each)

# A = [6,5,7,2,5,8,6.5,9]
# tree = BinaryTree()
# load_tree(tree, A)

B = [1,3,2,5,4,6]
tree_2 = BinaryTree()
load_tree(tree_2, B)

preorder_tree_walk_r(tree_2.root)
tree_2.delete(tree_2, tree_2.root.right.right)
print
preorder_tree_walk_r(tree_2.root)


# tree.insert_r(11, tree.root)
# inorder_tree_walk_nr(tree.root)
# print
# preorder_tree_walk_r(tree.root)

# preorder_tree_walk_nr_stack(tree.root)
# print
# inorder_tree_walk_nr(tree.root)
# tree.delete(tree, tree.root.right)
# print
# print
# preorder_tree_walk_nr_stack(tree.root)
# print
# inorder_tree_walk_nr(tree.root)

# print tree.search_1(6.5)
# print tree.search_2(6.6)

# print tree.root.data
# print tree.root.left.data
# print tree.root.left.left.data
# print tree.root.left.right.data
# print tree.root.right.data
# print tree.root.right.right.data
