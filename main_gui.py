__author__ = 'TPei'
from tkinter import *

from data.manager import *


class App:
    def __init__(self, master):
        self.button_width = 25
        self.description = Label(master, text="Please choose a visualization mode:")
        self.description.pack()
        self.sleep = Button(master,
                            width=self.button_width,
                         text="Nightly Sleep over time",
                         command=self.sleep)
        self.sleep.pack()
        self.spw = Button(master,
                          width=self.button_width,
                         text="Average Sleep per Weekday",
                         command=self.sleep_per_weekday)
        self.spw.pack()
        self.steps = Button(master,
                            width=self.button_width,
                         text="Daily Steps over time",
                         command=self.steps)
        self.steps.pack()
        self.cvs = Button(master,
                          width=self.button_width,
                         text="Coffee's effect on sleep",
                         command=self.coffee_vs_sleep)
        self.cvs.pack()

    def coffee_vs_sleep(self):
        coffee_effect_sleep(get_all_the_data())

    def sleep(self):
        plot_sleep()

    def steps(self):
        plot_step_graph()

    def sleep_per_weekday(self):
        visualize_sleep_per_weekday()

root = Tk()
app = App(root)
root.mainloop()

'''
visualize_sleep_per_weekday()
plot_sleep()
plot_step_graph()
plot_all(get_all_the_data())
print(get_all_the_data('awake_time'))
compareDicts(get_all_the_data(), get_all_the_data('awake_time'))
coffee_effect_sleep(get_all_the_data())
'''