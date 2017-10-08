import collections

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        move_map = {'R': 0, 'L': 0, 'U': 0, 'D': 0}
        reverse = {'R': 'L', 'L': 'R', 'U': 'D', 'D': 'U'}
        for move in moves:
            if move_map[reverse[move]] > 0:
                move_map[reverse[move]] -= 1
            else:
                move_map[move] += 1
        for count in move_map.values():
            if count > 0:
                return False
        return True

    def judgeCircleOpt(self, moves):
        c = collections.Counter(moves)
        return c['L'] == c['R'] and c['U'] == c['D']
