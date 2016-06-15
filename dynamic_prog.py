neg_inf = -9999999

# cut_rod_r runs in exponential time
def cut_rod_r(p, n):
    if n == 0:
        return 0
    q = neg_inf
    for i in range(0, n):
        q = max(q, p[i] + cut_rod_r(p, n-i-1))
    return q

p = [1,5,8,9,10,17,17,20,24,30]

# print cut_rod_r(p, 10)


# cut_rod_memoized runs in
def cut_rod_memoized(p, n):
    r = [neg_inf] * (n+1)
    r[0] = 0
    return cut_rod_memoized_aux(p, n, r)

def cut_rod_memoized_aux(p, n, r):
    if r[n] != neg_inf:
        return r[n]
    q = neg_inf
    for i in range(1, n+1):
        q = max(q, p[i-1] + cut_rod_memoized_aux(p, n-i, r))
    r[n] = q
    return q

# print cut_rod_memoized(p, 10)


# cut_rod_bottom_up runs in
def cut_rod_bottom_up(p, n):
    r = [neg_inf]*(n+1)
    r[0] = 0
    for i in range(1, n+1):
        q = neg_inf
        for j in range(1, i+1):
            q = max(q, p[j-1] + r[i-j])
        r[i] = q
    return r[n]

# print cut_rod_bottom_up(p, 10)
