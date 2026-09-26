#creating set
a={1,2,3,4,}
print(a)

#using set function
a=set([5,6,7])
print(a)

#empty set
a=set()
print (type(a))

#accessing set items
my_set={10,22,33,44}
for item in my_set:
    print(item)

#using in keyword
a={1,2,3}
print(2 in a)
print(5 in a)

#adding itemes
 #adding single items
a={1,2,3}
a.add(4)
print(a)

#multiple items
a={1,2,3}
a.update([4,5,6])
print(a)

#remove
a={11,22,33}
a.remove(22)
print(a)

#discard
a={44,55,66}
a.discard(76)
print(a)

#pop
a={3,4,5}
remove_item=a.pop()
print(remove_item)

#clear
a={3,4,5}
a.clear()
print(a)

#joning
a={3,4,5}
b={1,2,3}
result=a.union(b)
print(result)

#update
a={3,4,5}
b={1,2,3}
a.update(b)
print(a)

#set intersection
a={3,4,5}
b={1,2,3}
result=a&b
print(result)

#set diffrence
a={3,4,5}
b={1,2,3}
result=a-b
print(result)

#symmetric
a={3,4,5}
b={1,2,3}
result=a^b
print(result)

#set copy
a={3,4,5}
b=a.copy()
print(b)




