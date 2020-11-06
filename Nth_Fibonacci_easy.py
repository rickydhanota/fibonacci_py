#Nth Fibonacci

#The Fibonacci sequence is defined as follows: the first number of the sequence is 0, the second number is 1, and the nth number is the sum of the (n-1)th and (n-2)th numbers. Write a function that takes in an integer n and returns the nth Fibonacci number

#Import note: the Fibonacci sequence is often defined with its first two numbers as F0 = 0 and F1 = 1. For the purpose of the question, the first Fibonacci number is F0; therefore, getNthFib(1) is equal to F0, getNthFib(2) is equal to F1

#Sample input #1 where n = 2
#Sample output #1 - 1 // 0, 1
#Sample input #2 where n = 6
#Sample output #2 - 5 // 0, 1, 1, 2, 3, 5

#)(2^n) time | O(n) space
# def getNthFib(n):
#     #the if and the elif are both of our base cases which we would need in any recursive type problem
#     if n == 2:
#         return 1
#     elif n == 1:
#         return 0
#     else:
#         return getNthFib(n - 1) + getNthFib(n - 2)

def getNthFib(n, memoize = {1:0, 2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize)
        return memoize[n]
        

print(getNthFib(6))