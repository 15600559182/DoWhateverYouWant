# mergeSort 合并排序

# 比较并交换位置，合并数组
def merge(left, right):
    i, j = 0, 0
    result = []

    while i < len(left) and j < len(right):
        # 比较大小
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 最后追加上剩余的
    result += left[i:]
    result += right[j:]
    return result


# 拆分数组
def merge_sort(lists):
    # 递归
    if len(lists) <= 1:
        return lists
    num = len(lists) // 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)


if __name__ == '__main__':
    arr = [46, 19, 9, 17, 4, 42, 9, 1, 31, 37, 0]
    arr = merge_sort(arr)
    print(arr)
