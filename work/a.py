# 快速排序

# 找一个数作为基准数  大于基数的再右边 否则左边
# 快速排序
def quick_sort(lists, left, right):
    if left >= right:
        return
    a = left
    b = right
    x = lists[0]

    while a < b:
        while lists[b] >= x and a < b:  # 右侧为比较的第一个数 如果比标记数 小则继续走
            b -= 1
        while lists[a] <= x and a < b:  # 左侧为比较的第一个数 如果比标记数 打则继续走
            a += 1
        if a < b:
            lists[a], lists[b] = lists[b], lists[a]

    lists[a] = x
    quick_sort(lists, a, left-1)
    quick_sort(lists, b, right)
    return lists


if __name__ == '__main__':
    arr = [56, 18, 6, 3, 97, 66, 57, 26, 88, 30, 99, 93]
    arr = quick_sort(arr, 0, len(arr) - 1)
    print(arr)
