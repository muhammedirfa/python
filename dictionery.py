#1. Creating a Dictionary
a={
    "name":"irfan",
    "age":"21",
    "place":"pattambi"
}
print(a)

 #2.Accessing Dictionary Items
my_dict={"name":"shadil","age":21}
print(my_dict["name"])

#3.Changing Dictionary Items
my_dict = {"name": "jhon", "age": 30, "place": "palakkad"}
my_dict["age"] = 31
print(my_dict)

#4. Adding Items to a Dictionary 
my_dict = {"name": "John", "age": 30}
my_dict["city"] = "New York" 
print(my_dict)

#5.Removing Items from a Dictionary 
my_dict = {"name": "John", "age": 30, "city": "New York"}
age = my_dict.pop("age") 
print(age)

# pop items() Removes and returns the last inserted key-value pair. 
my_dict = {"name": "John", "age": 30} 
last_item = my_dict.popitem() 
print(last_item)

#del statement: Deletes the specified key-value pair. 
my_dict = {"name": "John", "age": 30} 
del my_dict["age"]
print(my_dict) 

#clear(): Removes all elements from the dictionary.
my_dict.clear()
print(my_dict) 

#6. Copying a Dictionary
original = {"name": "John", "age": 30}
copy_dict = original.copy()
print(copy_dict) 

#7.Nested Dictionaries 
nested_dict = {

    "person1": {"name": "John", "age": 30},
    "person2": {"name": "Alice", "age": 25}
     
} 
print(nested_dict["person1"]["name"])  

#8.Dictionary Methods
# key()
my_dict = {"name": "John", "age": 30}
print(my_dict.keys()) 

#values()
print(my_dict.values()) 

#itmes()
print(my_dict.items()) 

#update()
my_dict = {"name": "John", "age": 30} 
my_dict.update({"city": "New York", "age": 31}) 
print(my_dict)  

#fromkeys()
keys = ["name", "age", "city"]
new_dict = dict.fromkeys(keys, "Unknown") 
print(new_dict) 

#setdefault(key, value):
my_dict = {"name": "John", "age": 30}
city=my_dict.setdefault("city","new york")
print(city)