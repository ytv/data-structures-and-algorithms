# Input: sequence of n numbers <a1, a2, ..., an>
# Output: reordering <a1', a2', ... , an'> in sorted order


def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1

        while(j >= 0 and A[j] > key):
            A[j+1] = A[j]
            j -= 1

        A[j+1] = key

# A = [19,6,58,16,13,4,68,1,-9]
# print insertion_sort(A)
# print A
