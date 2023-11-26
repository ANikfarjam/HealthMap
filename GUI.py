#Author: ANikfarjam
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttkb
import matplotlib.pyplot as plt
import json
import pandas as pd
from operator import mul
from DataFrames import covid_df, influenza_df, Pneumonia_df
from analysisFuntions import anl_deathRate, anl_by_age, anl_monthly, anl_yearly, year_filter
import banner
import AgeBanner
#functions
colors_dic={}

    
def display_map_data(df):
    for widget in map_data_panel.winfo_children():
        widget.destroy()
    global colors_dic
    sorted_dict = dict(sorted(colors_dic.items(), key=lambda item: item[1]))
    #print(sorted_dict)
    cp_df = df.copy()
    #display Virus name
    column_name = cp_df.columns[1].split()[0]
    Head = ttkb.Label(map_data_panel, text= column_name, style='info.Inverse.TLabel')
    Head.grid(column=0, row=0, sticky="NSEW")
    #display Total death
    total_death = df.get(df.columns[1]).sum()
    ds_Label = ttkb.Label(map_data_panel, style='info.Inverse.TLabel', text= str(column_name)+ ' deaths: ' +str(total_death))
    ds_Label.grid(column=0, row=1, sticky="NSEW")
    #line_tacker = 0
    if var_2020.get() == 1:
        yr_label = ttkb.Label(map_data_panel, text="Now showing data for the year 2020.")
        yr_label.grid(column=0, row=2, sticky="NSEW")
    elif var_2021.get() == 1:
        yr_label = ttkb.Label(map_data_panel, text="Now showing data for the year 2021.")
        yr_label.grid(column=0, row=2, sticky="NSEW")
    elif var_2022.get() == 1:
        yr_label = ttkb.Label(map_data_panel, text="Now showing data for the year 2022.")
        yr_label.grid(column=0, row=2, sticky="NSEW")
    elif var_2023.get() == 1:
        yr_label = ttkb.Label(map_data_panel, text="Now showing data for the year 2023.")
        yr_label.grid(column=0, row=2, sticky="NSEW")
    else:
        yr_label = ttkb.Label(map_data_panel, text="This data is from 2020-2023")
        yr_label.grid(column=0, row=2, sticky="NSEW")
    for row, (color, value) in enumerate(sorted_dict.items()):
        # Create a colored label
        label = ttkb.Label(map_data_panel, text= "{:.3f} to {:.3f}".format(value[0] * 100, value[1] * 100), background=color)
        label.grid(column=0, row=row + 3, sticky="ew", columnspan=2)
        #line_tacker = row + 2
    
def get_key_by_value(dictionary, target_value):
    for key, value in dictionary.items():
        if target_value in value or [target_value] in value:
            return key
    return None
def on_polygon_click(event):
     
     # Clear the existing content in Data_frame
    for widget in Data_frame.winfo_children():
        widget.destroy()
    # clicked_item is a variable that stores the item ID of polygon
    clicked_item = event.widget.find_closest(event.x, event.y)[0]
    print(clicked_item)
    stateName = get_key_by_value(polygon_dic, clicked_item)
    #showing data on the bottom of map
    if selected_option.get() == 'Covid-19':
        df = anl_monthly(covid_df)
    elif selected_option.get() == 'Influenza':    
        df = anl_monthly(influenza_df)
    elif selected_option.get() == 'Pneumonia':    
        df = anl_monthly(Pneumonia_df)
    df = df[df['Jurisdiction']==stateName]
    df = df.sort_values(['Year','Month'])
    #print(df)
    banner.create_banner(df, Data_frame, stateName)
    
    


def color_map(df, polygon_dic):
    #check if the color dic is empty
    #clear the dictionary if its not empty
    global colors_dic
    if len(colors_dic) > 0:
        colors_dic={}
    #to color code the population, we first define minimum and maximum amount of death per capita
    #since we have 10 color catagories we devide the difference between max and min to 10 
    #print(df)
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
                colors_dic['lime'] = [0,min_death] 
            elif jurisdiction_total_death >= (min_death + step_int) and jurisdiction_total_death < (min_death + (2 * step_int)):
                canvas.itemconfig(canvas_id, fill="green")
                colors_dic['green'] = [min_death, min_death + step_int]
            elif jurisdiction_total_death >= (min_death + (2 * step_int)) and jurisdiction_total_death < (min_death + (3 * step_int)):
                canvas.itemconfig(canvas_id, fill="yellow")
                colors_dic['yellow'] = [min_death + step_int, min_death + (2 * step_int)]
            elif jurisdiction_total_death >= (min_death + (3 * step_int)) and jurisdiction_total_death < (min_death + (4 * step_int)):
                canvas.itemconfig(canvas_id, fill="gold")
                colors_dic['gold'] = [min_death + (2 * step_int), min_death + (3 * step_int)]
            elif jurisdiction_total_death >= (min_death + (4 * step_int)) and jurisdiction_total_death < (min_death + (5 * step_int)):
                canvas.itemconfig(canvas_id, fill="orange")
                colors_dic['orange'] = [min_death + (3 * step_int), min_death + (4 * step_int)]
            elif jurisdiction_total_death >= (min_death + (5 * step_int)) and jurisdiction_total_death < (min_death + (6 * step_int)):
                canvas.itemconfig(canvas_id, fill="darkorange")
                colors_dic['darkorange'] = [min_death + (4 * step_int), min_death + (5 * step_int)]
            elif jurisdiction_total_death >= (min_death + (6 * step_int)) and jurisdiction_total_death < (min_death + (7 * step_int)):
                canvas.itemconfig(canvas_id, fill="sandybrown")
                colors_dic['sandybrown'] = [min_death + (5 * step_int), min_death + (6 * step_int)]
            elif jurisdiction_total_death >= (min_death + (7 * step_int)) and jurisdiction_total_death < (min_death + (8 * step_int)):
                canvas.itemconfig(canvas_id, fill="coral")
                colors_dic['coral'] = [min_death + (6 * step_int), min_death + (7 * step_int)]
            elif jurisdiction_total_death >= (min_death + (8 * step_int)) and jurisdiction_total_death < (min_death + (9 * step_int)):
                canvas.itemconfig(canvas_id, fill="red")
                colors_dic['red'] = [min_death + (7 * step_int), min_death + (8 * step_int)]
            else:
                canvas.itemconfig(canvas_id, fill="darkred")
                colors_dic['darkred'] = [min_death + (8 * step_int), min_death + (9 * step_int)]
    display_map_data(df)


#creatint the main windows and frame
#def change_polygon_color():
#    canvas.itemconfig(polygon_id, fill="blue")
root = ttkb.Window(themename="flatly")
root.title("HealthMap")
#root.geometry("900x1000")
#frame is a place holder for tk widgits
left_frame = ttkb.Frame(root)
left_frame.grid(column=0,row=0, sticky=("N", "W", "E", "S"))
right_frame = ttkb.Frame(root)
right_frame.grid(column=1,row=0, sticky=("N", "W", "E", "S"))
#separator2 = ttkb.Separator(root, orient='horizontal',style='info.Horizontal.TSeparator')
#separator2.grid(column=1,row=1, sticky=("N", "W", "E", "S"))
#separator.pack()
#this frame is analyzing data based on age
#it shows monthly and age analysis
anl_frame = ttkb.Frame(root)
anl_frame.grid(column=1,row=1, sticky=("N", "W", "E", "S"))
#analysis by age
#age_frame = ttkb.LabelFrame(anl_frame, text='Death Rate Based on Age', style='primary.TLabelframe')
#age_frame.grid(column=0,row=0, sticky=("N", "W", "E", "S"))
#monthy analysis
Data_frame = ttkb.LabelFrame(anl_frame, text='Monthly Data Analysis', style='primary.TLabelframe')
Data_frame.grid(column=1,row=0, sticky=("N", "W", "E", "S"))
#this frame can sort data to a specific year
Date_frame = ttkb.Frame(root)
Date_frame.grid(column=0,row=1, sticky=("N", "W", "E", "S"))
#crating pannel to display map data
map_data_panel = ttkb.Frame(root, style='info.TFrame')
map_data_panel.grid(column=3, row=0, sticky=("N", "W", "E", "S"))
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
            canvas.tag_bind(st_shape, '<Button-1>', on_polygon_click)
            
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
                # Bind the click event to the polygon
                canvas.tag_bind(st_shape, '<Button-1>', on_polygon_click)
        polygon_dic[str(feature.get('properties').get('name'))] = shapes
#filtering pannel
selected_option = tk.StringVar()
label1 = ttkb.Label(left_frame, text="Wekcome to HealthMap!",style="Inverse.TLable").grid(column=0,row=0, sticky="NSEW")
label2 = ttkb.Label(left_frame, text="Select Data to show:",style='info.Inverse.TLable').grid(column=0,row=1, sticky="NSEW")
covid_filter = ttkb.Radiobutton(left_frame, text='Covid-19', variable=selected_option, value='Covid-19', style='flatly', command=lambda: color_map(anl_deathRate(covid_df), polygon_dic))
covid_filter.grid(column=0,row=2, sticky="NSEW")
#covid_filter.pack()

influenza_filter = ttkb.Radiobutton(left_frame, text='Influenza', variable=selected_option, value='Influenza', style='flatly', command=lambda: color_map(anl_deathRate(influenza_df), polygon_dic))
influenza_filter.grid(column=0,row=3, sticky="NSEW")
#influenza_filter.pack()
pneumonia_filter = ttkb.Radiobutton(left_frame, text='Pneumonia', variable=selected_option, value='Pneumonia', style='flatly', command=lambda: color_map(anl_deathRate(Pneumonia_df), polygon_dic))
pneumonia_filter.grid(column=0,row=4, sticky="NSEW")


#Date Filteration
label3 = ttkb.Label(Date_frame, text="Representation by Date:",style='Inverse.TLable').grid(column=0,row=0, sticky="NSEW")
label4 = ttkb.Label(Date_frame, text="Select Date to show:",style='info.Inverse.TLable').grid(column=0,row=1, sticky="NSEW")
# Define df_to_pass with a default value or as an empty DataFrame
def check_func(year):
    #print(selected_option.get())
    df_to_pass = pd.DataFrame()
    if selected_option.get() == 'Covid-19':
        df_to_pass = anl_yearly(covid_df)
    elif selected_option.get() == 'Influenza':    
        df_to_pass = anl_yearly(influenza_df)
    elif selected_option.get() == 'Pneumonia':    
        df_to_pass = anl_yearly(Pneumonia_df)
    #print(df_to_pass)
    color_map(year_filter(df_to_pass,year), polygon_dic)
#this function check witch checkbutton is clicked
#The control variable that tracks the current state of the checkbutton. 
#Normally this variable is an IntVar, and 0 means cleared and 1 means set
var_2020 = tk.IntVar()
var_2021 = tk.IntVar()
var_2022 = tk.IntVar()
var_2023 = tk.IntVar()

year_2020 = ttkb.Checkbutton(Date_frame, text='2020', style='flatly', variable= var_2020, command=lambda: check_func('2020'))
year_2020.grid(column=0,row=2, sticky="NSEW")
year_2021 = ttkb.Checkbutton(Date_frame, text='2021', style='flatly', variable= var_2021, command=lambda: check_func('2021'))
year_2021.grid(column=0,row=3, sticky="NSEW")
year_2022 = ttkb.Checkbutton(Date_frame, text='2022', style='flatly', variable= var_2022, command=lambda: check_func('2022'))
year_2022.grid(column=0,row=4, sticky="NSEW")
year_2023 = ttkb.Checkbutton(Date_frame, text='2023', style='flatly', variable= var_2023, command=lambda: check_func('2023'))
year_2023.grid(column=0,row=5, sticky="NSEW")
# to do analysis based on age 
# I create a buton that opens up a new windows and show related data
def open_frame(disease):
     # Create a new top-level window (frame)
    new_window = ttkb.Toplevel(root)
    new_window.title(str(disease) + " analysis by age")
    if disease == 'Covid-19':
        AgeBanner.create_age_banner(anl_by_age(covid_df), new_window)
    elif disease == 'Influenza':
        AgeBanner.create_age_banner(anl_by_age(influenza_df), new_window)
    elif disease == 'Pneumonia':
        AgeBanner.create_age_banner(anl_by_age(Pneumonia_df), new_window)
    
        
open_button = ttkb.Button(Date_frame, text="Age Analysis", command=lambda: open_frame(selected_option.get()), style='primary.Outline.TButton')
open_button.grid(column=0,row=6, sticky="NSEW")


root.mainloop()