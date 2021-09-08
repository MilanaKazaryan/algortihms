def binary_search_helper(lst, elt, left, right):
    n = len(lst)
    if left > right:
        return None
    else: 
        mid = (left + right)//2
        if lst[mid] == elt: 
            return mid
        elif lst[mid] < elt: 
            return binary_search_helper(lst, elt, mid+1, right)
        else:
            return binary_search_helper(lst, elt, left, mid-1)


def binary_search(lst, elt):
    n = len(lst)
    if elt < lst[0] or elt > lst[n-1]:
        return None
    else:
        return binary_search_helper(lst, elt, 0, n-1)


print("Searching for 9 in list [0,2,3,4,6,9,12]")
print(binary_search([0, 2, 3, 4, 6, 9, 12], 9))
