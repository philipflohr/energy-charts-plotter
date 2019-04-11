import argparse
import json
import urllib.request
from datetime import datetime
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser(description="An easy way to plot data from energy-charts.com using matplotlib...")
parser.add_argument('--month', dest='plot_month', action='store_true')
parser.set_defaults(plot_month=False)
parser.add_argument('year', default=2018, type=int, help="The year. Default: 2018")
parser.add_argument('index', default=1, type=int, help="The index. (week n / month n) Default: 1")
args = vars(parser.parse_args())

plt.ylabel("Produced electricity in GW")
plt.legend()

url = 'https://energy-charts.de/power/'
if args['plot_month']:
    pass
else:
    url += 'week_' + str(args['year']) + '_' + str(int(args['index'])).zfill(2) + '.json'
#rint(url)

with urllib.request.urlopen(url) as url_result:
    data = json.loads(url_result.read().decode())
    plot_data = []
    time_data = []
    plot_labels = []
    enabled_sources = [source for source in data if 'disabled' not in source]
    for energy_source in enabled_sources:
        source = energy_source['key'][0]['en']
        plot_labels.append(source)
        color = energy_source['color']
        values = energy_source['values']
        time_list = []
        value_list = []
        for [time, value] in values:
            time_list.append(datetime.fromtimestamp(time/1000))
            value_list.append(value)
        time_data = time_list.copy()
        plot_data.append(value_list)
        time_list.clear()
    plt.stackplot(time_data, plot_data, labels=plot_labels)
    plt.show()

