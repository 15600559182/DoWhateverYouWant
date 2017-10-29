def exR1(n):
    if n <= 0:
        return ""
    return exR1(n - 3) + n + exR1(n - 2) + n

if __name__ == '__main__':
    print(exR1(6))