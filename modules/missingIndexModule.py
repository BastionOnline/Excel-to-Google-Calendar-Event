import pandas as pd

def missingIndex(df):
    DataMissingidx = []
    DataMissingdf = pd.DataFrame(columns=df.columns)

    #Use both index and its' value in a dataframe
    for idx, value in enumerate(df["Start Date"]):
        try:
            # try converting the VALUE
            print(f"index {idx}")
            print(f"index {value}")
            pd.to_datetime(value)


        except Exception:
            # if it DOESNT work, store it's index here
            DataMissingidx.append(idx)
            # DataMissingrow.append(df.iloc[idx])
            DataMissingdf = pd.concat([DataMissingdf, df.iloc[[idx]]], ignore_index=True)
            # DataMissingdf = DataMissingdf.append(df.iloc[idx], ignore_index=True)
            print(DataMissingdf)
            df.drop(idx)

    print(f"data missing\n {DataMissingdf}")
    return df, DataMissingidx, DataMissingdf