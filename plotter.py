__author__ = 'TPei'
import matplotlib.pyplot as plt
import numpy as np


def plot_bar_chart(total_sleep, deep_sleep, light_sleep, no_sleep, labels=[]):
    """
    plot a bar chart where the total sleep bar is made up out of
    deep sleep + light sleep + no sleep bars stacked on top of each other
    :param total_sleep:
    :param deep_sleep:
    :param light_sleep:
    :param no_sleep:
    :param labels:
    :return:
    """
    fig = plt.figure('sleep')
    ax = fig.add_subplot(111)


    ## necessary variables
    ind = np.arange(len(total_sleep))
    width = 0.5

    try:
        offset = max(total_sleep) / 20
        ## the bars
        bars = ax.bar(ind, total_sleep, width, alpha=0.7, color='r')


        # three subbars stacked to meat the total_time
        p1 = plt.bar(ind, deep_sleep,   width, color='#002EB8')
        p2 = plt.bar(ind, light_sleep, width, color='#005CE6', bottom=deep_sleep)
        p3 = plt.bar(ind, no_sleep, width, color='#FF4719', bottom=[deep_sleep[j] + light_sleep[j] for j in range(len(deep_sleep))])

        # add value label at the top of the stacked bars
        for rect in bars:
            height = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., offset+height, '%d' % height,
                    ha='center', va='bottom')

        # axes and labels
        ax.set_xlim(-width, len(ind)+width)
        ax.set_ylim(0, max(total_sleep) + max(total_sleep) / 10)
        ax.set_ylabel('total sleep in hours per night')
        ax.set_title('Sleep Duration per night')
        xTickMarks = labels
        ax.set_xticks(ind+(width/2))
        xtickNames = ax.set_xticklabels(xTickMarks)
        plt.setp(xtickNames, rotation=-45, fontsize=10)

        # add label
        plt.legend((p1[0], p2[0], p3[0]), ('Deep Sleep', 'Light Sleep', 'Awake'))


        plt.show()
    except ValueError:
        print("no data was found")


def plot_line_graph(total_sleep, deep_sleep, light_sleep, no_sleep, labels=[]):
    """
    create a line graph with total sleep,
    deep sleep, light sleep and awake time
    :param total_sleep:
    :param deep_sleep:
    :param light_sleep:
    :param no_sleep:
    :param labels:
    :return:
    """
    ax = plt.subplot(111)
    line_total, = plt.plot(total_sleep, label='Total Sleep')
    line_deep, = plt.plot(deep_sleep, label='Deep Sleep', linestyle='--')
    line_light, = plt.plot(light_sleep, label='Light Sleep', linestyle='-.')
    line_awake, = plt.plot(no_sleep, label='Awake')
    #plt.legend(handles=[line_total, line_deep, line_light, line_awake])
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1,
           ncol=2, mode="expand", borderaxespad=0.)
    plt.ylabel('Sleep Duration in Hours')

    # set ylim to max total_sleep + 10%
    plt.ylim(0, max(total_sleep) + (max(total_sleep) / 10))
    plt.show()
    print("daym")