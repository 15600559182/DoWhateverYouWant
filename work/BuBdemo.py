arr = [40, 21, 1, 5, 22, 7, 3, -1, 9]

index = len(arr) - 1
boo = True
while boo:
    boo = False
    for i in range(index):
        if (arr[i] > arr[i + 1]):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            boo = True
    index -= 1

print(arr)
