
def solution(P, K):
    flowers = [0] * len(P)
    result = 0
    for idx, day in enumerate(P):
        flowers[day - 1] = 1
        left, right = 0, 0
        for n in range(len(flowers)):
            if flowers[n] == 0:
                right += 1
            else:
                if right - left == K:
                    return idx + 1
                left = n
                right = n
    return -1