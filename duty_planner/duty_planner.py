"""
непосредственно, планировщик

"""
from basic_duties.__w_duty import WDuty

class DutyPlaner():
    def __init__(self, duties_list):
        self.duty_list = duties_list
        self.max_load = max(duties_list)
        self.min_load = min(duties_list)

    def calculate_duties(self):
        self.result = []
        w_duty = None
        for H in range(self.min_load+1, self.max_load+1):
            for t_i in range(len(self.duty_list)): ##t_i - индекс времени
                if self.duty_list[t_i] >= H:
                    if (w_duty is None) or w_duty.finished:
                        w_duty = WDuty(start=t_i, display_h=H)
                    else:
                        w_duty.prolongate()
                else:
                    if (w_duty is not None):
                        w_duty.finish()
                        self.result.append(w_duty)
        return self.result



