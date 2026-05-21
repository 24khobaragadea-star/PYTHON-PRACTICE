nums=[10,20,30,40,50,60]
mixed=["hello",10,True,10.20]

print(nums[0])
print(nums[-1])    # Used for bigger data , more convinient
print(nums[5])

print(nums[1:5])    # includes start , exclude end . 
print(nums[0:6])
print(nums[:-1])
print(nums[::2])
print(nums[::-1])
print(nums[::-2])

fruits=["apple","banana","kiwi","grapes"]

fruits.append("mango")
print(fruits)

fruits.insert(1,"orange")
print(fruits)

fruits.remove("mango")
print(fruits)
popped=fruits.pop()
print(fruits)
poppedd=fruits.pop(1)
print(fruits)

num=[3,2,5,6,9,0,1]
num.sort()               # sorts in ascending automaticlly
print(num)
num.sort(reverse=True)   # sorts in descending 
print(num)

print(len(num))
print(sum(num))
print(max(num))
print(min(num))
print(num.count(2))
print(num.index(5))
num.reverse()          # just reverses the list
print(num)


## 2D MATRIX CREATION AND OPERATIONS ON IT 

matrix=[[1,2,3],
        [7,8,9],
        [4,5,6]]
print(matrix[0][1])

for row in matrix:
    for val in row:
        print(val,end="") # end=" " keeps the cursor stays in same line 
    print()               # this changes the line after outer loop iteration
