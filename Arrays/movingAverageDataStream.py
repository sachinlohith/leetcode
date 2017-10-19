from collections import deque

class solution:
    def __init__(self, size):
        self.size = size
        self.queue = deque([])
        self.sum = 0

    def next(self, num):
        self.sum += num
        self.queue.append(num)
        if self.size >= len(self.queue):
            return float(self.sum) / len(self.queue)
        else:
            self.sum -= self.queue.popleft()
            return float(self.sum) / len(self.queue)

