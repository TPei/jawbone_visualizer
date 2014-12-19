__author__ = 'TPei'
from tkinter import *

from data.manager import *


class App:
    def __init__(self, master):
        master.wm_title("Jawbone Visualizer")
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
        self.cpw = Button(master,
                          width=self.button_width,
                         text="Average Coffee per Weekday",
                         command=self.coffee_per_weekday)
        self.cpw.pack()
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
        self.svc = Button(master,
                          width=self.button_width,
                         text="Sleep's effect on coffee",
                         command=self.sleep_vs_coffee)
        self.svc.pack()
        Label(master, text="OR").pack(anchor=W)
        self.composite_sleep = IntVar()
        self.composite_coffee = IntVar()
        self.composite_steps = IntVar()
        Label(master, text="Create a composite line chart").pack(anchor=W)
        Checkbutton(master, text="Sleep", variable=self.composite_sleep).pack(anchor=W)
        Checkbutton(master, text="Coffee", variable=self.composite_coffee).pack(anchor=W)
        Checkbutton(master, text="Steps", variable=self.composite_steps).pack(anchor=W)
        self.cvs = Button(master,
                          width=self.button_width,
                         text="Create",
                         command=self.composite).pack()

    def coffee_vs_sleep(self):
        coffee_effect_sleep(get_all_the_data())

    def sleep_vs_coffee(self):
        sleep_effect_on_coffee(get_all_the_data())

    def sleep(self):
        plot_sleep()

    def steps(self):
        plot_step_graph()

    def sleep_per_weekday(self):
        visualize_sleep_per_weekday()

    def coffee_per_weekday(self):
        visualize_coffee_per_weekday()

    def composite(self):
        values = []
        if self.composite_sleep.get() == 1:
            values.append(1)

        if self.composite_coffee.get() == 1:
            values.append(3)

        if self.composite_steps.get() == 1:
            values.append(2)

        plot_all(get_all_the_data(), values)

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