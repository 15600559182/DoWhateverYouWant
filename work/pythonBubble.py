class pythonBubble:
    def BuB_sort(self, arr):
        # 循环次数取决于数组的长度
        for index in range(len(arr) - 1):
            for i in range(len(arr)):
                if (i != len(arr) - 1):
                    if (arr[i] > arr[i + 1]):
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]


if __name__ == "__main__":
    arr = [29, 10, 14, 37, 14, 6, 0, 7, -1]
    b = pythonBubble()
    b.BuB_sort(arr)
    print(arr)
