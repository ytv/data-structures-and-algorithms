def partition (A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
        # print A
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

A = [19,6,58,16,13,4,68,1,18]
# print partition(A, 0, len(A) - 1)
# print A

quicksort(A, 0, len(A) - 1)
print A
