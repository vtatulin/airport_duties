import matplotlib.pyplot as plt


def plot_duty_list(duty_list: list):
    x_points, y_points = [], []
    for i, p in enumerate(duty_list):
        x_points.append(i)
        x_points.append(i + 1)
        y_points.append(p)
        y_points.append(p)
    plt.plot(x_points, y_points)
