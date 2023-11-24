import tkinter as tk
import ttkbootstrap as ttkb
from ttkwidgets import Table
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from table import create_table
import matplotlib.pyplot as plt
import seaborn as sns
import squarify

def create_age_banner(df, frame):
    
    cp_df = df.copy()
     # Create a Table from out dataframe
    table_frame  = ttkb.Frame(frame, height=5, width=10)
    table_frame.grid(row=2,column=0,sticky="NSEW")
    create_table(cp_df, table_frame)
    #charts
    #first need to polish dat
    #cp_df.iloc[:, [2, 4]] = cp_df.iloc[:, [2, 4]].div(cp_df.iloc[:, 0], axis=0)
    cp_df = cp_df.drop(columns='POPESTIMATE2022')
    cp_df = cp_df.drop(index=0)
    fig_df = cp_df.set_index('Jurisdiction').T
    #print(fig_df)
    fig, ax = plt.subplots(figsize=(50,5))
    #ax.set_xticks(range(len(cp_df.columns)))
    #plt.figure(figsize=(10, 6))
    hmap = sns.heatmap(fig_df, linewidths=0.5, ax=ax, xticklabels=True, cmap='Blues')
    plt.title('Population Age Distribution')
    plt.tick_params(axis='x', labelsize=8)
    # Create a canvas for the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(column=0, row=0, sticky="NSEW")


    # Update the layout to make it resizable
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(0, weight=1)

    return table_frame, hmap