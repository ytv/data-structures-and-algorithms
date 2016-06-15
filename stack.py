def s_top(S):
    return len(S) - 1

def stack_empty(S):
    if len(S) == 0:
        return True
    else:
        return False

# S = []
# print stack_empty(S)
#
# S = [1,2,3]
# print stack_empty(S)

def push(S, x):
    S.append(x)

# S = [1,2,3]
# push(S, 4)
# print S

def pop(S):
    if stack_empty(S):
        return "Error: underflow"
    else:
        x = S[len(S) - 1]
        del S[len(S) - 1]
        return x

# S = [1,2,3,4]
# print pop(S)
# S = []
# print pop(S)
