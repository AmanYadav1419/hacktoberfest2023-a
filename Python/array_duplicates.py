# Find duplicates in an array

def findDup(liArr):
    liArr.sort()

    return [liArr[i] for i in range(0, len(liArr)-1) if liArr[i]==liArr[i+1]]
 
print("enter array elements: ")
sample = list(map(int, input().split()))
print(findDup(sample))
#print(findDup([2, 3, 1, 0, 2, 5,3]))