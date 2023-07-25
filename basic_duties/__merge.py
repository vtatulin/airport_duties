from typing import List, Dict
from .__w_duty import WDuty


def _merge(duty_list: List[WDuty]):
    ## Важное замечение: по задумке мы мерджим смены одной "высоты"
    result_height = duty_list[0].display_h

    ## пересекаем смены со всеми и объединяем
    end_time = max([_.start + _.duration for _ in duty_list])
    start_stops = [0 for _ in range(end_time + 1)]  ## на старт пишем +1, на стоп - -1
    for wd in duty_list:
        start_stops[wd.start] += 1
        start_stops[wd.start + wd.duration] -= 1

    ##что в моменте? сколько смен в проммежуток?
    durations_at_moment = [0 for _ in range(end_time + 1)]
    _cur_duties = 0
    for i, el in enumerate(start_stops):
        _cur_duties += el
        durations_at_moment[i] = _cur_duties
    ## итого - каждый элемент массива durations_at_moment - сколько смен тут перекрыто.
    ## 0 - нет перекрытия смен

    wd = None  #:None|WDuty
    result = []
    for i, ss in enumerate(durations_at_moment):
        if ss > 0:
            if (wd is None) or wd.finished:
                wd = WDuty(start=i, display_h=result_height)
            else:
                wd.prolongate()
        else:
            if (wd is not None) and (not wd.finished):
                wd.finish()
                result.append(wd)
    return result


def merge_duties(duty_list: List[WDuty]):
    height_lists = get_height_lits(duty_list)

    result = []
    for _height, _dlist in height_lists.items():
        result += _merge(_dlist)
    return result


def get_height_lits(duty_list: List[WDuty]) -> Dict[int, List[WDuty]]:
    height_lists = {}
    for _dw in duty_list:
        _h = _dw.display_h
        lst = height_lists.get(_h, None)
        if lst:
            lst.append(_dw)
        else:
            height_lists[_h] = [_dw]
    return height_lists
