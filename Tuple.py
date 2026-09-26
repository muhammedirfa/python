#creating Tuple
my_tuple=(1,2,3,'python',4,5)
print(my_tuple)

#single items
single_tuple=(5,)
print(type(single_tuple))

#accessing itemes
my_tuple=('apple','banana','cheery')
print(my_tuple[1])
print(my_tuple[-1])

#slicing tuple
my_tuple=('10','20','30','40','50')
print(my_tuple[1:4])

#updating tuple
  #reassigning
my_tuple=(1,2,3)
my_tuple=(4,5,6)
print(my_tuple)

#covert tuple to list
my_tuple = ('apple', 'banana', 'cherry')
temp_list = list(my_tuple)
temp_list[1] = 'orange'
my_tuple = tuple(temp_list)
print(my_tuple) 

#unpacking tuple
my_tuple=('apple','banana','cheery')
(fruit1,fruit2,fuit3)=my_tuple
print(fruit1)
print(fruit2)
print(fuit3)

#uing star
my_tuple=(1,2,3,4,5)
(a,b,*c)=my_tuple
print(a)
print(b)
print(c)

#joining
tuple1=(1,2,3)
tuple2=(4,5,6)
join_tuple=tuple1+tuple2
print(join_tuple)

#tuple methods
#count
my_tuple=(1,2,3,2,2,4)
print(my_tuple.count(2))

#index
my_tuple=('apple','banana','cherry')
print(my_tuple.index('banana'))

#deleting tuple
my_tuple=('apple','banana','cherry')
del my_tuple




