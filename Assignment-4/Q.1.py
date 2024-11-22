def is_palindrome(lst):
    if len(lst) <= 1:
        return True
    if lst[0] != lst[-1]:
        return False
    return is_palindrome(lst[1:-1])

# Test cases
print(is_palindrome([]))           
print(is_palindrome([7]))          
print(is_palindrome([8, 11, 8]))   
print(is_palindrome([19, 3, 44, 44, 3, 19]))  
print(is_palindrome([3, 18, 4]))   
print(is_palindrome([23, 14, 3, 14, 3, 23]))  
