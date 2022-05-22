a, b, s = list(map(int, input().split()))
res = 'Yes'
if s < abs(a) + abs(b):
    res = 'No'
else:
    if (abs(a) + abs(b) - s) % 2 != 0:
        res = 'No'
print(res)