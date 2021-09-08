# в массиве найти n-нное по величине число
def search(arr, n):
    if len(arr) < n:
        return False
    insertion_sort(arr)
    a = arr[0]
    counter = 1
    if counter == n:
        return a
    for i in range(1, len(arr)):
        if a == arr[i]:
            continue
        else:
            counter += 1
            a = arr[i]
            if counter == n:
                return a
    return False


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


print(search([0, 6, 9, 8], 3))
print(search([5, 7, 9, 11, 13], 2))
print(search([], 4))
print(search([0, 0, 0, 0, 0], 3))
