import argparse
import matplotlib.pyplot as plt

from plotter_util import get_url, get_plot_data

parser = argparse.ArgumentParser(description="An easy way to plot data from energy-charts.com using matplotlib...")
parser.add_argument('--plot_lang', type=str, help="The plot language", default='en', choices=['en', 'de', 'fr', 'it'])
parser.add_argument('--month', dest='plot_month', action='store_true')
parser.set_defaults(plot_month=False)
parser.add_argument('year', default=2018, type=int, help="The year. Default: 2018")
parser.add_argument('index', default=1, type=int, help="The index. (week n / month n) Default: 1")
args = vars(parser.parse_args())

plt.ylabel("Produced electricity in GW")

url = get_url(args['year'], int(args['index']), args['plot_month'])
(time_data, plot_data, plot_labels, plot_color) = get_plot_data(url, args['plot_lang'])
plt.stackplot(time_data, plot_data, labels=plot_labels, colors=plot_color)
plt.legend()
plt.show()

