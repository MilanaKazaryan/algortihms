def binary_search(arr, element):
    if element < arr[0] or element > arr[-1]:
        return None
    else:
        left = 0
        right = len(arr)-1
        while left <= right:
            middle = (left+right) // 2
            if element == arr[middle]:
                return
            elif element < arr[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            return False


print(binary_search([0, 2, 3, 4, 6, 9, 12], 9))
print(binary_search([0, 2], 0))
print(binary_search([1, 3, 5, 7, 9, 11, 13], 14))
