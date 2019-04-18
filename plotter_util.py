import json
import urllib.request
from datetime import datetime
import re

def get_usage(url) -> ([],[]):
    with urllib.request.urlopen(url) as url_result:
        data = json.loads(url_result.read().decode())
        plot_data = []
        time_data = []
        data_dict = {}
        import_data = [source for source in data if 'disabled' in source][0]
        for (time, value) in import_data['values']:
            data_dict[time] = value
        enabled_sources = [source for source in data if not 'disabled' in source]
        for energy_source in enabled_sources:
            for (time, value) in energy_source['values']:
                data_dict[time] += value
        for key, value in data_dict.items():
            plot_data.append(value)
            time_data.append(datetime.fromtimestamp(time / 1000))
        return time_data, plot_data

def get_plot_data(url, lang='en', excluded_sources=[], include_usage=False) -> ([],[],[],[]):
    with urllib.request.urlopen(url) as url_result:
        data = json.loads(url_result.read().decode())
        plot_data = []
        plot_color = []
        time_data = []
        plot_labels = []
        enabled_sources = [source for source in data if 'disabled' not in source]
        enabled_sources = [source for source in enabled_sources if not source['key'][0][lang] in excluded_sources]
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

def set_size(width, fraction=1):
    """ Set aesthetic figure dimensions to avoid scaling in latex.

    Parameters
    ----------
    width: float
            Width in pts
    fraction: float
            Fraction of the width which you wish the figure to occupy

    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    # Width of figure
    fig_width_pt = width * fraction

    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    golden_ratio = (5**.5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * golden_ratio

    fig_dim = (fig_width_in, fig_height_in)

    return fig_dim

nice_fonts = {
        # Use LaTex to write all text
        "text.usetex": True,
        "font.family": "serif",
        # Use 10pt font in plots, to match 10pt font in document
        "axes.labelsize": 10,
        "font.size": 10,
        # Make the legend/label fonts a little smaller
        "legend.fontsize": 8,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
}

