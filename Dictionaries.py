## Dictionaries store key-value pairs. Keys must be unique. O(1) average lookup time — this makes dicts extremely
## useful in DSA for hashing problems.

# CREATING A DICT
student={"name" : "aarya",
         "age" : 20,
         "branch" : "AIDS",
         "cgpa" : 9
        }

# ACCESSING A DICT 
print(student["name"])
print(student.get("age"))
print(student.get("phone"))

# UPDATE A DICT

student["age"]= 19
print(student)
student["phone number"]= 12345
print(student)


##  ITERATION 
for key in student:
    print(key,student[key])

for key, value in student.items():       ## student.items() gives BOTH key and value together.
    print(key,value)

print(student.keys())    ## print all keys
print(student.values())  ## print all values
print("year" in student)


# Frequency counter (extremely common in DSA)
words=["apple","apple","mango","banana","mango","kiwi"]
freq={}
for word in words:
    freq[word]=freq.get(word , 0)+1
print(freq)


# SIMPLER WAY WITH USING defaultdict

from collections import defaultdict , Counter
freq2=(words)
print(freq2)

