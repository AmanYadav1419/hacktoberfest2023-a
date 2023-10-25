n=int(input("Enter Number: "))
arr = [int(input("Enter Element: ")) for _ in range(1,n+1)]
x=0
y=0
for i in arr:
    if(i>x):
        y=x
        x=i
print(x,y)