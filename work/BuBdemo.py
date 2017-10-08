#第二种方法写冒泡排序
arr = [40, 21, 1, 5, 22, 7, 3, -1, 9]

boo = True
while boo:
    boo = False
    for i in range(len(arr) - 1):
        if (arr[i] > arr[i + 1]):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            boo = True

print(arr)
