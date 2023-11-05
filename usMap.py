import plotly.express as ptl
import plotly.tools as ptool
import pandas as  pd
#import geopandas as gpd

# for testing perpuse i am using some domy data
def create_map(df=pd.read_csv("States.csv"), selected_data=None):
    
    Map = ptl.choropleth(
        data_frame=df,
        locations= 'state', 
        locationmode='USA-states',  
        scope='usa',
        color= selected_data)
    #convert the plotly map to HTML
    #html = Map.to_html()
    return Map
