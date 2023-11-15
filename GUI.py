import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttkb
import matplotlib.pyplot as plt
import json
import pandas as pd
from operator import mul
from DataFrames import covid_df, influenza_df, Pneumonia_df
from analysisFuntions import anl_deathRate
#functions
def color_map(df, polygon_dic):
    #to color code the population, we first define minimum and maximum amount of death per capita
    #since we have 10 color catagories we devide the difference between max and min to 10 
    min_death = df[df.columns[3]].min() 
    max_death = df[df.columns[3]].max()
    step_int = (max_death - min_death)/10
    # Now we itterate through our polygon dictionary and extract the polygon ID from the dictionary
    for jurisdiction, polygons in polygon_dic.items():   
        for canvas_id in polygons:
            # Find the total death value from the data frame and then color the polygon related to that state besed on the death rate
            jurisdiction_total_death = df.loc[df['Jurisdiction'] == jurisdiction, df.columns[3]].values[0]
            if jurisdiction_total_death >= min_death and jurisdiction_total_death < min_death + step_int:
                canvas.itemconfig(canvas_id, fill="lime")
            elif jurisdiction_total_death >= (min_death + step_int) and jurisdiction_total_death < (min_death + (2 * step_int)):
                canvas.itemconfig(canvas_id, fill="green")
            elif jurisdiction_total_death >= (min_death + (2 * step_int)) and jurisdiction_total_death < (min_death + (3 * step_int)):
                canvas.itemconfig(canvas_id, fill="yellow")
            elif jurisdiction_total_death >= (min_death + (3 * step_int)) and jurisdiction_total_death < (min_death + (4 * step_int)):
                canvas.itemconfig(canvas_id, fill="gold")
            elif jurisdiction_total_death >= (min_death + (4 * step_int)) and jurisdiction_total_death < (min_death + (5 * step_int)):
                canvas.itemconfig(canvas_id, fill="orange")
            elif jurisdiction_total_death >= (min_death + (5 * step_int)) and jurisdiction_total_death < (min_death + (6 * step_int)):
                canvas.itemconfig(canvas_id, fill="darkorange")
            elif jurisdiction_total_death >= (min_death + (6 * step_int)) and jurisdiction_total_death < (min_death + (7 * step_int)):
                canvas.itemconfig(canvas_id, fill="sandybrown")
            elif jurisdiction_total_death >= (min_death + (7 * step_int)) and jurisdiction_total_death < (min_death + (8 * step_int)):
                canvas.itemconfig(canvas_id, fill="coral")
            elif jurisdiction_total_death >= (min_death + (8 * step_int)) and jurisdiction_total_death < (min_death + (9 * step_int)):
                canvas.itemconfig(canvas_id, fill="red")
            else:
                canvas.itemconfig(canvas_id, fill="darkred")


#creatint the main windows and frame
#def change_polygon_color():
#    canvas.itemconfig(polygon_id, fill="blue")
root = ttkb.Window(themename="darkly")
root.title("HealthMap")
#root.geometry("900x1000")
#frame is a place holder for tk widgits
left_frame = ttkb.Frame(root)
left_frame.grid(column=0,row=0, sticky=("N", "W", "E", "S"))
right_frame = ttkb.Frame(root)
right_frame.grid(column=1,row=0, sticky=("N", "W", "E", "S"))
#since i am creating map from my custom built polygons then i need a dictionatry to keep track of them
#{"type":"Feature","id":"AL","properties":{"name":"Alabama"},"geometry":{"type":"Polygon",
#the key values are states name
# the values are the polygon shapes
polygon_dic={}

#We have State Boundries json datas that i can create polygons in shape of the states
#When we do that for all the states we can get map of united states
def get_bounding_box(features):
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = float('-inf'), float('-inf')
    
    for feature in features:
        geometry = feature['geometry']
        if geometry['type'] == 'Polygon':
            for polygon in geometry['coordinates']:
                for coord in polygon:  # Assuming the outer ring is first
                    min_x, min_y = min(min_x, coord[0]), min(min_y, coord[1])
                    max_x, max_y = max(max_x, coord[0]), max(max_y, coord[1])
        elif geometry['type'] == 'MultiPolygon':
            for multipolygon in geometry['coordinates']:
                for polygon in multipolygon:
                    for coord in polygon:  # Assuming the outer ring is first
                        min_x, min_y = min(min_x, coord[0]), min(min_y, coord[1])
                        max_x, max_y = max(max_x, coord[0]), max(max_y, coord[1])

    return min_x, min_y, max_x, max_y

def transform(coord, scale_factor, offset_x, offset_y, canvas_width, canvas_height):
    # Scale and translate the coordinates
    x = (coord[0] - offset_x) * scale_factor
    y = (coord[1] - offset_y) * scale_factor
    # Flip the y coordinate to match the tkinter canvas
    y = canvas_height - y
    # print(str(coord) + ' -> ' + str((x, y)))
    return x, y

with open('state-geojson.json', 'r') as f:
    data = json.load(f)
canvas_width = 800
canvas_height = 400
canvas = ttkb.Canvas(right_frame, bg="white", width=canvas_width, height=canvas_height)
#canvas.grid(column=0,row=0, sticky="NSEW")
canvas.create_rectangle(0, 0, canvas_width, canvas_height, fill="white", outline="")

canvas.pack(fill=tk.BOTH, expand=True)
min_x, min_y, max_x, max_y = get_bounding_box(data['features'])
#print(min_x, min_y, max_x, max_y)
range_x = max_x - min_x
range_y = max_y - min_y
scale_factor = min(canvas_width / range_x, canvas_height / range_y)
offset_x = min_x
offset_y = min_y

for feature in data['features']:
    geometry = feature['geometry']
    if geometry['type'] == 'Polygon':
        for polygon in geometry['coordinates']:
            # Transform coordinates
            # print(polygon)
            scaled_polygon = [transform(coord, scale_factor, offset_x, offset_y, canvas_width, canvas_height) for coord in polygon]
            # Draw the polygon on the canvas
            st_shape = canvas.create_polygon(*scaled_polygon, outline='black', fill='gainsboro')
            canvas.itemconfig(st_shape, fill='gainsboro')
            #{"type":"Feature","id":"AL","properties":{"name":"Alabama"},"geometry":{"type":"Polygon",
            polygon_dic[str(feature.get('properties').get('name'))] = [st_shape]
            
            
    elif geometry['type'] == 'MultiPolygon':
        shapes = []
        for multipolygon in geometry['coordinates']:
            for polygon in multipolygon:
                # Transform coordinates
                scaled_polygon = [transform(coord, scale_factor, offset_x, offset_y, canvas_width, canvas_height) for coord in polygon]
                # Draw the polygon on the canvas
                st_shape = canvas.create_polygon(*scaled_polygon, outline='black', fill='gainsboro')
                canvas.itemconfig(st_shape, fill='gainsboro')
                shapes.append(st_shape)    
        polygon_dic[str(feature.get('properties').get('name'))] = shapes
#filtering pannel
selected_option = tk.StringVar()
label1 = ttkb.Label(left_frame, text="Wekcome to HealthMap!").grid(column=0,row=0, sticky="NSEW")
label2 = ttkb.Label(left_frame, text="Select Data to show:").grid(column=0,row=1, sticky="NSEW")
covid_filter = ttkb.Radiobutton(left_frame, text='Covid-19', variable=selected_option, value='Covid-19', command=lambda: color_map(anl_deathRate(covid_df), polygon_dic))
covid_filter.grid(column=0,row=2, sticky="NSEW")
#covid_filter.pack()

influenza_filter = ttkb.Radiobutton(left_frame, text='Influenza', variable=selected_option, value='Influenza', command=lambda: color_map(anl_deathRate(influenza_df), polygon_dic))
influenza_filter.grid(column=0,row=3, sticky="NSEW")
#influenza_filter.pack()
pneumonia_filter = ttkb.Radiobutton(left_frame, text='Pneumonia', variable=selected_option, value='Pneumonia', command=lambda: color_map(anl_deathRate(Pneumonia_df), polygon_dic))
pneumonia_filter.grid(column=0,row=4, sticky="NSEW")
#pneumonia_filter.pack()

print(polygon_dic)
root.mainloop()

