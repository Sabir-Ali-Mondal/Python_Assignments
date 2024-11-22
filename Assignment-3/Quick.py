#quicksort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = []   
    right = []
    equal = [] 

    for element in arr:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            equal.append(element)

    return quick_sort(left) + equal + quick_sort(right)


arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))


sorted_arr = quick_sort(arr)


print("Sorted array is:")
print(sorted_arr)
