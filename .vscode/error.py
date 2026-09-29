#1.
# a = 10
# b = 0
# print(a / b)


#2.TypeError
# a = 10
# b = "5"
# print(a + b)


#3.value error
# a = int("hello")
# print(a)

#4.index error
# a = [10, 20, 30]
# print(a[5])

#5.KeyError
# a = {"name": "Irfan",
#     "age": 21}
# print(a["place"])

#6.FileNotFoundError
# a = open("hello.txt", "r")


#7.try:
#     a = 10 / 0
# except:
#     print("An error occurred")

#8.else block
try:
    a = 10 / 2
except:
    print("Error")
else:
    print("No error")
