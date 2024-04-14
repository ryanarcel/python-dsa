# reversing a integer 4571, the results is 1754

# solution algorithm:

# let n be the given integer
# let remainder be 0
# let reversed be 0
 
# while n is greater than 0
# 1. get the last digit of n by getting its remainder with 10: remainder = n % 10
# 2. remove that last digit from the n by dividing it by 10: n = n / 10
# 3. let reversed be: reversed = reversed * 10 + remainder
# since n will be divided by 10 every iteration, it will eventually come to 0 to terminate the loop

def reverse_integer (n):
    remainder = 0
    reversed = 0

    while n > 0:
        remainder = n % 10

        # in Python, dividing with / will result to a float therefore never return a result of 0
        # divide with // instead for the result to be integer
        n = n // 10
        reversed = reversed * 10 + remainder
    
    return reversed


print(reverse_integer(4571))
    
