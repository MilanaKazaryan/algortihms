def swap(lst, i, j):
    n = len(lst)
    assert(i >= 0 and i < n)
    assert(j >= 0 and j < n)
    (lst[i], lst[j]) = (lst[j], lst[i])
    return


def copy_back(output_lst, lst, left, right):
    assert(len(output_lst) == right - left + 1)
    for i in range(left, right+1):
        lst[i] = output_lst[i - left]
    return 


def merge_helper(lst, left, mid, right):
    if left > mid or mid > right:
        return
    i1 = left
    i2 = mid + 1
    output_lst = []
    while i1 <= mid or i2 <= right:
        if i1 <= mid and i2 <= right:
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


def mergesort_helper(lst, left, right):
    if left == right:
        return 
    elif left + 1 == right:
        if lst[left] > lst[right]:
            swap(lst, left, right)
    else: 
        mid = (left + right) // 2  # compute mid point.
        mergesort_helper(lst, left, mid)
        mergesort_helper(lst, mid + 1, right)
        merge_helper(lst, left, mid, right)


def mergesort(lst):
    if len(lst) <= 1:
        return
    else:
        mergesort_helper(lst, 0, len(lst)-1)
