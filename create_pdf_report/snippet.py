import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import numpy as np
# Create a sample DataFrame




# Render the styled DataFrame to an image
def render_mpl_table(data, col_width=2.5, row_height=0.5, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in mpl_table._cells.items():
        cell.set_edgecolor(edge_color)
        if k[0] == 0:
            cell.set_text_props(weight='bold', color='w', ha='center', va='center')
            cell.set_facecolor(header_color)
        else:
            cell.set_text_props( ha='center', va='center')
            cell.set_facecolor(row_colors[k[0] % len(row_colors)])
    return ax

#so calculate the df in the previous module and here just create the table 




