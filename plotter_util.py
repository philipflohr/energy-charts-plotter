import json
import urllib.request
from datetime import datetime
import re


def get_plot_data(url, lang='en') -> ([],[],[],[]):
    with urllib.request.urlopen(url) as url_result:
        data = json.loads(url_result.read().decode())
        plot_data = []
        plot_color = []
        time_data = []
        plot_labels = []
        enabled_sources = [source for source in data if 'disabled' not in source]
        for energy_source in enabled_sources:
            source = energy_source['key'][0][lang]
            plot_labels.append(source)
            color_list = re.split('[(),]', energy_source['color'])
            plot_color.append([int(s) / 256 for s in color_list if s.isdigit()])
            values = energy_source['values']
            time_list = []
            value_list = []
            for [time, value] in values:
                time_list.append(datetime.fromtimestamp(time / 1000))
                value_list.append(value)
            time_data = time_list.copy()
            plot_data.append(value_list)
    return time_data, plot_data, plot_labels, plot_color


def get_url(year: int, index: int, plot_month: bool) -> str:
    url = 'https://energy-charts.de/power/'
    if plot_month:
        url += 'month_' + str(year) + '_' + str(index).zfill(2) + '.json'
    else:
        url += 'week_' + str(year) + '_' + str(index).zfill(2) + '.json'
    return url