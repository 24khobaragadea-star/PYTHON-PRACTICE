##ARITHMETIC OPERATORS
a,b=12,2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

##COMPARISON OPERATOR 
x=10
print(x<12)
print(x==15)
print(x<=10)

##LOGICAL OPERATORS
cgpa=8.0
age=18
print(cgpa<8.0 and age>12)
print(cgpa<8.0 or age>12)
print(not(age<20))

##ASSIGNMENT OPERATORS
x=10
x+=1
x-=1
x*=12
print(x)


##INPUT & OUTPUT 

name=input("enter you name : ")
print("Hello",name,"you are so beautiful")

a,b,c=map(int, input("enter 3 numbers: ").split())
print(a,b,c)


a,b,c,d,e = list(map(int, input ("enter numbers : ").split()))
print(a,b,c,d,e)