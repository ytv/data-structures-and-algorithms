class Node(object):
    def __init__(self, data, parent = None, left = None, right = None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

def min(A):
    if A:
        min = A[0]
        for elem in A[1:]:
            if min > elem:
                min = elem
        return min

# print min(A)

def max(A):
    if A:
        max = A[0]
        for elem in A[1:]:
            if max < elem:
                max = elem
        return max

# print max(A)

def min_max(A):
    if A:
        j = 1
        if len(A)%2 == 1:
            min, max = A[0], A[0]
        else:
            min, max = A[0], A[1]
            j = 2
        for i in range(j, len(A), 2):
            small, large = A[i], A[i+1]
            if small > large:
                small, large = large, small
            if min > small:
                min = small
            if max < large:
                max = large
        return min, max

# print min_max(A)

def make_nodes(A):
    if A:
        B = []
        for elem in A:
            B.append(Node(elem))
        return B

#####
# builds a binary tree from the bottom up, as a tournament between elements
# where the smallest wins.  Returns the tree root, which is the minimum
#
#        1
#      /   \
#     1      2
#   /  \    / \
#  8   1   2   6
#  \  /\  /\  /\
#  8 3 1 5 2 6 9
#
#     1
#   /   \
#  5     1
#  |    / \
#  5   2   1
#  |  /\  /\
#  5 2 6 9 1
#####
def build_binary_tree_from_bottom(array_of_nodes):
    if array_of_nodes:
        B = []
        j = 0
        if len(array_of_nodes)%2 == 1:
            B.append(array_of_nodes[0])
            j = 1
        for i in range(j, len(array_of_nodes), 2):
            a, b, = array_of_nodes[i], array_of_nodes[i+1]
            min = Node(a.data)
            if a.data > b.data:
                min = Node(b.data)
            a.parent, b.parent = min, min
            min.left, min.right = a, b
            B.append(min)
        if len(B) == 1:
            return B[0]
        return build_binary_tree_from_bottom(B)

def second_smallest(min):
    prior_min = min
    second_min = None
    while prior_min.left and prior_min.right:
        # set pointers
        min_ptr, other_ptr = prior_min.left, prior_min.right
        if prior_min.data == prior_min.right.data:
            min_ptr, other_ptr = prior_min.right, prior_min.left
        # set or recalculate second min
        if not second_min:
            second_min = other_ptr
        elif second_min.data > other_ptr.data:
            second_min = other_ptr
        prior_min = min_ptr
    return second_min

# A = [5,6,9,6,76,28,0,31,13]

# print build_binary_tree_from_bottom(make_nodes(A)).data
# print build_binary_tree_from_bottom(make_nodes(A)).left.data
# print build_binary_tree_from_bottom(make_nodes(A)).left.right.data
# print build_binary_tree_from_bottom(make_nodes(A)).right.data
# print second_smallest(build_binary_tree_from_bottom(make_nodes(A))).data
