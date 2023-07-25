
import matplotlib.pyplot as plt
from duty_planner.duty_planner import  DutyPlaner
import basic_duties
import basic_plot

def calculate_schedule_n_plot():
    duty = [0, 12, 13, 16, 20, 40, 38, 39, 20, 10, 8, 6, 12, 30, 40, 43, 38, 45, 56, 40, 30, 21, 11, 7, 0, 11, 12, 5
            ]
    # duty = [0,0]
    # duty = [0,2,0,0,3]
    min_duty_duration = 4
    dp = DutyPlaner(duty)
    worker_duties = dp.calculate_duties()

    basic_duties.prolongate_duties_except_last(worker_duties, min_duty_duration)
    worker_duties = basic_duties.merge_duties(worker_duties)
    basic_duties.prolongate_duties(worker_duties, min_duty_duration)
    basic_plot.plot_duty_list(duty)
    basic_plot.plot_worker_duties(worker_duties)

    duties_sum = sum(_.duration for _ in worker_duties)
    work_sum = sum(duty)
    title = f"""Duties: {duties_sum} man*duty;work ammount: {work_sum}
    ratio: {round(100 * duties_sum / work_sum, 2)}    """
    plt.title(title)
    plt.show()

if __name__ == '__main__':
    calculate_schedule_n_plot()

