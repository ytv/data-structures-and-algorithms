import heap

def heap_maximum(A):
    return A[0];

def heap_extract_max(A, heap_size):
    if heap_size < 1:
        return "Error: heap underflow"
    else:
        max = A[0]
        A[0] = A[heap_size - 1]
        heap_size -= 1
        heap.max_heapify(A, 0, heap_size)
        return max

def print_heap(A, heap_size):
    print A[:heap_size]

def heap_increase_key(A, i, key):
    if key < A[i]:
        return "Error: the new key is smaller than the current key"
    else:
        A[i] = key
        while(i > 0 and A[i] > A[heap.parent(i)]):
            heap.exchange(A, i, heap.parent(i))
            i = heap.parent(i)

def max_heap_insert(A, heap_size, key):
    heap_size += 1
    A[heap_size-1] = -99999
    heap_increase_key(A, heap_size-1, key)


# A = [4,1,3,2,16,9,10,14,8,7]
# heap.build_max_heap(A)
# print A

# heap_extract_max(A, len(A))
# print_heap(A, len(A)-1)

# print heap_increase_key(A, 3, 3)
# heap_increase_key(A, 3, 30)
# print_heap(A, len(A)-1)

# max_heap_insert(A, len(A)-1, 100)
# print A
