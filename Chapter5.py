def min_coins(d, n):
    INF = float('inf')
    F = [INF] * (n + 1)
    F[0] = 0

    for x in range(1, n + 1):
        for coin in d:
            if coin <= x:
                F[x] = min(F[x], F[x - coin] + 1)

    print("Bang F:", F)
    return F[n]


d = [1, 3, 4]
n = 6
print("So dong it nhat:", min_coins(d, n))