from DataFrames import covid_df, influenza_df, Pneumonia_df
import pandas as pd
import re
st_df = pd.read_csv("State Population.csv")
st_df = st_df[['NAME', 'POPESTIMATE2022']]
#st_df= st_df.drop(columns='population')
def anl_by_age(df):
    """
    input: a dataframe 
    output: manipulated datdrame or siries based on age
    """
    # this data is devided in these age catagories
    # ["All Ages", "AgeGroup1: 0-17 years", "18-64 years", "65 years and over"]
    # i need to create a data frame that contains Name of State, Age Group, Death Rate
    all_age_df = df[df['Age Group']=="All Ages"]
    all_age_df = all_age_df.groupby('Jurisdiction').agg({df.columns[3]:'sum'}).reset_index()
    result_df = pd.merge(st_df, all_age_df, left_on='NAME', right_on='Jurisdiction')
    result_df = result_df.drop(columns='NAME')
    #result_df = pd.merge(st_df, all_age_df, on= 'Jurisdiction')
    result_df = result_df.rename(columns={df.columns[3]:'all ages'})
    #group age 0-17
    Age_group_1 = df[df['Age Group']=="0-17 years"]
    Age_group_1 = Age_group_1.groupby('Jurisdiction').agg({df.columns[3]:'sum'}).reset_index()
    result_df = pd.merge(result_df, Age_group_1, on= 'Jurisdiction')
    result_df = result_df.rename(columns={df.columns[3]:'0-17 years'})

    #group 18-64 years
    Age_group_2 = df[df['Age Group']=="18-64 years"]
    Age_group_2 = Age_group_2.groupby('Jurisdiction').agg({df.columns[3]:'sum'}).reset_index()
    result_df = pd.merge(result_df, Age_group_2, on= 'Jurisdiction')
    result_df = result_df.rename(columns={df.columns[3]:'18-64 years'})
    
    #gourp 65 years and over
    Age_group_3 = df[df['Age Group']=="65 years and over"]
    Age_group_3 = Age_group_3.groupby('Jurisdiction').agg({df.columns[3]:'sum'}).reset_index()
    result_df = pd.merge(result_df, Age_group_3, on= 'Jurisdiction')
    result_df = result_df.rename(columns={df.columns[3]:'65 years and over'})
    

    return result_df#[51 rows x 8 columns]
def anl_deathRate(df):
    mod_df = df.groupby('Jurisdiction').agg({df.columns[3]:'sum'}).reset_index()
    result_df = pd.merge(mod_df, st_df, left_on='Jurisdiction', right_on='NAME')
    result_df = result_df.drop(columns='NAME')
    result_df['Death Per Capita'] = result_df.iloc[:,1]/result_df.iloc[:,2]
    return result_df
def anl_weekly(df):
    """
    input: a dataframe 
    output: manipulated datdrame or siries based on weeklydeath rate
    I dont think analyzing weekly doesnt make sence
    """
    return None
def anl_monthly(df):
    """
    input: a dataframe 
    output: manipulated datdrame or siries based on monthly death rate
    """
    #data gets updated every 2 weeks
    #data frames have these columns
    #'Week Ending Date','Jurisdiction', 'Age Group', 'Pneumonia Deaths', 'Total Deaths'
    #droping the day from date format
    cp_df = df.copy()
    cp_df.loc[:,'Week Ending Date'] = cp_df['Week Ending Date'].apply(lambda x: '/'.join(x.split('/')[::2]))
    #df['Week Ending Date'] = df['Week Ending Date'].apply(lambda x: '/'.join(x.split('/')[::2]))
    mod_df = cp_df.groupby(['Week Ending Date', 'Jurisdiction']).agg({cp_df.columns[3]:'sum', cp_df.columns[4]:'sum'}).reset_index()
    #print(mod_df)
    mod_df[['Month', 'Year']] = mod_df['Week Ending Date'].str.split('/', expand=True)
    return mod_df
    
def anl_yearly(df):
    """
    input: a dataframe 
    output: manipulated datdrame or siries based on yearly death rate
    """
    cp_df = df.copy()
    cp_df.loc[:,'Week Ending Date'] = cp_df['Week Ending Date'].apply(lambda x: x.split('/')[2])
    mod_df = cp_df.groupby(['Week Ending Date', 'Jurisdiction']).agg({cp_df.columns[3]:'sum', cp_df.columns[4]:'sum'}).reset_index()
    return mod_df

def year_filter(df, year):
    #used to color the map based on the yearly filter
    #we must pass in a data frame that is in same format as what anl_yearly reaturns
    cp_df = df.copy()
    #print(cp_df)
    mod_df = cp_df[cp_df['Week Ending Date']==year]
    #now convert the format to what out color map function accept
    mod_df = mod_df.drop(columns='Week Ending Date')
    mod_df['Death Per Capita'] = mod_df.iloc[:,1]/mod_df.iloc[:,2]
    return mod_df
    