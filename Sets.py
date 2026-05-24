s={1,2,2,3,4,2,5,5,6}
print(s)

s.add(8)
print(s)
s.discard(3)
print(s)
s.remove(4)      # if that no. is not present then it gives key error
print(s)


a={1,2,3,4}
b={3,4,5,6}

print(a|b)  # merging all elements removing duplicate ones
print(a & b)  # this gives common element in both sets
print(a-b)  # gives element present in a but not in b . remove duplicates
print(a^b)