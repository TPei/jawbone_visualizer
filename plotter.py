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


def plot_line_graph(time_in_bed, total_sleep, deep_sleep, light_sleep, no_sleep, labels=[]):
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
    line_total, = plt.plot(total_sleep, label='Total Sleep', linewidth=6.0)
    line_in_bed, = plt.plot(time_in_bed, label='Time in Bed')
    line_deep, = plt.plot(deep_sleep, label='Deep Sleep', linestyle='--', linewidth=4.0)
    line_light, = plt.plot(light_sleep, label='Light Sleep', linestyle='-.', linewidth=4.0)
    line_awake, = plt.plot(no_sleep, label='Awake')
    #plt.legend(handles=[line_in_bed, line_total, line_deep, line_light, line_awake])
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1,
           ncol=2, mode="expand", borderaxespad=0.)
    plt.ylabel('Sleep Duration in Hours')

    # set ylim to max total_sleep + 10%
    plt.ylim(0, max(time_in_bed) + (max(time_in_bed) / 8))
    plt.show()


def composite_line_bar(time_in_bed, total_sleep, deep_sleep, light_sleep, no_sleep, labels=[]):
    ax = plt.subplot2grid((3,3), (0,0), colspan=2, rowspan=3)
    line_total, = plt.plot(total_sleep, label='Total Sleep', linewidth=6.0)
    line_in_bed, = plt.plot(time_in_bed, label='Time in Bed')
    line_deep, = plt.plot(deep_sleep, label='Deep Sleep', linestyle='--', linewidth=4.0)
    line_light, = plt.plot(light_sleep, label='Light Sleep', linestyle='-.', linewidth=4.0)
    line_awake, = plt.plot(no_sleep, label='Awake')
    #plt.legend(handles=[line_in_bed, line_total, line_deep, line_light, line_awake])
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1,
           ncol=2, mode="expand", borderaxespad=0.)
    plt.ylabel('Sleep Duration in Hours')

    # set ylim to max total_sleep + 10%
    plt.ylim(0, max(time_in_bed) + (max(time_in_bed) / 8))
    #plt.show()


    ################
    ## bar chart ##
    ################
    ax = plt.subplot2grid((3,3), (0, 2), rowspan=3)

    ## necessary variables
    ind = np.arange(5)
    width = 0.5


    try:
        offset = max(total_sleep) / 20
        ## the bars


        bars2 = []
        bars2.append(sum(time_in_bed)/float(len(time_in_bed)))
        bars2.append(sum(total_sleep)/float(len(total_sleep)))
        bars2.append(sum(deep_sleep)/float(len(deep_sleep)))
        bars2.append(sum(light_sleep)/float(len(light_sleep)))
        bars2.append(sum(no_sleep)/float(len(no_sleep)))

        '''
         time_in_bed = [(sum(time_in_bed)/float(len(time_in_bed)))]
        total_sleep = [(sum(total_sleep)/float(len(total_sleep)))]
        deep_sleep = [(sum(deep_sleep)/float(len(deep_sleep)))]
        light_sleep = [(sum(light_sleep)/float(len(light_sleep)))]
        no_sleep = [(sum(no_sleep)/float(len(no_sleep)))]
        '''

        bars = ax.bar(ind, bars2, width, alpha=0.7, color='r')


        # three subbars stacked to meat the total_time
        p0 = plt.bar(ind, bars2, width)
        #p00 = plt.bar(ind, total_sleep, width)
        #p1 = plt.bar(ind, deep_sleep, width)
        #p2 = plt.bar(ind, light_sleep, width)
        #p3 = plt.bar(ind, no_sleep, width)

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
        xTickMarks = ['in bed', 'asleep', 'deep sleep', 'light sleep', 'awake']
        ax.set_xticks(ind+(width/2))
        xtickNames = ax.set_xticklabels(xTickMarks)
        #plt.setp(xtickNames, rotation=-45, fontsize=10)

        # add label
        #plt.legend((p1[0], p2[0], p3[0]), ('Deep Sleep', 'Light Sleep', 'Awake'))


        plt.show()
    except ValueError:
        print("no data was found")