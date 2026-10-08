import re

text = "hello world"
print(re.search(r"world",text)) #search


text = "hello world"
print(re.match(r"world",text)) #match


text = "hello 3,3,3, world 1,2,3"
print(re.findall(r"\D+",text))    #Short an poperty


text = "hello 3,3,3, world 1,2,3"
print(re.findall(r"\d+",text))

text = "hello 3,3,3, world 1,2,3"
print(re.sub(r"\d+","numbers",text)) #replace



text = "book,pen,bag,shoe"
print(re.split(r"[;,]", text)) #split


text = "HELLO world"
print(re.search(r"hello", text, re.IGNORECASE)) 



