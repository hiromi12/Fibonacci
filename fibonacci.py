# Fibonacci Sequence
# Date: Oct 7, 2022
# Author: Hiromi Honda

# Program Description: 
# Function 'fibonacci' is a recursion function that calculates fibonacci sequence until n(th).
# Function 'print_fibonacci' is a function that prints fibonacci sequence.

def fibonacci(n):
  if n < 0:
    return
  elif n <= 1:
    return n
  else:
    return (fibonacci(n - 1) + fibonacci(n - 2))

def print_fibonacci(n):
  if n <= 0:
    print("Enter positive integer.")
  else:
    for i in range(n):
      print(fibonacci(i), end=" ")
      
print_fibonacci(20)

# Output (0.4s)
# 
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 
# 