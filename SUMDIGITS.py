n = int(input())

while n > 0:
    l = []
    prefix = []
    s = int(input())
    l = list(map(int, input().split()))
    prefix.append(l[0])
    for i in range(1, s):
        prefix.append(l[i] + prefix[i - 1])

    q = int(input())
    while q > 0:
        l, r = map(int, input().split())
        if l > 1:
            print(prefix[r - 1] - prefix[l - 2])
        else:
            print(prefix[r - 1])

        q -= 1

        # for i in range(1,s+1):
        # l.append(int(input()))
    n -= 1

