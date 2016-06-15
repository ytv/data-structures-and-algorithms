import random

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def randomized_partition(A, p, r):
    q = random.randint(p, r)
    A[q], A[r] = A[r], A[q]
    return partition(A, p, r)

def randomized_select(A, p, r, i):
    if p == r:
        return A[p]
    q = randomized_partition(A, p, r)
    # print q, A
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q - 1, i)
    else:
        return randomized_select(A, q + 1, r, i - k)

def randomized_select_iter(A, p, r, i):
    while True:
        if p == r:
            return A[p]
        q = randomized_partition(A, p, r)
        # print q, A
        k = q - p + 1
        if i == k:
            return A[q]
        if i < k:
            r = q - 1
        else:
            p = q + 1
            i = i - k

array = [19,6,58,16,13,4,68,1,18]
# print randomized_partition(A, 0, len(A)-1)
# print A
# print randomized_select(array, 0, len(array) - 1, 9)
print randomized_select_iter(array, 0, len(array) - 1, 9)
