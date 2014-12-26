__author__ = 'TPei'
from abc import ABCMeta, abstractmethod
import matplotlib.pyplot as plt


class Plot(metaclass=ABCMeta):
    """
    abstract plot superclass
    """

    def set_ydata(self, ydata):
        """
        setter of ydata
        :param ydata:
        :return:
        """
        self.ydata = ydata

    def set_xdata(self, xdata):
        """
        setter of xdata
        :param xdata:
        :return:
        """
        self.xdata = xdata

    @abstractmethod
    def get_plot_data(self):
        """
        each plot subclass should support
        the get plot data action
        :return:
        """
        pass

    @abstractmethod
    def plot(self):
        """
        each plot subclass should support
        the plotting action
        :return:
        """
        pass