import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns
def create_banner(df, frame):
    # Create a Matplotlib figure and axis
    fig, ax = plt.subplots()
    lPlot = sns.lineplot(df, x='Week Ending Date', y=df.columns[2],ax=ax)
    # Rotate x-axis labels vertically
    lPlot.set_xticklabels(lPlot.get_xticklabels(), rotation=90, fontsize=7)
    #plt.show()
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()
    return canvas_widget

 