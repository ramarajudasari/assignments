t = int(input())
while t > 0:
    n = int(input())
    l = list(map(int, input().split()))

    sum = 0

    for x in range(0, n):
        if l[x] == -1:
            l[x] = sum // x
        sum = sum + l[x]
        print(l[x], end=' ')

    t -= 1
    print()