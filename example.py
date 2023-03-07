#import scKTLD1
#print(scKTLD1.callTLD)

#from scKTLD1 import callTLD
#print(callTLD)

import numpy as np
import sys
import os

import tkinter
import matplotlib
import matplotlib.pyplot as plt
import sklearn.metrics.pairwise as skmetrics
import seaborn as sns

from scKTLD import edge2adj
from scKTLD import callTLD
from scKTLD import displayTLD

matplotlib.use('TkAgg')

hiccolors = ["lightyellow", "red"]
my_cmap = matplotlib.colors.LinearSegmentedColormap.from_list('hicheat', hiccolors)
matplotlib.cm.register_cmap(cmap = my_cmap)
featurecolors = ["blue", "white", "red"]
my_cmap = matplotlib.colors.LinearSegmentedColormap.from_list('featureheat', featurecolors)
matplotlib.cm.register_cmap(cmap = my_cmap)

path_input = "/media/biology/datadisk/schic_datset/Tan2018/50k"

chrs = ["chr" +  c for c in np.append(np.array(range(1,23)),"X")]
cells = os.listdir(path_input)

## call TAD

chr = chrs[2]
cell = cells[1]
print(cell, chr)

graphfile_edge = path_input+"/"+cell+"/"+chr+".txt"
graph_edge = np.loadtxt(graphfile_edge)

graph_adj = edge2adj(graph_edge, chr = chr, resolution = 50000, reference = "hg19")

boundary_spec = callTLD(graph_adj)

displayTLD(graph_adj, boundary_spec, 800, 1000, brecon = True)

plt.show()
#plt.savefig("/media/biology/datadisk/liuerhu/scTAD/biological significance/Tan_50k/commonTADs_show/"+cell+".tiff", dpi = 350)
plt.close()
