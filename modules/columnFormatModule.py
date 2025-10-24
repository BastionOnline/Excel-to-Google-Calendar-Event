import pandas as pd

def columnFormat(df):
    df = df.dropna(subset=["Subject"])
    # locate ' ' in start time and put true in 'Start Time'
    # Can't use df to df.loc
    # df = df.loc[df["Start Time"] == 'Empty', 'All Day Event'] = "True"


    # df.loc[df["Start Time"] == ' ', 'All Day Event'] = "TRUE"
    # df.loc[df["Start Time"] == ' ', 'Start Time'] = "00:00:00"


    # df.loc[df["End Date"] == ' ', 'End Date'] = "00:00:00"
    # df.loc[df["All Day Event"] == '0.0', 'All Day Event'] = 'FALSE'

    df['Start Date'] = pd.to_datetime(df["Start Date"], errors='coerce')
    df["Start Date"] = df["Start Date"].dt.strftime('%Y-%m-%d')


    # df['End Date'] = pd.to_datetime(df['End Date'], errors='coerce')

    # df['End Date'] = df['End Date'].dt.strftime('%Y-%m-%d')


    # print(df.loc[~df["All Day Event"] == "TRUE"])
    # Modify a specific cell with a boolean value
    # df.at[1, 'Boolean Column'] = True

    # print(df)

    # selection = df.iat[0, 2]
    # print(type(selection))

    df = df.reset_index(drop=True)
    return df