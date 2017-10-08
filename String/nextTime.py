# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

import itertools
import re

time_re = re.compile(r'^(([01]\d|2[0-3])([0-5]\d))$')

def check(s):
    return bool(time_re.match(s))

def solution(S):
    A, B, C, D = S[0], S[1], S[3], S[4]
    perms = [x for x in itertools.product([A, B, C, D], repeat=4)]
    perms = map(lambda x: ''.join(x), perms)
    perms = filter(check, perms)
    perms = sorted(perms, key=lambda x: int(x))
    perms = map(int, perms)
    curTime = int(A + B + C + D)
    perms = sorted(list(set(perms)))
    if perms[-1] == curTime:
        res = str(perms[0])
        res = ('0' * (4 - len(res))) + res
        return res[:2] + ':' + res[2:]
    else:
        res = str(perms[perms.index(curTime) + 1])
        res = ('0' * (4 - len(res))) + res
        return res[:2] + ':' + res[2:]