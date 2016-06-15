# Max-heap property: for each node i (except for root node), A[parent(i)] > A[i]
import math

def parent(i):
    return int(math.floor((i-1)/2))

def left(i):
    return 2*(i+1)-1

def right(i):
    return 2*(i+1)

def exchange(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

# Max-heapify: assumes binary trees rooted at Left(i) and Right(i) are Max-heaps,
# but A[i] may be smaller than its children.  Lets value of A[i] float down
def max_heapify(A, i, heap_size):
    l = left(i)
    r = right(i)
    largest = i

    if l < heap_size and A[l] > A[i]:
        largest = l
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        exchange(A, i, largest)
        max_heapify(A, largest, heap_size)

# build_max_heap runs Max-heapify from the last of the second to bottom element
# to the root element
def build_max_heap(A):
    for i in range(parent(len(A)-1), -1, -1):
        max_heapify(A, i, len(A))


def heapsort(A):
    build_max_heap(A)
    heap_size = len(A)

    for i in range(0, len(A)):
        exchange(A, 0, heap_size-1)
        heap_size -= 1
        max_heapify(A, 0, heap_size)

# A = [16,4,10,14,7,9,3,2,8,1]
# max_heapify(A,1,len(A))
# print A

# A = [4,1,3,2,16,9,10,14,8,7]
# build_max_heap(A)
# print A

# A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
# heapsort(A)
# print A
