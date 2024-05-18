"""Good morning! Here's your coding interview problem for today.
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?"""




x=int(input('Enter the list size:'))
i=0

print('Enter list elements:\n')
l1 = [int(input()) for _ in range(x)]
k=int(input('Enter the no:'))

y='False'

start=l1[0]

j=1

for j in range(x):
    if((start+l1[j])==k):
        y='True'
    j+=1

print(y)
    
