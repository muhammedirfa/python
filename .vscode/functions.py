def great():#define function
    print("hello world")

great() #call function


def great(name,age,place):
    print(f"my name is {name}my age is {age}iam comming from{place}")

great("irfan" , 21,"pattambi")

#defult aregument
def great(name,age,place="no placed seleted"):
    print(f"my name is {name}my age is {age}iam comming from{place}")

great("irfan",21)

#key words
def great(name,age,place):
    print(f"my name is {name}my age is {age}iam comming from {place}")


great("irfan",21,place="pattambi")
great(place="pattambi",name="john",age=22)


#abrebiter
 
def number(*a):
    print(a)

number(1,2,3,4,5,6,7,8,9,10)

#arebiter key word
def details(**a):
    print(a)

details(name="irfan",age=21,place="palakkad",country="india")


def details(name,*args,**kwrgs):
    print(name)
    print(args)
    print(kwrgs)

details("name",11,22,33,44,55,66,fname="irfan",age=21,place="palakkad",country="india")



def add_def(x, y):
    return x + y

print(add_def(10,30))


add=lambda x,y: x+y
print(add(10,20))


def num(a):
    if a>=1:
        print("postive number")
    elif a<=1:
        print("negative number")
    else:
        print("one")
num(1)
num(2)
num(-1)

# odd or even

def num (a):
    if a%2==0:
        return("even")
    else:
        return("odd")
print(num(3))

#largest among three numbers

def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
result = find_largest(10, 25, 15)
print("Largest number is:",result)


# length of a string

def get_length(text):
    return 
a = "muhammed irfan pp"
result = get_length(a)
print("Length is:", result) 


#captlize
def make_capital(text):
    return text.upper()
a = "muhammed irfan pp"
result = make_capital(a)
print("Capitalized:", result)










