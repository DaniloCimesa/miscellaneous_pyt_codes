
def is_prime_number(num):
    #first check if num is less than 2
    #if so, return False
    if num <=1:
        return False
    #check if num is divisible by any number from 2 to square root of num+1
    for i in range(2, int(num**0.5) + 1):
    #if so, return False
        if num % i == 0:
            return False
    #else return True
    return True

is_prime_number(37)