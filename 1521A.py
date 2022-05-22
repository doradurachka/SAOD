for i in range(int(input())):
    a, b = map(int, input().split())
    if b == 1:
        print("NO")
    else:
        print("YES")
        print(a*b, a, a*b + a)
