def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print(factorial(3))
print(factorial(0))

def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
for i in range(9):
    print(fibonacci(i))