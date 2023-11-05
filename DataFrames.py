import matplotlib.pyplot as plt
import pandas as pd
import warnings
#create dataframe for choropleth map
df = pd.read_csv("data.csv")#created a data frame from our csv dataset
df['Total Deaths'].fillna(0, inplace=True)#filled out empty data slots
#there were extra data that wouldnt help us ...
df = df.drop(columns=['Data As Of', 'Start Week', 'End Week','MMWRyear', 'MMWRweek', 'Group', 'Indicator', 'Footnote'])
#print(df.head())
#we need to create 3 diferent data frame one for each respiratory disease
#covid
covid_df = df[['Week Ending Date','Jurisdiction', 'Age Group', 'COVID-19 Deaths','Total Deaths']]
with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    covid_df['COVID-19 Deaths'].fillna(0, inplace=True)#filled out empty data slots
#print("covid data:")
#print(covid_df.head(10))
#print(covid_df.tail(10))
#influenza
influenza_df = df[['Week Ending Date','Jurisdiction', 'Age Group', 'Influenza Deaths', 'Total Deaths']]
with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    influenza_df['Influenza Deaths'].fillna(0, inplace=True) # filled out empty data slots
#print("influenza data:")
#print(influenza_df.head())
#print(influenza_df.tail())
#Pneumonia
Pneumonia_df = df[['Week Ending Date','Jurisdiction', 'Age Group', 'Pneumonia Deaths', 'Total Deaths']]
with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    Pneumonia_df['Pneumonia Deaths'].fillna(0, inplace=True) # filled out empty data slots
#print("influenza data:")
#print(Pneumonia_df.head())
#print(Pneumonia_df.tail())


