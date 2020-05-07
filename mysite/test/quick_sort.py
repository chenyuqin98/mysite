def quick_sort(alist, first, last):
    if first >= last:
        return
    low = first
    high = last
    mid_value = alist[low]
    while low < high:
        while low < high and mid_value <= alist[high]:
            high -= 1
        alist[low] = alist[high]
        while low < high and mid_value > alist[low]:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value
    quick_sort(alist, low + 1, last)
    quick_sort(alist, first, low - 1)


def search(alist, first, last, item):
    mid = (first + last) // 2
    if first>last:
        return -1
    elif alist[mid] == item:
        # global index
        # index= mid
        return mid
    elif item > alist[mid]:
        return search(alist, mid + 1, last, item)
        # return index
    else:
        return search(alist, first, mid - 1, item)
        # return index
    # return -1


if __name__ == '__main__':
    li = [1, 4, 5, 6]
    # quick_sort(li, 0, len(li)-1)
    print(li)
    target = search(li, 0, len(li) - 1, 7)
    print(target)
    print(0//2)