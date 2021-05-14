t=int(input())
prime=[x for x in range(101)]
p=2
while p * p <= 100:
    
    
    if prime[p] == p:
        
        
        for i in range(p * p, 101, p):
            if prime[i]%p==0:
                prime[i]=p
            
    p += 1


while t>0:
    dt=dict()
    dt[2]=0
    l=[]
    n=int(input())
    while n>1:
        if prime[n]==n:
            if n in dt:
                dt[n]+=1
            else:
                dt[n]=1
            l.append(n)
        else:
            if prime[n] in dt:
                dt[prime[n]]+=1
            else:
                dt[prime[n]]=1
            l.append(prime[n])
        
            
        n=n//prime[n]
        s=[]
    for n in dt:
        s.append(str(n)+'^'+str(dt[n]))
    print('*'.join(s))
    t-=1

    
