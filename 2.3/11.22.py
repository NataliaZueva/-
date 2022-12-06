def prime_number(a):
    k = 0
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            k = k + 1
    if k <= 0:
        return a
    else:
        return -1


def transformation(a):
    q = []
    b = [int(i) for i in str(a)]
    if int(a) > 0:
        q.append(int(a))
        for i in range(len(b) - 1):
            b.insert(0, b.pop())
            li = int(''.join(map(str, b)))
            if prime_number(li) != -1:
                q.append(li)
            else:
                return -1
    return q


k = 0
for i in range(2, 1_000_000):
    if prime_number(i) != -1:
        if transformation(i) != -1:
            print(i)
            k += 1
print(k)
