#recursion.py
""" recursion.py is a simple example of how to define and use recursion in a function"""

import time

def even_nums(num):
    """ recursive function to find and print """
    print(num)
    if num % 2 != 0:
        print("Please enter an even number.")
    elif num == 2:
        return num
    else:
        return even_nums(num - 2)    

def fibonacci_iteration(index):
    """ returns the fibonacci number at the specified index without using recursion"""
    seq = [0,1]
    for i in range(index):
        seq.append(seq[-1]+seq[-2])
    return seq[-2]

def fibonacci_recursion(index_of_number):
    """ returns the fibonacci number at the specified index """
    if index_of_number <= 1:
        return index_of_number
    else:
        return fibonacci_recursion(index_of_number-1)+fibonacci_recursion(index_of_number-2)


#even_nums(9)
#for i in range(1,8):
#    print(Fibonacci(i))

print("\n")

print("***** recursion *****")
rec = time.time()
print(fibonacci_recursion(200))
rec_res = time.time()-rec
print("speed : " + str(rec_res) + "\n")

print("***** iteration *****")
it = time.time()
print(fibonacci_iteration(200))
it_res = time.time()-it
print("speed : " + str(it_res) + "\n")

if rec_res < it_res:
    print("Recursion was faster!\n")
else:
    print("Iteration was faster!\n")
