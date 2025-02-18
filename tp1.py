import random
import string
import time
print("enter string")
target=input()
letters = string.ascii_letters
result = ""
for letter in target:
    while True:
        l= random.choice(letters)
        print(result + l)
        if(l==letter):
            result+=l
            break
        time.sleep(0.1)
