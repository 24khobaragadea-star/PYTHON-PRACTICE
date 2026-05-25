## List comprehensions are a concise, Pythonic way to create lists. Very commonly used and expected in interviews. 

## WITHOUT COMPREHENSION 
square=[]
for x in range(1,6):
    square.append(x**2)
print(square)

cube=[]
for x in range(1,6):
    square.append(x**3)
print(cube)

## With comprehension (same result, one line)

squares=[x**2 for x in range(1,6)]
print(squares)
cube=[x**3 for x in range(1,6)]
print(cube)

even =[x for x in range(1,11) if x % 2==0]
print(even)

words=["apple","python","hello"]
upper=[w.upper() for w in words]
print(upper)
lower=[w.lower() for w in words]
print(lower)

names=["aarya","arjun","parthvi"]
namelen={name : len(name)for name in names}
print(namelen)