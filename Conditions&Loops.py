## BASIC IF-ELSE 

marks=int(input("enter your marks : "))
if(marks>90): 
    print(" A Grade ")
elif(marks>=75):
    print(" B Grade")  
elif(marks>60):
    print(" C Grade")
else:
    print("F Grade")


## NESTED CONDITIONS 

age=int(input("enter your age please : "))
has_id=True
if age>=18:
    if has_id:
        print("entry allowed")
    else:
        print("bring id card")
else:
    print("too young for entry")

## One-line condition (ternary operator)
x=int(input("enter marks pls : "))
result="odd" if x%2!=0 else "even"
print(result)

#LOOPS 
##TYPE 1
for i in range(10) :
    print (i) 
print("-------------")
##TYPE 2 
for i in range (1,14):
    print (i)
print("--------------")
##TYPE 3
for i in range(1,11,3):
    print(i)
print("---------------")
##TYPE 4
for i in range (10,1,-1):
    print(i)
print("-----------------")
##TYPE 5
name="aarya"
for ch in name:
    print(ch)
print("------------------")
##TYPE 6
fruits=["apple","banana","cake"]
for i in range(len(fruits)): #This loop runs how many times?-as much as the number of fruits are
    print(fruits[1])
print("-------------------")
##TYPE 7
for i in range(3):
    for j in range(2):
        print(i,j,i*j)

## PRINT STARS
for i in range(3):
    for j in range(4):
        print("*")
    print()
## MULTIPLICATION TABLE GRId 
for i in range(1,6):
    for j in range(1,6):
        print(i*j,end=" ")
    print()

## TRIANGLE PATTERN
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()
print("---------------")
## REVERSE TRIANGLE PATTERN
for i in range(6,1,-1):
    for j in range(i):
        print("*",end=" ")
    print()
print("----------------")
## BREAK 
for i in range(10):
     if i%2==0:
         continue   # this continue kya karta hai?- current iteration ko skip kar deta hai!! 
     print(i)