import pandas as pd

def blankFiller(df):
    #where there is a blank put time
    df.loc[df["Start Time"] == ' ', 'Start Time'] = pd.to_datetime("00:00:00", format='%H:%M:%S').time()


    # df['Start Time'] = df['Start Time'].fillna(pd.to_datetime("00:00:00", format='%H:%M:%S').time())
    print(df)

    #enumerate used to loop over AN ITERABLE (LIST, TUPLE, DATAFRAME) and keep track of INDEX
    for idx, time in enumerate(df['Start Time']):
        try:
            pd.to_datetime(time, format='%H:%M:%S').time()
            print(f"\n\n{idx}. is a time\n{time}")
        except:
            print("not a date")

    # print(df)

    # df.loc[df["Start Time"] == '', 'Start Time'] = "00:00:00.000000"

    # if df[df[0]]

    # for idx, date in enumerate(df['Start Date']):
    #     try:




    # df['Start Time'] = pd.to_datetime(df['Start Time'], format='%H:%M:%S',errors='coerce')
    # print('df pd. to datetime')
    # print(df)


    # df.replace("N")
    # print(df)



    # df["Start Time"] = df["Start Time"].dt.strftime('%H:%M:%S')
    # print(df)

    return df