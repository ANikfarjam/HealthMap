import tkinter as tk
import ttkbootstrap as ttkb
from ttkwidgets import Table
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from table import create_table
import matplotlib.pyplot as plt
import seaborn as sns
def create_banner(df, frame, stateName):
    #polish the data frame
    cp_df = df.copy()
    cp_df = cp_df.drop(columns=['Jurisdiction', 'Month', 'Year'])
    cp_df.rename(columns={'Week Ending Date': 'Months'}, inplace=True)
    cp_df.reset_index(drop=True, inplace=True)
    # Create a Matplotlib figure and axis
    fig, ax = plt.subplots()
    lPlot = sns.lineplot(cp_df, x='Months', y=cp_df.columns[1], ax=ax)
    # Rotate x-axis labels vertically
    lPlot.set_xticklabels(lPlot.get_xticklabels(), rotation=90, fontsize=7)
    plt.title(stateName)
    # Create a Table from out dataframe
    table_frame  = ttkb.Frame(frame, height=30, width=20, bord=10)
    table_frame.grid(row=0,column=1,sticky="NSEW")
    create_table(cp_df, table_frame)
    """
    # we can use grid to create a table like data representation
    text_widget = tk.Text(frame, height=10, width=30)
    text_widget.insert(tk.END, df.to_string(index=False, justify='right'))
    text_widget.grid(column=1, row=0, sticky="NSEW")
    """
    # Create a canvas for the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(column=0, row=0, sticky="NSEW")

    # Update the layout to make it resizable
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(0, weight=1)

    return canvas_widget,#text_widget

 