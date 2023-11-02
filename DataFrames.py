import matplotlib.pyplot as plt
import pandas as pd
#create dataframe for choropleth map
df = pd.read_csv("data.csv")#created a data frame from our csv dataset
df['Total Deaths'].fillna(0, inplace=True)#filled out empty data slots
#there were extra data that wouldnt help us ...
df = df.drop(columns=['Data As Of', 'Start Week', 'MMWRyear', 'MMWRweek', 'Week Ending Date', 'Group', 'Indicator', 'Footnote'])
#print(df.head())
#we need to create 3 diferent data frame one for each respiratory disease
#covid
covid_df = df[['Age Group', 'COVID-19 Deaths','Total Deaths']]
covid_df['COVID-19 Deaths'].fillna(0, inplace=True)#filled out empty data slots
print("covid data:")
print(covid_df.head(10))
print(covid_df.tail(10))
#influenza
influenza_df = df[['Age Group', 'Influenza Deaths', 'Total Deaths']]
influenza_df['Influenza Deaths'].fillna(0, inplace=True) # filled out empty data slots
print("influenza data:")
print(influenza_df.head())
print(influenza_df.tail())
#Pneumonia
Pneumonia_df = df[['Age Group', 'Pneumonia Deaths', 'Total Deaths']]
Pneumonia_df['Pneumonia Deaths'].fillna(0, inplace=True) # filled out empty data slots
print("influenza data:")
print(Pneumonia_df.head())
print(Pneumonia_df.tail())

