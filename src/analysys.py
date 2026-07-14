def average_salary(df):
    print("\nAverage Salary")
    print(df["Salary"].mean())


def highest_salary(df):
    print("\n Highest Salary")
    print(df["Salary"].max())


def lowest_salary(df):
    print("\n Lowest Salary")
    print(df["Salary"].min())


def department_salary(df):
    print("\n Average Salary by department")
    print(df.groupby("Department")["Salary"].mean())


def city_salary(df):
    print("\n Average Salary by city")
    print(df.groupby("City")["Salary"].mean())


def gender_salary(df):
    print("\n Average Salary by gender")
    print(df.groupby("Gender")["Salary"].mean())


def education_salary(df):
    print("\n Average Salary by education")
    print(df.groupby("Education")["Salary"].mean())


def performance_Count(df):
    print("\n Performance Count")
    print(df["Performance"].value_counts())

    
def workmode_Count(df):
    print("\n Work mode Count")
    print(df["Work_Mode"].value_counts())


def top_5_salary(df):
    print("\nTop 5 Salary")
    print(df.nlargest(5,"Salary"))


def bottom_5_salary(df):
    print("\nBottom 5 Salary")
    print(df.nsmallest(5,"Salary"))