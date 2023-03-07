#!/usr/bin/python3
for num in range(0,100):
    if (num % 10) > (num // 10) and num != 89:
        print("{:02d}, ".format(num), end='')
print("89")
