import os
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import(
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

def generate_report(df):

    os.makedirs("reports",exist_ok=True)

    pdf= SimpleDocTemplate(
        "reports/Final_Report.pdf"
    )
    styles = getSampleStyleSheet()
    elements = []

    #Title 
    elements.append(
        Paragraph(
            "Employee Exploratory Data Analysis Report",
            styles["Title"]
        )
    )
    elements.append(Spacer(1,20))

    #Dataset Summary
    elements.append(
        Paragraph(
            "<b>Dataset Summary</b>",
            styles["Heading2"]
        )
    )
    elements.append(
        Paragraph(
            f"Total Employees :{len(df)}",
            styles["BodyText"]
        )
    )
    elements.append(
        Paragraph(
            f"Total Columns :{len(df.columns)}",
            styles["BodyText"]
        )
    )
    elements.append(
        Paragraph(
            f"Missing Values:{df.isnull().sum()}",
            styles["BodyText"]
        )
    )
    elements.append(
        Paragraph(
            f"Duplicate Rows:{df.duplicated().sum()}",
            styles["BodyText"]
        )
    )
    elements.append(Spacer(1,20))
#Salary Analysis
    elements.append(
        Paragraph(
            f"<b>Salary Analysys</b>",
            styles["Heading2"]
        )
    )
    elements.append(
        Paragraph(
            f"Average Salary: RS{df['Salary'].mean():,.2f}",
            styles["BodyText"]
        )
    )
    elements.append(
        Paragraph(
            f"Highest Salary: RS{df['Salary'].max():,.2f}",
            styles["BodyText"]
        )
    )
    elements.append(
        Paragraph(
            f"Lowest Salary: RS{df['Salary'].min():,.2f}",
            styles["BodyText"]
        )
    )
    elements.append(Spacer(1,20))


    #Business Insights
    elements.append(
        Paragraph(
            "<b>Business Insights</b>",
            styles["Heading2"]
        )
    )
    elements.append(
        Paragraph(
            f"Highest Paying Department:"
            f"{df.groupby("Department")['Salary'].mean().idxmax()}",
            styles["BodyText"]
        )
    )
    elements.append(
        Paragraph(
            f"Highest Paying City:"
            f"{df.groupby("City")['Salary'].mean().idxmax()}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Most Common Work Mode"
            f"{df['Work_Mode'].mode()[0]}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Highest Performance Rating"
            f"{df['Performance'].max()}",
            styles["BodyText"]
        )
    )
    elements.append(
        Paragraph(
            f"Most Common Education"
            f"{df['Education'].mode()[0]}",
            styles["BodyText"]
        )
    )
    elements.append(Spacer(1,20))


    #Recommendations
    elements.append(
        Paragraph(
            "<b>Recomendations</b>",
            styles["Heading2"]
        )
    )
    elements.append(
        Paragraph(
            "1.Review Salary Structure acorss department.",
            styles["BodyText"]

        )
    )
    elements.append(
        Paragraph(
            "2.Encourage employee skill development",
            styles["BodyText"]
        )
    )
    elements.append(
        Paragraph(
            "3.Improve Performance evaluation process",
            styles["BodyText"]
        )
    )
    elements.append(
        Paragraph(
            "4.Monitor salary outliers regularly",
            styles["BodyText"]
        )
    )
    elements.append(
        Paragraph(
            "5.Continue data-driven HR decision making",
            styles["BodyText"]
        )
    )

    #Build pdf
    pdf.build(elements)
    print("="*50)
    print("PDf generated successfully")
    print("="*50)