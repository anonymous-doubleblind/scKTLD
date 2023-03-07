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

path_input = "./data/exp-sc/gm12878_cell7_chr3_sparse.txt"
graph_edge = np.loadtxt(path_input)
chr='chr3'
resolution = 50000
graph_adj = edge2adj(graph_edge, chr = chr, resolution = resolution, reference = "hg19")

boundary_spec = callTLD(graph_adj)

displayTLD(graph_adj, boundary_spec, 800, 1000, brecon = True)

plt.show()
#plt.savefig("path to save/filename.tiff", dpi = 350)
plt.close()
