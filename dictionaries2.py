#1. Create and Access
Book={"Title":"The Art of War",
      "Author":"Sun Tzu",
      "Year published":"between 475 and 221 B.C.E"}
print(Book)

#2. Word Frequency Counter
from collections import Counter
fruits="apple banana apple orange banana banana"
print("The fruit count:" + str(fruits))
res = Counter(fruits.split())
print("The word frequency of fruits:" + str(dict(res)))

#3. Convert Two Lists into a dictionary
keys=['name','age','city']
values=['Alice',25,'London']

res ={keys[i]:values[i] for i in range (len(keys))}
print("Personal_Info:"+str(res))