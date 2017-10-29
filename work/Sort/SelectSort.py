# 选择排序
if __name__ == '__main__':
    arr = [40, 21, 1, 5, 22, 7, 3, -1, 9]
    index = len(arr)
    for i in range(index):
        min = i
        boo = False
        for j in range(index):
            if j > i:
                if arr[min] > arr[j]:
                    min = j
                    boo = True
        if boo:
            arr[i], arr[min] = arr[min], arr[i]
    print(arr)
