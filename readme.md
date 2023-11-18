droping these colums

Date As Of, Start Week, MMWRyear MMWRweek, Week Ending Date, Group, Indicator, Foornote
we have DataFrames.py that we cleaned up data and created 3 other data frames based on each individual deseases

analysisFunctions.py implements functions that manipulate data frames for ploting and for map

GUI.py creates our tkinter gui window

    created states shape polygon

    created radio buttons that can change the color of map based on the data of selected desease

![Alt Text](./sample1.png)
![Alt Text](./sample2.png)
![Alt Text](./sample3.png)
![Alt Text](./sample4.png)
![Alt Text](./sample5.png)
map polygon dictionary

{'Alabama': [2], 'Arizona': [3], 'Arkansas': [4], 'California': [5], 'Colorado': [6], 'Connecticut': [7], 'Delaware': [8], 'Florida': [9], 'Georgia': [10], 'Idaho': [11], 'Illinois': [12], 'Indiana': [13], 'Iowa': [14], 'Kansas': [15], 'Kentucky': [16], 'Louisiana': [17], 'Maine': [18], 'Maryland': [[20]], 'Massachusetts': [21], 'Michigan': [[25]], 'Minnesota': [26], 'Mississippi': [27], 'Missouri': [28], 'Montana': [29], 'Nebraska': [30], 'Nevada': [31], 'New Hampshire': [32], 'New Jersey': [33], 'New Mexico': [34], 'New York': [35], 'North Carolina': [36], 'North Dakota': [37], 'Ohio': [38], 'Oklahoma': [39], 'Oregon': [40], 'Pennsylvania': [41], 'Rhode Island': [[43]], 'South Carolina': [44], 'South Dakota': [45], 'Tennessee': [46], 'Texas': [47], 'Utah': [48], 'Vermont': [49], 'Virginia': [[52]], 'Washington': [[55]], 'West Virginia': [56], 'Wisconsin': [57], 'Wyoming': [58]}
    the numbers are refrence and not name necessurily 


at the end of the day im going to use corntab to schedule updating our data.csv-->desease file because the data gets updated evry 2 weeks command
~ corntab -e <frequency> curl -o data.csv https://path/to/file.csv


