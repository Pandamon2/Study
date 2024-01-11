import sys
N = int(sys.stdin.readline())
list = [0] * (10000 + 1)
for i in range(N):
    list[int(sys.stdin.readline())] += 1
for i in range(len(list)):
    if list[i] != 0:
        for _ in range(list[i]):
            print(i)