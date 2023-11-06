from DataFrames import covid_df, influenza_df, Pneumonia_df
import pandas as pd
st_df = pd.read_csv("States.csv")
st_df= st_df.drop(columns='population')
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
    result_df = pd.merge(st_df, all_age_df, on= 'Jurisdiction')
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
    result_df = pd.merge(st_df, mod_df, on='Jurisdiction')
    return result_df
def anl_weekly(df):
    """
    input: a dataframe 
    output: manipulated datdrame or siries based on weeklydeath rate
    """
    return None
def anl_monthly():
    """
    input: a dataframe 
    output: manipulated datdrame or siries based on monthly death rate
    """
    return None
def anl_yearly():
    """
    input: a dataframe 
    output: manipulated datdrame or siries based on yearly death rate
    """
    return None