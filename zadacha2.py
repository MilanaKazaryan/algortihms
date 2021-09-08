def swap(lst, i, j):
    n = len(lst)
    assert (i >= 0 and i < n)
    assert (j >= 0 and j < n)
    (lst[i], lst[j]) = (lst[j], lst[i])
    return

def copy_back(output_lst, lst, left, right):
    assert (len(output_lst) == right - left + 1)
    for i in range(left, right + 1):
        lst[i] = output_lst[i - left]
    return

def mergeHelper(lst, left, mid, right):
    if left > mid or mid > right:
        return
    i1 = left
    i2 = mid + 1
    output_lst = []
    while (i1 <= mid or i2 <= right):
        if (i1 <= mid and i2 <= right):
            if lst[i1] <= lst[i2]:
                output_lst.append(lst[i1])
                i1 = i1 + 1
            else:
                output_lst.append(lst[i2])
                i2 = i2 + 1
        elif i1 <= mid:
            output_lst.append(lst[i1])
            i1 = i1 + 1
        else:
            output_lst.append(lst[i2])
            i2 = i2 + 1
    copy_back(output_lst, lst, left, right)
    return

def mergesortHelper(lst, left, right):
    if (left == right):
        return
    elif (left + 1 == right):
        if (lst[left] > lst[right]):
            swap(lst, left, right)
    else:
        mid = (left + right) // 2
        mergesortHelper(lst, left, mid)
        mergesortHelper(lst, mid + 1, right)
        mergeHelper(lst, left, mid, right)

def mergesort(lst):
    if len(lst) <= 1:
        return  # nothing to do
    else:
        mergesortHelper(lst, 0, len(lst) - 1)

def apples(arr,n):
    if len(arr) <= 1:
        return False
    mergesort(arr)
    left = 0
    right = len(arr) - 1
    baskets = 0
    while left <= right:
        if left == right:
            baskets += 1
            break
        if arr[left] == n:
            baskets += 1
            left += 1
        if arr[right] == n:
            baskets += 1
            right -= 1
        if arr[left] + arr[right] <= n:
            baskets += 1
            left += 1
            right -= 1
    return baskets

# задача про яблоки и корины
# макс кол-во корзин для яблок
print(apples([3, 2, 1, 4, 6, 5, 7, 8], 8))
print(apples([],2))
print(apples([3, 3, 3, 3, 3], 3))
print(apples([1, 2, 2, 3, 3], 3))
