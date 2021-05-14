t=int(input())
while t>0:
    m,n=map(int,input().split())


    prime = [True for i in range(n+1)]
    p = 2
    while p * p <= n:
        
        # If prime[p] is not changed, then it is a prime
        if prime[p] == True:
            
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    s=0
    prime[0]=False
    prime[1]=False
    # Print all prime numbers
    for p in range(m,n + 1):
        if prime[p]:
            s+=p
    print(s)
    t-=1
