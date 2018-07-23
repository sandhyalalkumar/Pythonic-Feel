T = input()

for _ in range(0, T):
    N, A, B = map(int, raw_input().split())
    numbers = map(int, raw_input().split())
    countA = 0
    countB = 0
    for e in numbers:
        if e == A:
            countA = countA + 1
        if e == B:
            countB = countB + 1
    print (countA*countB*1.0)/(N*N)
