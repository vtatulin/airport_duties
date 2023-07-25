"""
worker duties
"""


class WDuty():
    def __init__(self, start: int, display_h: int, duration: int = 1):
        self.display_h = display_h  ## для красоты визуализации
        self.start = start
        self.finished = False
        self.duration = duration

    def prolongate(self):
        self.duration += 1

    def finish(self):
        self.finished = True

    def __repr__(self):
        return f'WDuty(start={self.start}, display_h={self.duration}, duration={self.duration}) ##end at: {self.start + self.duration}'


if __name__ == '__main__':
    wd = WDuty(1)
