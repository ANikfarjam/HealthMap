import plotly.express as ptl
import plotly.tools as ptool
import pandas as  pd
import matplotlib.pyplot as plt
# for testing perpuse i am using some domy data
stateData =  pd.read_csv("States.csv")
Map = ptl.choropleth(
    data_frame=stateData,
    locations= 'state', 
    locationmode='USA-states',  
    scope='usa',
    color='population',)
Map.show()