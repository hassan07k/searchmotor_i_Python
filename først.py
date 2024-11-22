f = open("tekstfil1.txt", "rt")

for x in f:
    print (x)

mylist = ["apple", "banana", "cherry"]
print (mylist)

for x in mylist:
    print (x)
    
mylist.append("orange")
print(mylist)

f.close()