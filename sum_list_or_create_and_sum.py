def list_sum(lst):
    """
    Returns the sum of all elements in the list.
    If input is an integer, then sum all integers from 0 to that integer
    """
    sum=0
    
    if type(lst)==list:
        for elem in lst:
            sum += elem
        
        return sum
    elif type(lst)==int:
            for elem in range(lst+1):
                sum+=elem
            return sum
    else:
        return "Invalid input"

print(list_sum([1,2,3,4,5]))

print(list_sum(9))

print(list_sum("hello"))