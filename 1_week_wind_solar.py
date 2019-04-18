import matplotlib.pyplot as plt
from plotter_util import *

plt.style.use('seaborn')
width = 345
print(set_size(width))
fig, (ax, ax2) = plt.subplots(1, 2, figsize=(6.3, 4))
fig.suptitle("Produced electricity in Germany after fuels: Wind and Solar only")

excluded_sources = ['Hydro Power', 'Biomass', 'Uranium', 'Brown Coal', 'Hard Coal', 'Gas', 'Others', 'Pumped Storage',
                    'Seasonal Storage', 'Oil']

url = get_url(2018, 4, False)
time, data, legend, colors = get_plot_data(url, excluded_sources=excluded_sources)
_, usage = get_usage(url)

ax.plot(time, usage, label='usage', color='r')
ax.stackplot(time, data, labels=legend, colors=colors)
ax.set_xlim(time[0], time[-1])
ax.set_ylim(0, 80)
ax.set_facecolor('w')
ax.set_ylabel("Produced electricity in GW")
for tick in ax.get_xticklabels():
    tick.set_rotation(45)
#ax.legend(loc='upper center', ncol=4, bbox_to_anchor=(0.5, -0.25))

url = get_url(2018, 34, False)
time, data, legend, colors = get_plot_data(url, excluded_sources=excluded_sources)
_, usage = get_usage(url)

ax2.plot(time, usage, label='usage', color='r')
ax2.stackplot(time, data, labels=legend, colors=colors)
ax2.set_xlim(time[0], time[-1])
ax2.set_ylim(0, 80)
ax2.set_facecolor('w')
plt.figlegend(loc='upper center', ncol=4, bbox_to_anchor=(0.5, -0.25))
for tick in ax2.get_xticklabels():
    tick.set_rotation(45)

plt.grid(True)
plt.savefig("test.pdf", format='pdf', bbox_inches='tight')

print("Test")

