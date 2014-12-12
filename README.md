jawbone_visualizer
========================

Visualize metrics recorded by the jawbone up band

Uses either a provided .json file with all tracked sleeps / daily moves,
which can be obtained by using the jawbone api call "https://jawbone.com/nudge/api/v.1.1/users/@me/sleeps"
or "https://jawbone.com/nudge/api/v.1.1/users/@me/moves"
and then be saved as a json file

or uses the IFTTT recipe that backs up the general sleep metrics recorded by the jawbone up band
which can be downloaded as a csv file

Just add sleep.json or sleep.csv to the res folder
Moves should be saved as moves.json

Creates a visualisation like so:
![Github languages](https://github.com/TPei/jawbone_sleep_visualizer/blob/master/img/sleep.png)
![Github languages](https://github.com/TPei/jawbone_sleep_visualizer/blob/master/img/average_sleep_per_weekday.png)
![Github languages](https://github.com/TPei/jawbone_sleep_visualizer/blob/master/img/steps.png)