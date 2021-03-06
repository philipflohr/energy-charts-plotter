import matplotlib as mpl
import matplotlib.pyplot as plt
from plotter_util import *

url = get_url(2018,4,False)
time, data, legend, colors = get_plot_data(url)

mpl.rcParams.update(nice_fonts)

fig, ax = plt.subplots(1, 1, figsize=(6.3, 4))

# Plot
ax.stackplot(time, data, labels=legend, colors=colors)
ax.set_xlim(time[0], time[-1])
plt.xticks(rotation=45)
ax.set_facecolor('w')
fig.suptitle("Produced electricity in Germany after fuels")
ax.set_ylabel("Produced electricity in GW")
ax.legend(loc='upper center', ncol=4, bbox_to_anchor=(0.5, -0.25))
plt.savefig("test.pdf", format='pdf', bbox_inches='tight')

print("Source: " + url)

