import tkinter as tk
import ttkbootstrap as ttkb
from ttkwidgets import Table
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from table import create_table
import matplotlib.pyplot as plt
import seaborn as sns
def create_age_banner(df, frame, stateName):
    cp_df = df.copy()
     # Create a Table from out dataframe
    table_frame  = ttkb.Frame(frame, height=10, width=20, bord=10)
    table_frame.grid(row=0,column=0,sticky="NSEW")
    create_table(cp_df, table_frame)
    #charts
    selected_rows = df.loc[df['Jurisdiction'] == stateName]
    print(selected_rows)

    return table_frame
