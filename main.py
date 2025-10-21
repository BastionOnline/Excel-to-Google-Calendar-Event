import os
import pandas as pd
from datetime import datetime
import sqlite3 as sq

from modules.fileSelect import cliMenu
from modules.formatting import columnFormat
from modules.export import exportFile
################################################################################################
#read ONLY certain columns from file
#clean empty rows
#export to csv
#how to make hidden file
#add if statment if wrong file is chosen


#how to add colour
#add description, strip it
#add reminders in time
#add database to compare upload
#add coloured tabs, need openpyxl installed
#setup directory navs

## FOUND ONLINE: ALWAYS COPY CSV TO TEXT EDITOR TO VERIFY OUTPUT
# IF COMMAS ARE IN ENTRIES, PUT IT IN QUOTES
# ADD NOTIFICATIONS FOR EVENTS, SET CALENDAR BEFORE CSV UPLOAD

################################################################################################



df, FileSelect, DirMain = cliMenu()
df = columnFormat(df)

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

# print("data missing")
# print(DataMissingdf)

# for missing in DataMissingdf:
#     print(missing)


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

#####################################################################################
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


##############################################################################################


POADir, File = os.path.split(FileSelect)

# POAMissing = os.path.join(POADir, "POAs that were can't be processed.xlsx")
dateofcreation = "created " + str(datetime.today().today().strftime('%b %#d, %Y')).replace(':',',').replace('.',',') + ".xlsx"
if len(DataMissingdf) == 0:
    TrialListFile = os.path.join(POADir, f"List of Trials - {dateofcreation}")
elif len(DataMissingdf) == 1:
    TrialListFile = os.path.join(POADir, f"List of Trials, {len(DataMissingdf)} error - {dateofcreation}")
else:
    TrialListFile = os.path.join(POADir, f"List of Trials, {len(DataMissingdf)} errors - {dateofcreation}")

########################################################################################################

exportFile(POADir, DirMain, df, TrialListFile, excelexport, DataMissingdf, FileSelect)
