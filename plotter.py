__author__ = 'TPei'
import matplotlib.pyplot as plt
import numpy as np


def plot_bar_chart(total_sleep, deep_sleep, light_sleep, no_sleep, labels=[]):
    fig = plt.figure('sleep')
    ax = fig.add_subplot(111)


    ## necessary variables
    ind = np.arange(len(total_sleep))
    width = 0.5

    try:
        offset = max(total_sleep) / 20
        ## the bars
        bars = ax.bar(ind, total_sleep, width, alpha=0.7, color='r')
        p1 = plt.bar(ind, deep_sleep,   width, color='r')
        p2 = plt.bar(ind, light_sleep, width, color='y', bottom=deep_sleep)
        p3 = plt.bar(ind, no_sleep, width, color='g', bottom=[deep_sleep[j] + light_sleep[j] for j in range(len(deep_sleep))])
        for rect in bars:
            height = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., offset+height, '%d' % height,
                    ha='center', va='bottom')

        # axes and labels
        ax.set_xlim(-width, len(ind)+width)
        ax.set_ylim(0, max(total_sleep) + max(total_sleep) / 10)
        ax.set_ylabel('total sleep in seconds per night')
        ax.set_title('Sleep Duration per day')
        xTickMarks = labels
        ax.set_xticks(ind+(width/2))
        xtickNames = ax.set_xticklabels(xTickMarks)
        plt.setp(xtickNames, rotation=-45, fontsize=10)
        plt.legend((p1[0], p2[0], p3[0]), ('Deep Sleep', 'Light Sleep', 'Awake'))
        plt.show()
    except ValueError:
        print("no data was found")