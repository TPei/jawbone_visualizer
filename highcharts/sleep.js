$(function () {
    var to_hours = function(seconds) {
        hrs = seconds / 60 / 60;
        return Math.round(hrs * 100) / 100;
    };

    var average = function(array) {
        sum = 0;
        for(var x = 0; x < array.length; x ++) {
            sum = sum + array[x];  //or Sum += scores[x];
        }

        return (sum / array.length);  //length of the array scores is in scores.length
    };

    var decimal_two = function(value){
        return Math.round(value * 100) / 100;
    };

    var array_sum = function(array){
        var sum = 0;
        for(var i = 0; i < array.length; i++){
            sum += array[i];
        }
        return sum;
    };

    var moving_average = function(array, n){
        /** calculates the n-day average of array */
        var mov_avg = [];

        if(n > array.length)
            return [array.length];

        /*
        until we can calculate the n day average, we'll calculate the
        average of all available entries for each entriy
        => 1st element
         */
        for(var count = 1; count < n; count++){
            var suba = array.slice(0, count);
            var subs = array_sum(suba);

            mov_avg.push(subs / suba.length);
        }

        for(var i = 0; i < array.length - n; i++){
            var subarray = array.slice(i, i+n);
            var subsum = array_sum(subarray);

            mov_avg.push(subsum / subarray.length);
        }

        return mov_avg;

    };
    /**
     * parse json
     */
    $.getJSON('../res/sleep.json', function(json) {
        var items = json.data.items;
        var bed = [];
        var total = [];
        var sound = [];
        var light = [];
        var awake = [];

        /*
        had a night where I deactivated sleep in between,
        this would count as two nights here
         */
        jQuery.each(items, function(i, val) {
            bed.push(to_hours(val.details.duration));
            total.push(to_hours(val.details.light + val.details.sound));
            sound.push(to_hours(val.details.sound));
            light.push(to_hours(val.details.light));
            awake.push(to_hours(val.details.awake));
        });

        // reverse because json is ordered latest -> oldest
        bed.reverse();
        total.reverse();
        sound.reverse();
        light.reverse();
        awake.reverse();

        // get the seven day sleep average (moving average)
        seven_day_sleep_average = moving_average(total, 7);

        $('#container').highcharts({
            title: {
                text: 'Sleep per night',
                x: -20 //center
            },
            subtitle: {
                text: 'Source: Jawbone UP24',
                x: -20
            },
            xAxis: {
                title: {
                    text: 'Number of Nights'
                }
                /*categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']*/
            },
            yAxis: {
                title: {
                    text: 'Hours of Sleep'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }],
                floor: 0

            },
            tooltip: {
                valueSuffix: ' hrs'
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle',
                borderWidth: 0
            },
            series: [{
                name: 'Time in Bed',
                data: bed,
                visible: false
            }, {
                name: 'Total Sleep',
                data: total
            }, {
                name: 'Sound Sleep',
                data: sound,
                visible: false
            }, {
                name: 'Light Sleep',
                data: light,
                visible: false
            }, {
                name: 'Awake',
                data: awake,
                visible: false
            }, {
                name: '7day average',
                data: seven_day_sleep_average
            }]
        });

        $('#bar_container').highcharts({
            chart: {
                type: 'column'
            },
            title: {
                text: 'Average Sleep per Cycle'
            },
            subtitle: {
                text: 'Source: Jawbone UP24'
            },
            yAxis: {
                title: {
                    text: 'Hours of Sleep'
                }
            },
            xAxis: {
                title: {
                    text: 'Sleep Type'
                }
            },
            tooltip: {
                valueSuffix: ' hrs'
            },
            plotOptions: {
                bar: {
                    dataLabels: {
                        enabled: true
                    }
                }
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'top',
                y: 80,
                floating: true,
                borderWidth: 1,
                backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
                shadow: true
            },
            credits: {
                enabled: false
            },
            series: [{
                name: 'Time in Bed',
                data: [decimal_two(average(bed))]
            }, {
                name: 'Total Sleep',
                data: [decimal_two(average(total))]
            }, {
                name: 'Sound Sleep',
                data: [decimal_two(average(sound))]
            }, {
                name: 'Light Sleep',
                data: [decimal_two(average(light))]
            }, {
                name: 'Awake Sleep',
                data: [decimal_two(average(awake))]
            }]
        });

    });

});