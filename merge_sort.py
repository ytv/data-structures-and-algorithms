# Input: sequence of n numbers <a1, a2, ..., an>
# Output: reordering <a1', a2', ... , an'> in sorted order

import math

def merge(A, p, q, r):

    # Create a copy of the left-sided sorted subarray
    left = []
    for i in range(p, q+1):
        left.append(A[i])

    # Create a copy of the right-sided sorted subarray
    right = []
    for i in range(q+1, r+1):
        right.append(A[i])

    # Merge onto array a
    i, j = 0, 0
    k = p
    l_len = len(left)
    r_len = len(right)

    while(k <= r):
        if i < l_len and j < r_len:
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        elif i >= l_len and j < r_len:
            while(j < r_len):
                A[k] = right[j]
                j += 1
                k += 1
            break
        else:
            while(i < l_len):
                A[k] = left[i]
                i += 1
                k += 1
            break

def merge_sort(A, p, r):
    if p < r:
        # Calculate the midpoint of subarray
        q = int(math.floor((p+r)/2))

        # merge_sort left-side of subarray
        merge_sort(A, p, q)

        # merge_sort right-side of subarray
        merge_sort(A, q+1, r)

        # Merge the now sorted left and right sides
        merge(A, p, q, r)

# A = [19,6,58,16,13,4,68,1,-9]
# print merge_sort(A, 0, len(A)-1)
# print A
