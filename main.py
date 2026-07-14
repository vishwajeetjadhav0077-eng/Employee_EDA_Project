#import modules
import os
from src.load_data import load_data
from src.preprocessing import *
from src.analysys import *
from src.visualization import *
from src.report import generate_report

#Create the required folder
os.makedirs("images",exist_ok=True)
os.makedirs("reports",exist_ok=True)


#Load data
print("\n"+"="*60)
print("LOADING DATASET")
print("="*60)

df=load_data("data/employee_data.csv")


#Data preprocessing
print("\n"+"="*60)
print("DATA PREPROCESSING")
print("="*60)
dataset_info(df)

check_missing_values(df)

check_duplicates(df)

df=remove_duplicates(df)

save_clean_data(df)


#Business Analysis
print("\n"+"="*60)
print("BUSINESS ANALYSIS")
print("="*60)

average_salary(df)

highest_salary(df)

lowest_salary(df)

department_salary(df)

city_salary(df)

gender_salary(df)

education_salary(df)

performance_Count(df)

workmode_Count(df)

top_5_salary(df)

bottom_5_salary(df)


#Data Visualizations
print("\n"+"="*60)
print("DATA VISUALIZATIONS")
print("="*60)

age_distribution(df)

salary_distribution(df)

department_count(df)

gender_count(df)

education_count(df)

workmode_count(df)

performance_count(df)

salary_boxplot(df)

age_boxplot(df)

experience_vs_salary(df)

department_salary(df)

city_salary(df)


#Generate PDF report

print("\n "+ "="*60)
print("Generate pdf report")
print("="*60)

generate_report(df)


#Project Report

print("\n "+ "="*60)
print("Project completed successfully")
print("="*60)

