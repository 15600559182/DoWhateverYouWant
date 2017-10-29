# 快速排序

# 找一个数作为基准数  大于基数的再右边 否则左边
def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists


if __name__ == '__main__':
    arr = [56, 18, 6, 3, 97, 66, 57, 26, 88, 30, 99,93]
    arr = quick_sort(arr, 0, len(arr) - 1)
    print(arr)
