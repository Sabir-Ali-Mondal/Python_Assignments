#linear search

def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index  
    return -1 

arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
target = int(input("Enter the target element to search for: "))

result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} is found at index {result}.")
else:
    print(f"Element {target} is not found in the array.")
