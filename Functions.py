##BASIC FUNCTION
 
def greet(name):
   print("hello",name)
greet("aarya")
greet("arjun")

##FUNCTION WITH RETURN VALUE 

def add(a, b):
   return(a+b)
result=add(3,2)
print(result)

def min_max(number):
   return min(number),max(number)
num=min_max([1,2,3,4,5,75])
print(num)

## FUNCTION WITH IF-ELSE
def check_even(num):
   if num%2==0:
      print("number is even")
   else:
      print("number is odd")
check_even(10)
check_even(11)

## FUNCTION WITH USER INPUT

def check_even(num):
   if num%2==0:
      print("even")
   else:
      print("odd")

x=int(input("enter a number: "))

check_even(x)
check_even(x)

## FUNCTION WITH LAMBDA
square=lambda x: x*x    # lambda makes a code easier and short
print(square(5))

## FUNCTION WITH RECURSIVE CALL

def countdown(n):
   if n==0:
      return
   print(n)

   countdown(n - 1)
countdown(5)