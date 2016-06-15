from random import randint

def random_number_list(n, limit = 10, nonNeg = True):
    i = 0
    A = []
    if nonNeg == True:
        while i < n:
            A.append(randint(0, limit))
            i += 1
    else:
        while i < n:
            A.append(randint(-1*limit, limit))
            i += 1
    return A

# print random_number_list(10, 100)
# print random_number_list(10, 100, False)
