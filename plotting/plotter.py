__author__ = 'TPei'
import matplotlib.pyplot as plt
import numpy as np


def plot_bar_chart(title, ylabel, keys, values):
    """
    creates a bar chart for the given data
    :param title: title to display
    :param ylabel: ylabel text
    :param keys: names for the bars
    :param values: values to create bars for
    :param user: the user which we are visualizing here
    :return:
    """
    fig = plt.figure(title)
    ax = fig.add_subplot(111)


    ## necessary variables
    ind = np.arange(len(values))
    width = 0.5

    try:
        offset = max(values) / 20
        ## the bars
        bars = ax.bar(ind, values, width, alpha=0.7, color='r')
        for rect in bars:
            height = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., offset+height, '%.2f' % height,
                    ha='center', va='bottom')

        # axes and labels
        ax.set_xlim(-width, len(ind)+width)
        ax.set_ylim(0, max(values) + max(values) / 10)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        xTickMarks = keys
        ax.set_xticks(ind+(width/2))
        xtickNames = ax.set_xticklabels(xTickMarks)
        plt.setp(xtickNames, rotation=-45, fontsize=10)
        plt.show()
    except ValueError:
        print("no data was found")


def plot_sleep_per_weekday(title, ylabel, keys, values, counter, color_list):
    """
    creates a bar chart for the given data
    :param title: title to display
    :param ylabel: ylabel text
    :param keys: names for the bars
    :param values: values to create bars for
    :param user: the user which we are visualizing here
    :return:
    """
    fig = plt.figure(title)
    ax = fig.add_subplot(111)


    ## necessary variables
    ind = np.arange(len(values))
    width = 0.5

    try:
        offset = max(values) / 20
        ## the bars
        bars = ax.bar(ind, values, width, color=color_list)
        for rect in bars:
            height = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., offset+height, '%.2f' % height,
                    ha='center', va='bottom')

        # axes and labels
        ax.set_xlim(-width, len(ind)+width)
        ax.set_ylim(0, max(values) + max(values) / 10)
        ax.set_ylabel(ylabel)
        ax.set_title(title + "\n (based on " + str(sum(counter)) + " nights of sleep data)")
        xTickMarks = keys
        ax.set_xticks(ind+(width/2))
        xtickNames = ax.set_xticklabels(xTickMarks)
        plt.setp(xtickNames, rotation=-45, fontsize=10)
        plt.legend((bars[0], bars[-1]), ('Weeknights', 'Weeekends'), loc=4)
        plt.show()
    except ValueError:
        print("no data was found")


def plot_sleep_bars(total_sleep, deep_sleep, light_sleep, no_sleep, labels=[]):
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

    averages = []

    for i in range(1, len(total_sleep)+1):
        averages.append(sum(total_sleep[0:i]) / float(len(total_sleep[0:i])))

    fig, ax = plt.subplots()
    ax = plt.subplot2grid((3,3), (0,0), colspan=2, rowspan=3)
    line_total, = plt.plot(total_sleep, label='Total Sleep', linewidth=6.0)
    line_in_bed, = plt.plot(time_in_bed, label='Time in Bed')
    line_deep, = plt.plot(deep_sleep, label='Deep Sleep', linestyle='--', linewidth=4.0)
    line_light, = plt.plot(light_sleep, label='Light Sleep', linestyle='-.', linewidth=4.0)
    line_awake, = plt.plot(no_sleep, label='Awake')
    line_averages, = plt.plot(averages, label='Average')
    #plt.legend(handles=[line_in_bed, line_total, line_deep, line_light, line_awake])
    leg = plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1,
           ncol=2, mode="expand", borderaxespad=0.)

    lines = [line_total, line_in_bed, line_deep, line_light, line_awake, line_averages]

    lined = dict()
    for legline, origline in zip(leg.get_lines(), lines):
        legline.set_picker(5)  # 5 pts tolerance
        lined[legline] = origline

    def onpick(event):
        # on the pick event, find the orig line corresponding to the
        # legend proxy line, and toggle the visibility
        legline = event.artist
        origline = lined[legline]
        vis = not origline.get_visible()
        origline.set_visible(vis)
        # Change the alpha on the line in the legend so we can see what lines
        # have been toggled
        if vis:
            legline.set_alpha(1.0)
        else:
            legline.set_alpha(0.2)
        fig.canvas.draw()



    fig.canvas.mpl_connect('pick_event', onpick)
    plt.ylabel('Sleep Duration in Hours')
    plt.xlabel('Nights (starting 2014/12/04-05)')

    # set ylim to max total_sleep + 10%
    plt.ylim(0, max(time_in_bed) + (max(time_in_bed) / 8))
    plt.xticks(np.arange(0, len(time_in_bed), 1.0))
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
            ax.text(rect.get_x()+rect.get_width()/2., offset+height, '%.2f' % height,
                    ha='center', va='bottom')

        # axes and labels
        ax.set_xlim(-width, len(ind)+width)
        ax.set_ylim(0, max(total_sleep) + max(total_sleep) / 10)
        ax.set_ylabel('total sleep in hours per night')
        ax.set_title('Average times for sleep cycles')
        xTickMarks = ['in bed', 'asleep', 'deep', 'light', 'awake']
        ax.set_xticks(ind+(width/2))
        xtickNames = ax.set_xticklabels(xTickMarks)
        #plt.setp(xtickNames, rotation=-45, fontsize=10)

        # add label
        #plt.legend((p1[0], p2[0], p3[0]), ('Deep Sleep', 'Light Sleep', 'Awake'))


        plt.show()
    except ValueError:
        print("no data was found")


def steps_line(values, labels=[]):

    # calculate the average per entry
    averages = []

    for i in range(1, len(values)+1):
        averages.append(sum(values[0:i]) / float(len(values[0:i])))

    ax = plt.subplot(111)
    line_total, = plt.plot(values, label='Total Steps', linewidth=4.0)
    line_averages, = plt.plot(averages, label='Average', linewidth=2.0, linestyle='--')
    #plt.legend(handles=[line_in_bed, line_total, line_deep, line_light, line_awake])
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1,
           ncol=2, mode="expand", borderaxespad=0.)

    plt.ylabel('Number of steps per day')
    plt.xlabel('Days (starting 2014/12/04)')

    # set ylim to max total_sleep + 10%
    plt.ylim(0, max(values) + (max(values) / 8))
    plt.xticks(np.arange(0, len(values), 1.0))
    plt.show()


def plot_all(data, choices=[1]):

    import collections

    od = collections.OrderedDict(sorted(data.items()))

    print(od)


    labels = []
    coffee = []
    values = []
    time_in_bed = []
    total_sleep = []
    deep_sleep = []
    light_sleep = []
    no_sleep = []

    for day in od:
        labels.append(od[day]['date'])

        if 'coffee' in od[day]:
            coffee.append(od[day]['coffee'])
        else:
            coffee.append(0)

        if 'steps' in od[day]:
            values.append(od[day]['steps'])
        else:
            values.append(0)

        if 'bed' in od[day]:
            time_in_bed.append(od[day]['bed'])
        else:
            time_in_bed.append(0)

        if 'sleep' in od[day]:
            total_sleep.append(od[day]['sleep'])
        else:
            total_sleep.append(0)

        if 'sound' in od[day]:
            deep_sleep.append(od[day]['sound'])
        else:
            deep_sleep.append(0)

        if 'light' in od[day]:
            light_sleep.append(od[day]['light'])
        else:
            light_sleep.append(0)

        if 'awake' in od[day]:
            no_sleep.append(od[day]['awake'])
        else:
            no_sleep.append(0)


    fig, ax1 = plt.subplots()

    if 3 in choices:

        line_total, = ax1.plot(coffee, color='#ffa500', linewidth=4.0)
        #ax1.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1,
        #       ncol=2, mode="expand", borderaxespad=0.)

        ax1.set_ylabel('Cups of coffee per day', color='#ffa500')
        ax1.set_xlabel('Days (starting 2014/12/04)')

    # --------------------- #
    # ------- steps ------- #
    # --------------------- #
    if 2 in choices:

        ax2 = ax1.twinx()

        # calculate the average per entry
        averages = []

        for i in range(1, len(values)+1):
            averages.append(sum(values[0:i]) / float(len(values[0:i])))

        line_total, = ax2.plot(values, label='Total Steps', color='r', linewidth=4.0)
        line_averages, = ax2.plot(averages, label='Average', linewidth=2.0, linestyle='--')
        #plt.legend(handles=[line_in_bed, line_total, line_deep, line_light, line_awake])
        #plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1,
        #       ncol=2, mode="expand", borderaxespad=0.)

        ax2.set_ylabel('Number of steps per day', color='r')
        ax2.set_xlabel('Days (starting 2014/12/04)')

        # set ylim to max total_sleep + 10%
        #plt.ylim(0, max(values) + (max(values) / 8))

    # --------------------- #
    # ------- sleep ------- #
    # --------------------- #

    if 1 in choices:
        averages = []

        for i in range(1, len(total_sleep)+1):
            averages.append(sum(total_sleep[0:i]) / float(len(total_sleep[0:i])))

        ax3 = ax1.twinx()
        line_total, = ax3.plot(total_sleep, label='Total Sleep', linewidth=6.0)
        line_in_bed, = ax3.plot(time_in_bed, label='Time in Bed')
        line_deep, = ax3.plot(deep_sleep, label='Deep Sleep', linestyle='--', linewidth=4.0)
        line_light, = ax3.plot(light_sleep, label='Light Sleep', linestyle='-.', linewidth=4.0)
        line_awake, = ax3.plot(no_sleep, label='Awake')
        line_averages, = ax3.plot(averages, label='Averages')
        #plt.legend(handles=[line_in_bed, line_total, line_deep, line_light, line_awake])
        ax3.set_ylabel('Sleep Duration in Hours')

        leg = plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1,
               ncol=2, mode="expand", borderaxespad=0.)
        try:
            lines = [line_total, line_in_bed, line_deep, line_light, line_awake, line_averages]

            lined = dict()
            for legline, origline in zip(leg.get_lines(), lines):
                legline.set_picker(5)  # 5 pts tolerance
                lined[legline] = origline

            def onpick(event):
                # on the pick event, find the orig line corresponding to the
                # legend proxy line, and toggle the visibility
                legline = event.artist
                origline = lined[legline]
                vis = not origline.get_visible()
                origline.set_visible(vis)
                # Change the alpha on the line in the legend so we can see what lines
                # have been toggled
                if vis:
                    legline.set_alpha(1.0)
                else:
                    legline.set_alpha(0.2)
                fig.canvas.draw()

            fig.canvas.mpl_connect('pick_event', onpick)
        except Exception:
            print("whoops")

    plt.show()


def coffee_effect_sleep(data):
    '''
    plot a average sleep vs amount of coffee graph
    :param data:
    :return:
    '''
    categories = ['0', '1/2', '3/4', '5+']
    count = [0, 0, 0, 0]
    count_sound = [0, 0, 0, 0]
    count_light = [0, 0, 0, 0]
    count_awake = [0, 0, 0, 0]
    average_counter = [0, 0, 0, 0]
    average = [0, 0, 0, 0]
    average_sound = [0, 0, 0, 0]
    average_light = [0, 0, 0, 0]
    average_awake = [0, 0, 0, 0]

    import collections

    od = collections.OrderedDict(sorted(data.items()))

    category = 'sleep'

    for day in od:

        if 'coffee' in od[day] and category in od[day]:
            #coffee.append(od[day]['coffee'])
            if od[day]['coffee'] == 0:
                count[0] += od[day][category]
                count_sound[0] += od[day]['sound']
                count_light[0] += od[day]['light']
                count_awake[0] += od[day]['awake']
                average_counter[0] += 1
            elif od[day]['coffee'] < 3:
                count[1] += od[day][category]
                count_sound[1] += od[day]['sound']
                count_light[1] += od[day]['light']
                count_awake[1] += od[day]['awake']
                average_counter[1] += 1
            elif od[day]['coffee'] < 5:
                count[2] += od[day][category]
                count_sound[2] += od[day]['sound']
                count_light[2] += od[day]['light']
                count_awake[2] += od[day]['awake']
                average_counter[2] += 1
            else:
                count[3] += od[day][category]
                count_sound[3] += od[day]['sound']
                count_light[3] += od[day]['light']
                count_awake[3] += od[day]['awake']
                average_counter[3] += 1
        else:
            count[0] += od[day][category]
            count_sound[0] += od[day]['sound']
            count_light[0] += od[day]['light']
            count_awake[0] += od[day]['awake']
            average_counter[0] += 1

    #calculate average
    for i in range(0, len(count)):
        average[i] = (count[i] / float(average_counter[i]))
        average_sound[i] = (count_sound[i] / float(average_counter[i]))
        average_light[i] = (count_light[i] / float(average_counter[i]))
        average_awake[i] = (count_awake[i] / float(average_counter[i]))

    fig = plt.figure('Coffee -> Sleep')
    ax = fig.add_subplot(111)


    ## necessary variables
    ind = np.arange(len(average))
    width = 0.5

    try:
        offset = max(average) / 20
        ## the bars
        bars = ax.bar(ind, average, width, alpha=0.7, color='r')
        p1 = plt.bar(ind, average_sound,   width, color='#002EB8')
        p2 = plt.bar(ind, average_light, width, color='#005CE6', bottom=average_sound)
        #p3 = plt.bar(ind, average_awake, width, color='#FF4719', bottom=[average_sound[j] + average_light[j] for j in range(len(average_sound))])
        for rect in bars:
            height = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., offset+height, '%.2f' % height,
                    ha='center', va='bottom')

        # axes and labels
        ax.set_xlim(-width, len(ind)+width)
        ax.set_ylim(0, max(average) + max(average) / 10)
        ax.set_ylabel('Average Sleep Hours')
        ax.set_xlabel('Cups of coffee (respectively based on x occurences)')
        ax.set_title('Effect of coffee on sleep')

        for i in range(0, len(categories)):
            categories[i] += ' (' + str(average_counter[i]) + 'x)'

        xTickMarks = categories
        ax.set_xticks(ind+(width/2))
        xtickNames = ax.set_xticklabels(xTickMarks)
        plt.setp(xtickNames, rotation=0, fontsize=10)
        #plt.legend((p1[0], p2[0], p3[0]), ('Deep Sleep', 'Light Sleep', 'Awake'))
        plt.legend((p1[0], p2[0]), ('Deep Sleep', 'Light Sleep'))
        plt.show()
    except ValueError:
        print("no data was found")

