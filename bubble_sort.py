# Input: sequence of n numbers <a1, a2, ..., an>
# Output: reordering <a1', a2', ... , an'> in sorted order

def bubble_sort(A):
    for i in range(len(A)-1, 0, -1):
        for j in range(0, i):
            if A[j] > A[j+1]:
                t = A[j+1]
                A[j+1] = A[j]
                A[j] = t

# A = [19,6,58,16,13,4,68,1,-9]
# bubble_sort(A)
# print A
