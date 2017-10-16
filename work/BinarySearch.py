# 二分查找

# 参数：param要查找的值，arr数组
# 返回：对应的数组下标位置
def binarySearcbh(param, arr):
    left = 0
    right = len(arr) - 1
    while left <= right:

        #取中间的书来判断
        flag = left + (right - left) // 2
        if arr[flag] > param:
            right = flag - 1
        elif arr[flag] < param:
            left = flag + 1
        else:
            return flag
    return -1


if __name__ == '__main__':
    arr = [1, 2, 4, 6, 20, 50, 52, 83, 100]
    index = binarySearcbh(6, arr)
    print(index)
