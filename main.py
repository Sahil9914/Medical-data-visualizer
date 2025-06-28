# main.py

import matplotlib.pyplot as plt
from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Run both visualizations
cat_plot_fig = draw_cat_plot()
cat_plot_fig.savefig('catplot.png')

heat_map_fig = draw_heat_map()
heat_map_fig.savefig('heatmap.png')
