given = [x for x in range(1, int(input()) + 1)]
lens = len(given)
if lens % 2 == 1:
    print(-1)
else:
    answer = []
    lens = len(given)
    i = 1
    while i < lens:
        answer.extend([i+1, i])
        i += 2
    print(*answer)
