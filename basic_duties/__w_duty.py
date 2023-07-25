"""
worker duties
"""
from dataclasses import dataclass


@dataclass
class WDuty():
    start: int
    display_h: int
    duration: int = 1
    finished: bool = False

    def prolongate(self):
        self.duration += 1

    def finish(self):
        self.finished = True

    def __repr__(self):
        return f'WDuty(start={self.start}, display_h={self.duration}, duration={self.duration}) ##end at: {self.start + self.duration}'


if __name__ == '__main__':
    wd = WDuty(1)
