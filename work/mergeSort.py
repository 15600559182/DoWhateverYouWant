# mergeSort 合并排序

# 比较并交换位置，合并数组
def merge(left, right):
    i, j = 0, 0
    result = []

    while i < len(left) and j < len(right):
        # 比较大小 不断追加
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


# 拆分数组  分解：将原问题分解成一系列子问题；
def merge_sort(lists):
    #   对于子序列排序时，其长度为1时，递归结束。当个元素视为已排好序
    if len(lists) <= 1:
        return lists
    # 分解：将n个元素分成各含n/2个元素的子序列
    num = len(lists) // 2
    # 解决：用合并排序法将两个子序列递归的排序
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])

    # 合并：合并两个已排序的子序列以得到排序结果
    return merge(left, right)


if __name__ == '__main__':
    arr = [46, 19, 9, 17, 4, 42, 9, 1, 31, 37, 0]
    arr = merge_sort(arr)
    print(arr)
