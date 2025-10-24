import pandas as pd
import os
# import datetime
from datetime import datetime

def formatDate(df, date):
    # try to interpret whatever’s in this column as a date or datetime.
    df[date] = pd.to_datetime(df[date], errors='coerce')

    # formats datetime values back into string form — but in a consistent, clean format.
    df[date] = df[date].dt.strftime('%Y-%m-%d')

def stripEntry(df, column):
    df[column] = df[column].str.strip()


def formatTime(df, column):
    print(column)
    print(df)

    if (column == "Start Time"):
        df.loc[df[column] == ' ', column] = "00:00:00.000000"
        print(df)
    
    #convert WHATEVER you find into any datetime format
    #this approach is more broader and will capture more
    # df[column] = pd.to_datetime(df[column], errors='coerce')
    print(df[column].head())
    print(df[column].dtype)

    # reads it still as panda date type
    df[column] = pd.to_datetime(df[column], format='%H:%M:%S', errors='coerce')

    print('pd. to datetime')
    print(df)

    #convert what you found into hours, minutes, seconds
    df[column] = df[column].dt.strftime('%H:%M:%S')
    print(df)



def exportStandardFile(df, filePath):
    # drop or replace mandatory rows
    # df.loc[df["Subject"] == ' ', "Subject"] = "No Title"
    # today = datetime.now().date()
    # df.loc[df["Start Date"] == ' ', "Start Date"] = today
    
    df = df.dropna(subset=["Subject"])
    df = df.dropna(subset=['Start Date'])


    # replace user heading with correct heading

    # if start Date & Start Time == Same Column
        # duplicate them and title them differently
        # same with end date and end time

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

    path, fileName = os.path.split(filePath)

    currentDatetime = datetime.today().strftime('%b %#d, %Y %I-%M %p')
    googleFileName = f"Upload to Google - {fileName} {currentDatetime}.csv"
    googleFilePath = os.path.join(path, googleFileName)
    
    df.to_csv(googleFilePath, index=False, sep=",")

    eventsFound = df.shape[0]

    return eventsFound