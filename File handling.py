# writing to a file 
with open ("notes.txt" , "w") as f:
    f.write("hi im aarya  \n")
    f.write("im learning python \n ")
    f.write("file handling in python  \n")

# reading an entire file 
with open ("notes.txt" , "r") as f:
    content=f.read()
    print(content)

# reading a file line by line 
with open("notes.txt" , "r") as f:
    for line in f:
        print(line.strip())

# reading all lines by list 
with open("notes.txt" , "r") as f:
    lines=f.readlines()

# append to a existing file 

with open("notes.txt" , "a") as f:
    f.write("hey im there again")

with open("notes.txt","r") as f:
    content=f.read()
    print(content)
