base = 16
x = int(input())
while x > 0:
    diget = x % base
    print(diget, end='')
    x //= base