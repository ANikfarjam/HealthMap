import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttkb
from usMap import create_map
import matplotlib.pyplot as plt
import json

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
            st_shape
            #{"type":"Feature","id":"AL","properties":{"name":"Alabama"},"geometry":{"type":"Polygon",
            polygon_dic[str(feature.get('properties').get('name'))] = [st_shape]
            
            
    elif geometry['type'] == 'MultiPolygon':
        for multipolygon in geometry['coordinates']:
            shapes = []
            for polygon in multipolygon:
                # Transform coordinates
                scaled_polygon = [transform(coord, scale_factor, offset_x, offset_y, canvas_width, canvas_height) for coord in polygon]
                # Draw the polygon on the canvas
                st_shape = canvas.create_polygon(*scaled_polygon, outline='black', fill='gainsboro')
                st_shape 
                shapes.append(st_shape)    
            polygon_dic[str(feature.get('properties').get('name'))] = [shapes] 
#filtering pannel
selected_option = tk.StringVar()
label1 = ttkb.Label(left_frame, text="Wekcome to HealthMap!").grid(column=0,row=0, sticky="NSEW")
label2 = ttkb.Label(left_frame, text="Select Data to show:").grid(column=0,row=1, sticky="NSEW")
covid_filter = ttkb.Radiobutton(left_frame, text='Covid-19', variable=selected_option, value='Covid-19')
covid_filter.grid(column=0,row=2, sticky="NSEW")
#covid_filter.pack()
influenza_filter = ttkb.Radiobutton(left_frame, text='Influenza', variable=selected_option, value='Influenza')
influenza_filter.grid(column=0,row=3, sticky="NSEW")
#influenza_filter.pack()
pneumonia_filter = ttkb.Radiobutton(left_frame, text='Pneumonia', variable=selected_option, value='Pneumonia')
pneumonia_filter.grid(column=0,row=4, sticky="NSEW")
#pneumonia_filter.pack()


root.mainloop()

