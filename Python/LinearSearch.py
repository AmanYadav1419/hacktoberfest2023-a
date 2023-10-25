#Basic Linear Search

# Defines function that searches through array
def linearsearch(arr, x): # Passes in target as x, and the array
   return next((i for i in range(len(arr)) if arr[i] == x), -1)

arr = [1,2,3,4,5,6,7,8,9,10] # Defines array

x = int(input("Enter a number between 1 and 10: ")) # Gets the user key value

print(f"element found at index {str(linearsearch(arr, x))}")