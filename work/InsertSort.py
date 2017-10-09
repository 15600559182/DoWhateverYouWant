# 插入排序
# 和扑克牌插入类似
# 将一个元素和前边每一个元素比较如果最大则一直往后挪位置
if __name__ == '__main__':
    arr = [46, 19, 9, 17, 4, 42, 9, 1, 31, 37]
    for i in range(len(arr)):
        x = arr[i]
        index = i
        while index > 0 and arr[index - 1] > x:
            arr[index] = arr[index - 1]
            index -= 1
        arr[index] = x

    print(arr)
