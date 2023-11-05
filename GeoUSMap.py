import geopandas
import folium

def creat_geoMap():
    us = geopandas.read_file("States.csv")
    us.explore(
    column='population',  # make choropleth based on "BoroName" column
    tooltip="population",  # show "BoroName" value in tooltip (on hover)
    popup=True,  # show all values in popup (on click)
    tiles="CartoDB positron",  # use "CartoDB positron" tiles
    cmap="Set1",  # use "Set1" matplotlib colormap
    style_kwds=dict(color="black"),  # use black outline
)
