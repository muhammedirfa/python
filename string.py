
Name="shadil"
Age=21
place="mlp"
print(f"my Name is {Name} and i am {Age} years old and i am comming from {place} ")

#Escape charater
print ("hello\n wolrd")
print ("hello\twolrd")
print ("hello\'' wolrd")
print ("hello\"wolrd")
print ("hello\: wolrd")

#sring methods
#s="hello, world"
#print(len(s))
s="hello, world"
print(s.strip())

#split
s="hello, world"
print(s.split(","))
s="hello, world"
print(s.find("world"))
s="hello, world"
print(s.find("hello"))

#list
my_list=[1,2,3,'python',4.5]
print(my_list)

#acessing list
my_list=['apple','orange','cherry']
print(my_list [1])
print(my_list[-1])

#multiple items
my_list=[10,20,30,40,50]
print(my_list[1:4])

#changing list
my_list=[1,2,3,4,5]
my_list[1:3]=['a','b']
print(my_list)

#adding
#append
my_list=['apple','bannan']
my_list.append("a")
my_list.insert(1,'cherry')
print(my_list)

#insert
my_list = ['apple', 'banana']
my_list.insert(1, 'cherry')
print(my_list)

#exdent
my_list=['apple','banan']
new_list=['cherry','orange']
my_list.extend(new_list)
print(my_list)

#remove
my_list=['apple','banana','cherry']
my_list.remove('banana')
print(my_list)

#pop
my_list=['apple','banana','cherry']
popped_items=my_list.pop(1)
print(popped_items)
print(my_list)

#dell
my_list=['apple','banana','cherry']
del my_list[0]
print(my_list)

#clear
my_list=['apple','banana','cherry']
my_list.clear()
print(my_list)

#sorting
my_list = [5, 2, 8, 1, 3]
my_list.sort()
print(my_list)

#copying list
my_list = [10, 20, 30, 40]
new_list = my_list.copy()
print(new_list)

#joinin list
list1=['apple','orange']
list2=['cheery','banana']
combined_list=list1+list2
print(combined_list)

#using extend()
list1 = ['apple', 'banana']
list2 = ['cherry', 'orange']
list1.extend(list2)
print(list1)








