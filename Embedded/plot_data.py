import time
import math
from collections import deque, defaultdict

import matplotlib.animation as animation
from matplotlib import pyplot as plt

import threading

from random import randint

from statistics import *


class DataPlot:
    def __init__(self, max_entries=10):
        self.axis_x = deque(maxlen=max_entries)
        self.axis_y = deque(maxlen=max_entries)
        self.axis_y2 = deque(maxlen=max_entries)
        self.axis_y3 = deque(maxlen=max_entries)
        self.axis_y4 = deque(maxlen=max_entries)

        self.max_entries = max_entries

        self.buf1 = deque(maxlen=5)
        self.buf2 = deque(maxlen=5)
        self.buf3 = deque(maxlen=5)
        self.buf4 = deque(maxlen=5)

    def add(self, x, y, y2, y3, y4):
        self.axis_x.append(x)
        self.axis_y.append(y)
        self.axis_y2.append(y2)
        self.axis_y3.append(y3)
        self.axis_y4.append(y4)


class DataPlot2:
    def __init__(self, max_entries=10):
        self.axis_x = deque(maxlen=max_entries)
        self.axis_y = deque(maxlen=max_entries)

        self.max_entries = max_entries
        self.buf1 = deque(maxlen=5)

    def add2(self, x, y):
        self.axis_x.append(x)
        self.axis_y.append(y)


class RealtimePlot:
    def __init__(self, axes):
        self.axes = axes

        self.lineplot, = axes.plot([], [], "rx-")
        self.lineplot2, = axes.plot([], [], "gx-")
        self.lineplot3, = axes.plot([], [], "bx-")
        self.lineplot4, = axes.plot([], [], "yx-")

    def plot(self, dataPlot):
        self.lineplot.set_data(dataPlot.axis_x, dataPlot.axis_y)
        self.lineplot2.set_data(dataPlot.axis_x, dataPlot.axis_y2)
        self.lineplot3.set_data(dataPlot.axis_x, dataPlot.axis_y3)
        self.lineplot4.set_data(dataPlot.axis_x, dataPlot.axis_y4)

        self.axes.set_xlim(min(dataPlot.axis_x), max(dataPlot.axis_x))
        ymin = min([min(dataPlot.axis_y), min(dataPlot.axis_y2), min(dataPlot.axis_y3), min(dataPlot.axis_y4)]) - 2
        ymax = max([max(dataPlot.axis_y), max(dataPlot.axis_y2), max(dataPlot.axis_y3), max(dataPlot.axis_y4)]) + 2
        self.axes.set_ylim(ymin, ymax)
        self.axes.relim();


class RealtimePlot2:
    def __init__(self, axes):
        self.axes = axes

        self.lineplot, = axes.plot([], [], "co-")

    def plot2(self, dataPlot):
        self.lineplot.set_data(dataPlot.axis_x, dataPlot.axis_y)

        self.axes.set_xlim(min(dataPlot.axis_x), max(dataPlot.axis_x))
        self.axes.set_ylim(min(dataPlot.axis_y), max(dataPlot.axis_y))
        self.axes.relim();


def main():
    fig, axes = plt.subplots()
    plt.title('Pixy Cam Plotting Data')
    data = DataPlot();
    dataPlotting = RealtimePlot(axes)

    try:
        count = 0
        while True:
            count += 1
            data.add(count, 60 + 1 / randint(1, 5), 33)
            dataPlotting.plot(data)

            plt.pause(0.001)
    except KeyboardInterrupt:
        print('\n\nKeyboard exception received. Exiting.')
        plt.close()
        ser.close()
        exit()


if __name__ == "__main__": main()
