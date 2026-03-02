def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    
    elem1=elem2=1
    the_sum=0
    for i in range(3,n+1):
        the_sum=elem1+elem2
        elem1,elem2=elem2,the_sum
    return the_sum

for i in range(1,11):
    print(i,'->',fib(i))
    
    
def fib2(n):
    a,b = 0,1
    sequence = []
    while a<n:
        sequence.append(a)
        a,b=b,a+b
    return sequence
    
    
max=100
c=fib2(max)

print('Fibonacci sequence up to',max,'is',c)