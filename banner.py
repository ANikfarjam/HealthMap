import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns
def create_banner(df, frame, stateName):
    #polish the data frame
    df = df.drop(columns=['Jurisdiction', 'Month', 'Year'])
    df.rename(columns={'Week Ending Date': 'Month'}, inplace=True)
    df.reset_index(drop=True, inplace=True)
    # Create a Matplotlib figure and axis
    fig, ax = plt.subplots()
    lPlot = sns.lineplot(df, x='Month', y=df.columns[1], ax=ax)
    # Rotate x-axis labels vertically
    lPlot.set_xticklabels(lPlot.get_xticklabels(), rotation=90, fontsize=7)
    plt.title(stateName)
    # Create a Text widget to display DataFrame
    text_widget = tk.Text(frame, height=10, width=40)
    text_widget.insert(tk.END, df.to_string(index=False))
    text_widget.grid(column=1, row=0, sticky="NSEW")

    # Create a canvas for the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(column=0, row=0, sticky="NSEW")

    # Update the layout to make it resizable
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(0, weight=1)

    return canvas_widget, text_widget

 