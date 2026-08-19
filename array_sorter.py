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

#v3 of the solution
def move_zeros_to_end():
    nums = []
    print('Enter numbers in a sequence(write Q if you want to quit):')
    while True:
        input_num = input('Enter number:')
    
        if input_num.lower() == 'q':
            break
    
        if input_num.isdigit() or (input_num.startswith('-') and input_num[1:].isdigit()):
            nums.append(int(input_num))
        else:
            print('Invalid input. Please enter a valid number or Q to quit.')
    
    no_zeros = [i for i in nums if i !=0]
    zeros = [0] * (len(nums) - len(no_zeros))
    b = no_zeros + zeros
    return b, nums
    
result = move_zeros_to_end()
print('Original list:', result[1])
print('List after moving zeros:',result[0])