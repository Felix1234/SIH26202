def predict_trend(df):

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    predictions = []

    for column in numeric_columns:

        values = df[column].dropna()

        if len(values) < 2:
            continue

        first_value = values.iloc[0]
        last_value = values.iloc[-1]

        if last_value > first_value:
            trend = "Increasing"

        elif last_value < first_value:
            trend = "Decreasing"

        else:
            trend = "Stable"

        predictions.append({
            "column": column,
            "trend": trend
        })

    return predictions