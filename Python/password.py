#password generator
import random
letter = [chr(i) for i in range(65,91)]
letter.extend(chr(i) for i in range(97,123))
number=["0","1","2","3","4","5","6","7","8","9"]
char=["~","!","@","#","$","%","^","&","*"]
a=int(input("Enter the number of letters\n"))
b=int(input("Enter the number of number\n"))
c=int(input("Enter the number of character\n"))
passw=""
for _ in range(0,a+1):
    passw=passw+random.choice(letter)
for _ in range(0,b+1):
    passw +=random.choice(number)
for _ in range(0,c+1):
    passw += random.choice(char)
o=list(passw)
random.shuffle(o)
password = "".join(o)
print(password)
