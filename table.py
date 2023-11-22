import pandas as pd
from DataFrames import covid_df
import ttkbootstrap as ttkb
from tkinter import*
def create_table(df, frame):
    # Convert the DataFrame to a dictionary
    data_dic = df.to_dict(orient='list')

    # Create a Treeview widget with column headings
    data_tree = ttkb.Treeview(frame, columns=list(data_dic.keys()), show='headings', style='primary.Treeview')

    # Set the column headings
    for key in data_dic.keys():
        data_tree.heading(key, text=key)

    # Insert data into the table
    for i in range(len(data_dic[key])):
        row_data = [data_dic[col][i] for col in data_dic.keys()]
        data_tree.insert("", "end", values=row_data)

    # Attach the Treeview widget to the frame
    data_tree.grid(row=0, column=0, sticky="NSEW")

    # Update the layout to make it resizable
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)

    return data_tree

