if __name__ == '__main__':
    arr = [['t', 'h', 'i', 's'], ['w', 'a', 't', 's'], ['o', 'a', 'h', 'g'], ['f', 'g', 'd', 'f']]
    all = len(arr)
    index = all
    for a in range(len(arr)):
        aa = arr[a]

        for b in range(a + 1):

            if b == 0:
                print('', end='')
            c = all - 1 - b
            print(aa[c], end='=')
            print('[%d][%d]' % (b, c), end=',')
            if b == a:
                print(']')
        index -= 1
