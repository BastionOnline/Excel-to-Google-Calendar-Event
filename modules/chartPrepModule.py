def chartPrep(df):
    
    df['Start Date'] = df['Start Date'].str.strip()
    df['Subject'] = df['Subject'].str.strip()
    df['Description'] = df['Description'].str.strip()
    print(df)

    df.index = df.index+1
    print(df)

    excelexport = df.copy(deep=True)
    print(excelexport)


    DataMissingdf = df[df["Start Date"].isna()].copy(deep=True)
    print(DataMissingdf)

    # DataMissingdf = DataMissingdf.drop('All Day Event', axis=1)

    df = df.dropna(subset=['Start Date'])

    df = df.drop('Offence Number', axis=1)
    print(df)


    df = df.reset_index(drop=True)
    print("\nThis is the data frame")
    print(df)

    return df, excelexport