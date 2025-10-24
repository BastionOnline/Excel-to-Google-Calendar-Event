import pandas as pd
import os
from datetime import datetime
# replace user heading with correct heading

def formatDate(df, date):
    df[date] = pd.to_datetime(df[date], errors='coerce')
    df[date] = df[date].dt.strftime('%Y-%m-%d')
    # df['Start Date'] = pd.to_datetime(df["Start Date"], errors='coerce')
    # df["Start Date"] = df["Start Date"].dt.strftime('%Y-%m-%d')

def stripEntry(df, column):
    df[column] = df[column].str.strip()
    # df['Start Date'] = df['Start Date'].str.strip()
    # df['Subject'] = df['Subject'].str.strip()
    # df['Description'] = df['Description'].str.strip()

def formatTime(df, column):
    
    if (column == "Start Time"):
        df.loc[df[column] == ' ', column] = "00:00:00.000000"
        print(df)
    else:
        df.loc[df[column] == ' ', column] = "23:59:00.000000"
        print(df)

    #convert WHATEVER you find into any datetime format
    #this approach is more broader and will capture more
    df[column] = pd.to_datetime(df[column], errors='coerce')
    print('pd. to datetime')
    print(df)


    #convert what you found into hours, minutes, seconds
    df[column] = df[column].dt.strftime('%H:%M:%S')
    # return df


def exportStandardFile(df, filePath):
    # drop or replace mandatory rows
    df = df.dropna(subset=["Subject"])
    df = df.dropna(subset=['Start Date'])
    # df = df.reset_index(drop=True)

    # format date
    # x = value_if_true if condition else value_if_false
    # formatDate(df, "Start Date") if df["Start Date"] == True else pass
    formatDate(df, "Start Date")
    formatDate(df, "End Date") if "End Date" in df.columns else None


    formatTime(df, "Start Time") if "Start Time" in df.columns else None
    formatTime(df, "End Time") if "End Time" in df.columns else None


    stripEntry(df, "Subject")
    stripEntry(df, "Start Date")
    stripEntry(df, "Start Time") if "Start Time" in df.columns else None
    stripEntry(df, "End Date") if "End Date" in df.columns else None
    stripEntry(df, "End Time") if "End Time" in df.columns else None
    stripEntry(df, "Description") if "Description" in df.columns else None

    # dbprint = pd.read_sql("SELECT * FROM TRIALS", TrialdbConn)
    # dbcsvcopy = os.path.join(POADir, "Upload to Google - ALL current Trials as of " + str(datetime.today().date().strftime('%b %#d, %Y')) + ".csv")
    # dbprint.to_csv(dbcsvcopy,index=False, sep=",")
    # path.to_csv(pd,index=False, sep=",")

    path, fileName = os.path.split(filePath)

    currentDatetime = datetime.today().strftime('%b %#d, %Y %I-%M %p')
    # googleFileName = f"Upload to Google - {fileName} {str(datetime.today().date().strftime('%b %#d, %Y'))}.csv"
    # googleFilePath = os.path.join(os.getcwd(), googleFileName)
    googleFileName = f"Upload to Google - {fileName} {currentDatetime}.csv"
    googleFilePath = os.path.join(path, googleFileName)

    # googleFilePath.to_csv(df, index=False, sep=",")
    df.to_csv(googleFilePath, index=False, sep=",")