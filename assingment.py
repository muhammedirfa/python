#1. Create a string "hello" and convert it to uppercase using a string method.
my_string = "hello"
print(my_string.upper())

#2.Given "PYTHON" , convert it to lowercase using a string method.
my_string = "python"
print(my_string.lower())

#3.From "hello world" , replace "world" with "python" using a string method.
a= "hello world"
print(a.replace("world", "python"))

#4.Extract "ell" from "hello" using slicing only.
a="hello world"
print(a[1:5])

#5.Reverse the string "python" using slicing (no loops).
a="hello world"
print(a[::-1])

#6.Combine "hello" and "world" into one string using string operations.
a="hello"
b="world"
print(a + b)

#7.Repeat the string "hi" to get "hihihi" using string operations.
a="hello world"
result = a * 3
print(a)

#8.Check if "cat" exists in "concatenate" using a string operator.
s2="concatenate"
print(s2.find("cat"))

#9.Count how many times "a" appears in "banana" using a string method.
a = "banana"
print(a.count("a"))

#10.Remove leading and trailing spaces from " hello " using a string method
a = " hello "
print(a.strip())

#11.Find the index of "o" in "hello" using a string method
a = "hello"
print(a.index("o"))

#12.Split the string "a,b,c,d" into a list using a string method.
a = "a,b,c,d"
print(a.split(","))

#13.Join the list ["a","b","c"] into "abc" using a string method.
my_list = ["a", "b", "c"]
print("".join(my_list))

#14.Extract every 2nd character from "abcdef" using slicing → expected "ace
a = "abcdef"
print(a[::2])

#15.Replace all "a" with "@" in "banana" using a string method.
a = "banana"
print(a.replace("a", "@"))

#16.Check if "hello123" is alphanumeric using a string method
a = "hello123"
print(a.isalnum())

#17.Capitalize the first letter of "python" using a string method.
a = "python"
print(a.capitalize())

#18.Convert "hello world" into "Hello World" using a string method.
a = "hello world"
print(a.title())

#19.Remove all vowels from "python" using string operations (no loops if possible 😈).
a = "python"
result = a.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
print(result)

#20.Check if "madam" is a palindrome using slicing
a = "madam"
print(a == a[::-1])