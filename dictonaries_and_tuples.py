#DICTIONARIES
#dictionary structure
from itertools import count


dictionary = {
    "a":'b',
    "c":'d',
    "e":'f',
    "g":'h'
    
}

dictionary.pop('c')

print(dictionary)

#example of getting the item from dictionary
item_2=dictionary['c']
print(item_2)
#another way to get the item from dictionary
item_2_1=dictionary.get('c')
print(item_2_1)

#assigning value to a key
dictionary['c']='new_key'
print(dictionary)
print(dictionary['c'])
#removing item from dictionary
phonebook={}

phonebook['Danilo']=123456
print(phonebook)

del phonebook['Danilo']

#insert into dictionary
polish_to_english={'kwiat':'flower'}
polish_to_english.update({'drzewo':'tree'})

print(polish_to_english)
#popitem removes the last item
#pop removes the scepific item

#for loops to go through dictionary
for item in polish_to_english:
    print(item)
    
#keys and values
for key, value in polish_to_english.items():
    print('Pol/Eng ->', key, ':', value)
    
#if 
if 'kwiat' in polish_to_english:
    print('Yes')
else:
    print('No')
#del for removing the specific item
del dictionary[key]
#or to delete an entire dictionary
del dictionary

#copy dictionary
new_dict=dictionary.copy()
print(new_dict)

#excercise4
d1={'Adam Smith':'A','Judy Paxton':'B+'}
d2={'Mary Louis':'A', 'Patrick White':'C'}
d3={}
for item in (d1,d2):
    d3.update(item)

print(d3)

#---------------------------------------------------------------------------------------------

#TUPLES
#tuples
tuple="1",

print(type(tuple))

#example1
tuple_1=(1,2,3)
for elem in tuple_1:
    print(elem)

#example2
tuple_2=(1,2,3,4)
print(5 in tuple_2)
print(5 not in tuple_2)

#example3
tuple_3=(1,2,3,5)
print(len(tuple_3))

#example4

tuple_4=tuple_1+tuple_2
tuple_5=tuple_3*2

print(tuple_4, tuple_5)

#count number of duplicates 
#exercise4
tup = 1,2,3,2,4,5,6,2,7,2,8,9
duplicates= [t for t in tup if tup.count(t)>1]
print(len(duplicates))
print(type(tup))

#excercise5
#list to tuple
my_list=['car','ford','flower','tulip']
t=tuple(my_list)
print(t)

#excercise6 
#tuple to dictionary
colors = (('green','#008000'), ('red','#FF0000'), ('blue','#0000FF'))
colors_dict={}

for color in colors:
    colors_dict[color[0]]=color[1]

print(colors_dict)