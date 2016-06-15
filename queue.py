# Q = [None]*5
# Q = [1,None,None,None,5]
# Q_tail = 1
# Q_head = 4

def enqueue(Q, x):
    global Q_head
    global Q_tail
    if Q_head == Q_tail + 1:
        return "Error: overflow"
    Q[Q_tail] = x
    if Q_tail == len(Q) - 1:
        Q_tail = 0
    else:
        Q_tail += 1

# print enqueue(Q, 3)
# print Q
#
# print enqueue(Q, 4)
# print Q
#
# print enqueue(Q, 6)
# print Q

def dequeue(Q):
    global Q_head
    global Q_tail
    if(Q_head == Q_tail):
        return "Error: underflow"
    x = Q[Q_head]
    Q[Q_head] = None
    if Q_head == len(Q) - 1:
        Q_head = 0
    else:
        Q_head += 1
    return x
#
# print dequeue(Q)
# print Q
#
# print dequeue(Q)
# print Q
#
# print enqueue(Q, 6)
# print Q
#
# print enqueue(Q, 7)
# print Q
#
# print enqueue(Q, 8)
# print Q
#
# print enqueue(Q, 9)
# print Q
