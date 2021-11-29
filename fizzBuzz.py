'''
Given a number n, for each integeri in the range from 1 to n inclusive, print one value per line as follows:

If i is a multiple of both 3 and 5 print FizzBuzz.
If i is a multiple of 3 (but not 5), print Fizz.
If i is a multiple of 5 (but not 3), print Buzz.
If i is not a multiple of 3 or 5, print the value of i.

The function takes upper bound n and it returns None. 
The function must pront the appropriate response in ascending order each on a separate line.
'''

#
# Programmer: Nikola Andric
# Email: nikolazeljoandric@gmail.com
# Last Eddited: 11/28/2021
#


def fizzBuzz(n):

    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 3 != 0 and i % 5 == 0:
            print("Buzz")
        else:
            print(i) 

    return None


if __name__ == '__main__':
    n = int(input().strip())
    fizzBuzz(n)
