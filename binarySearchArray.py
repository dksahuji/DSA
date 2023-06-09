def binarySearch(array, target):
    start, end = 0, len(array)-1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif target > array[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1