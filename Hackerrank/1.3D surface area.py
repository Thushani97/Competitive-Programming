first_multiple_input = input().rstrip().split()

H = int(first_multiple_input[0])

W = int(first_multiple_input[1])

A = []

for _ in range(H):
    A.append(list(map(int, input().rstrip().split())))
