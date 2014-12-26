__author__ = 'TPei'
import matplotlib.pyplot as plt
from plotting.Plot import Plot


class LineGraph(Plot):
    """
    representing a line graph
    """

    def __init__(self, data=None):
        """
        :param data: data dict {'xdata': [...], 'ydata': [...]}
        sets ydata and xdata
        :return:
        """
        self.data = data
        self.ydata = []
        self.xdata = []

        if 'xdata' in data:
            self.xdata = data['xdata']

        if 'ydata' in data:
            self.ydata = data['ydata']

    def get_plot_data(self):
        """
        depending on whether or not there is y and xdata available
        plot plots accordingly
        :return: plt
        """
        if len(self.ydata) == 0:
            return plt
        if len(self.ydata) == len(self.xdata):
            if not isinstance(self.ydata[0], list):
                plt.plot(self.xdata, self.ydata)
            else:
                for i in range(0, len(self.ydata)):
                    plt.plot(self.xdata[i], self.ydata[i])
        else:
            if not isinstance(self.ydata[0], list):
                plt.plot(self.ydata)
            else:
                for date in self.ydata:
                    plt.plot(date)

        return plt

    def plot(self):
        self.get_plot().show()

if __name__ == '__main__':
    line = LineGraph({'xdata': [1, 2, 3, 4, 5], 'ydata': [1, 4, 9, 16, 25]})
    #plt = line.get_plot()
    #plt.show()
    line.plot()