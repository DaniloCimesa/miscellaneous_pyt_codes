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