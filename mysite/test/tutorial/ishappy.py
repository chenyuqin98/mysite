def find_peak(alist, first, last):
    mid = (first + last) // 2
    global value
    # print(mid)
    if alist[mid] > alist[mid + 1] and alist[mid] > alist[mid - 1]:
        value = mid
        return value
        # print(mid)
    elif alist[mid + 1] < alist[mid] < alist[mid - 1]:
        find_peak(alist, first, mid - 1)
        return value
    else:
        find_peak(alist, mid + 1, last)
        return value



if __name__ == '__main__':
    li = [1, 4, 5, 6, 4, 2]
    print(li)
    print(find_peak(li, 0, len(li) - 1))
    # print(li[2],li[3],li[4])
