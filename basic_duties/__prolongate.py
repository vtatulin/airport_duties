from typing import List
from .__w_duty import WDuty
from .__merge import get_height_lits


def prolongate_duties(duty_list: List[WDuty], min_duration):
    for wd in duty_list:
        if wd.duration < min_duration:
            wd.duration = min_duration


def prolongate_duties_except_last(duty_list: List[WDuty], min_duration):
    height_lists = get_height_lits(duty_list)
    for height, h_list in height_lists.items():
        h_list.sort(key=lambda x: x.display_h)
        for wd in h_list[:-1]:
            if wd.duration < min_duration:
                wd.duration = min_duration
