#random sequence of numbers with 0s in it
#objective is to transfer 0's at the end of the list
#and the rest of the numbers should stay in the same order

#my solution

a = [0,4,3,1,0,5,2,9,0,4,5,13,7,0,3,0,8]
b=[]
#low = []

#print(sorted(a))

for i in a:
    if i ==0:
        b.append(a.pop(a.index(i)))

c = a + b 
print(c)

#v2 of solution

a = [0,4,3,1,0,5,2,9,0,4,5,13,7,0,3,0,8]

no_zeros = [i for i in a if i !=0]
zeros = (int(len(a)) - int(len(no_zeros)))*[0]
b = no_zeros + zeros
print(b)