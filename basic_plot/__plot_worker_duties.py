from typing import List
import matplotlib.pyplot as plt
from basic_duties.__w_duty import WDuty


def plot_worker_duties(duty_list: List[WDuty]):
    for d in duty_list:
        plt.plot([d.start, d.start + d.duration], [d.display_h, d.display_h])
