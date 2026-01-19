#find the unique members of a list

my_list=[1,2,4,4,1,4,2,6,2,9]
unique_l=[]
for i in my_list:
    if i not in unique_l:
        unique_l.append(i)
            
my_list=unique_l

print(my_list)
