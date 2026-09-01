import pandas as pd


def generate_insights(df):

    insights = []

    # 1. Dataset overview
    rows = len(df)
    columns = len(df.columns)

    insights.append({
        "type": "dataset",
        "title": "Dataset Overview",
        "description": (
            f"The dataset contains {rows} rows "
            f"and {columns} columns."
        )
    })

    # 2. Missing value analysis
    missing_values = df.isnull().sum().sum()

    if missing_values > 0:

        insights.append({
            "type": "data_quality",
            "title": "Missing Values Detected",
            "description": (
                f"The dataset contains "
                f"{missing_values} missing values."
            )
        })

    else:

        insights.append({
            "type": "data_quality",
            "title": "Data Quality Good",
            "description": (
                "No missing values were detected."
            )
        })

    # 3. Numeric column analysis
    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    for column in numeric_columns:

        average = df[column].mean()
        maximum = df[column].max()
        minimum = df[column].min()

        insights.append({
            "type": "numeric_analysis",
            "title": f"Analysis of {column}",
            "description": (
                f"Average: {average:.2f}, "
                f"Maximum: {maximum}, "
                f"Minimum: {minimum}."
            )
        })

    return insights