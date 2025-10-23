import pandas as pd

def missingIndex(df):
    DataMissingidx = []
    # # DataMissingrow = []
    # # DataMissingdf = pd.DataFrame(columns=df.columns)

    # # DataMissingdf = pd.DataFrame()


    # # print(DataMissingdf)
    # # h = 0



    #Use both index and its' content in a dataframe
    for idx, value in enumerate(df["Start Date"]):

        try:
            # try converting the VALUE

            # if h == 4:
            #     print("hi")

            # print(df)
            pd.to_datetime(value)


        except Exception:
            # if it DOESNT work, store it's index here
            DataMissingidx.append(idx)
            # DataMissingrow.append(df.iloc[idx])
            DataMissingdf = pd.concat([DataMissingdf, df.iloc[[idx]]], ignore_index=True)
            # DataMissingdf = DataMissingdf.append(df.iloc[idx], ignore_index=True)
            print(DataMissingdf)
            df.drop(idx)

    print("data missing")
    print(DataMissingdf)

    # for missing in DataMissingdf:
    #     print(missing)
    return df, DataMissingidx, DataMissingdf