import os
import pandas as pd
from datetime import datetime
import sqlite3 as sq

from modules.fileSelect import cliMenu
from modules.formatting import columnFormat
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



# importcol = ["Subject", "Offence Number", "Start Date", "Start Time", "Description"]

# DirMain = os.getcwd()

# FileList = [f for f in os.listdir(DirMain) if f.endswith('.xlsx')]

# i = 0

# print("The following are the list of excel files in this folder:\n")

# while i < len(FileList):
#     for files in FileList:
#         print(f"{i+1}. {files}")
#         i += 1


# while True:
#     try:
#         UserSelection = int(input("\nWhich file do you want trials for? "))

#         if UserSelection < 0:
#             print("File does not exist")
#         elif UserSelection > len(FileList):
#             print("File does not exist")
#         else:
#             try:
#                 FileSelect = FileList[UserSelection-1]
#                 filedir = os.path.join(DirMain, FileSelect)

#                 df = pd.read_excel(FileSelect, sheet_name="POA Clients", usecols=importcol)

#                 print(f"{FileList[UserSelection-1]} will be prepared to upload.\n")
#                 break
#             except Exception as e:
#                 print(f"{type(e).__str__} {e}")
#                 print("\nThis file is not formated correctly. Please ensure the sheet in excel is titled:\n\nPOA Clients\n")
#     except Exception as e:
#         print(f"Invalid entry: {type(e).__name__}: {e}")


# return df, FileSelect, DirMain



df, FileSelect, DirMain = cliMenu()





# # FileSelect = FileList[UserSelection-1]

# # print(FileSelect)

# # filedir = os.path.join(DirMain, FileSelect)



# # df = pd.read_excel(FileSelect, sheet_name="POA Clients", usecols=importcol)


# # df = df.dropna(subset=["Start Time"]) DID NOT CLEAR BLANKS
# # df.replace(" ", "Empty", inplace=True)
# # df = df.dropna(subset=["Subject"])


# # df = df.dropna(subset=["Start Time"])
# df = df.dropna(subset=["Subject"])



# # df = df.loc[df.ne("Empty").any(axis=1)]
# # df = df.loc[~(df["Start Time"] == 'Empty')]

# # locate ' ' in start time and put true in 'Start Time'
# # Can't use df to df.loc
# # df = df.loc[df["Start Time"] == 'Empty', 'All Day Event'] = "True"


# # df.loc[df["Start Time"] == ' ', 'All Day Event'] = "TRUE"
# # df.loc[df["Start Time"] == ' ', 'Start Time'] = "00:00:00"


# # df.loc[df["End Date"] == ' ', 'End Date'] = "00:00:00"
# # df.loc[df["All Day Event"] == '0.0', 'All Day Event'] = 'FALSE'

# df['Start Date'] = pd.to_datetime(df["Start Date"], errors='coerce')

# df["Start Date"] = df["Start Date"].dt.strftime('%Y-%m-%d')


# # df['End Date'] = pd.to_datetime(df['End Date'], errors='coerce')

# # df['End Date'] = df['End Date'].dt.strftime('%Y-%m-%d')


# # print(df.loc[~df["All Day Event"] == "TRUE"])
# # Modify a specific cell with a boolean value
# # df.at[1, 'Boolean Column'] = True

# # print(df)

# # selection = df.iat[0, 2]
# # print(type(selection))

# df = df.reset_index(drop=True)


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
# SQL to CSV or just go to csv
    
csvfiledir = os.path.join(POADir, "Upload to Google - Trials as of " + str(datetime.today().date().strftime('%b %#d, %Y')) + ".csv")


Trialdbname = 'Trials Uploaded.db'

dbfile = os.path.join(DirMain, Trialdbname)

comptable = df.copy(deep=True)






# x = 0
# if x==0:
try:

    # if os.path.exists(dbfile):
    TrialdbConn = sq.connect(Trialdbname)
    TrialdbCursor = TrialdbConn.cursor()

    #SELECT * gets ENTIRE db, SELECT COUNT *, counts the rows
    TrialdbCursor.execute('SELECT COUNT (*) FROM TRIALS')

    TrialEntries = TrialdbCursor.fetchone()

    if TrialEntries [0] > 0:
        query = "SELECT * FROM TRIALS"
        Traildb = pd.read_sql(query, TrialdbConn)


        print("traildb")
        print(Traildb)
        print(df.columns)

        print(Traildb.head())
        
        print(type(Traildb))
        print(Traildb.info())
        print(Traildb.columns)


        #had overlapping variables
        Traildb['Start Date'] = pd.to_datetime(Traildb['Start Date'])
        #why could I reference it by string before and now it has to be index?
        #need to change start time format, not start date
        Traildb['Start Date'] = Traildb['Start Date'].dt.strftime('%Y-%m-%d')

        print(Traildb)


        #[[0]] gets row, [0], gets row as coloum
        # print(Traildb.loc[[0]])


        Traildb.loc[Traildb["Start Time"] == ' ', 'Start Time'] = "00:00:00.000000"
        # Traildb['Start Time'] = Traildb['Start Time'].fillna('00:00:00')


        print('fillna')
        print(Traildb)

        #convert WHATEVER you find into any datetime format
        #this approach is more broader and will capture more
        Traildb['Start Time'] = pd.to_datetime(Traildb['Start Time'], errors='coerce')
        print('pd. to datetime')
        print(Traildb)


        #convert what you found into hours, minutes, seconds
        Traildb["Start Time"] = Traildb["Start Time"].dt.strftime('%H:%M:%S')
        
        print('dt.strfttime')
        print(Traildb)


    #####################################################################################

    # trialrow = 1

    # Traildb.apply(lambda trialrow: compare_rows(trialrow, df), axis=1)

    #####################################################################################
        # Traildb['Subject','Start Date','Start Time','Description'].str.strip()
        # df['Start Time'] = pd.to_datetime(df['Start Time'], format='%H:%M:%S',errors='coerce')


        # print('post strip')
        # print(df)


        # pd.merge(df,Traildb,how='left',)

        # dftotal = len(df)
        traildbttoal = len(Traildb)

        compcol = 'Description'
        missing = 0

        print("Now checking Excel for updates")

        for idxa, rowa in comptable.iterrows():
            print(f"\n---------- Item {idxa+1}-----------")
            print(f"idxa: {idxa}")
            print(f"rowa: \n{rowa}\n")

            present = 0
            # missing = 0
            print(f'\nLength of comparision table is {len(comptable)} entries')
            print(comptable)
            
            print(f"---------- Item {idxa+1}-----------")

            for idxb, rowb in Traildb.iterrows():
                if (rowa[compcol] == rowb[compcol]):
                    print(f"\nExcel trial {idxa} found in database, index {idxb}:")
                    print(rowa)

                    #NEED TO REFERENCE YOURSLEF WHEN DROPPING
                    comptable = comptable.drop(idxa)
                    Traildb = Traildb.drop(idxb)
                    print(f"\nTrial {idxa} removed from export list")
                    print(f"length of trials to copy is now {len(comptable)}")
                    break
                    # present +=1


                elif present == 1:
                    comptable.drop(idxa)
                    print(f"\nExcel trial {idxa} dropped from export list")
                    print(rowa)
                    print(len(comptable))
                    missing = 0


                else:
                    print(f"\nExcel trial {idxa} does not match database index {idxb}")
                    print(rowb)
                    missing += 1
                    print(f"{missing} in total are missing from database")

        print("\nUpdate Check complete.")
        print(f"Total copy list is {len(comptable)}")
        Trialsfound = len(comptable)
        
        comptable.reset_index().index+1
        print(comptable)
        if len(comptable) > 0:
            with pd.ExcelWriter(TrialListFile) as writer:

                excelexport.to_excel(writer, sheet_name="List of Trials", index=True)
                if DataMissingdf > 0:
                    DataMissingdf.to_excel(writer,sheet_name="Not Uploaded", index=True)
                else:
                    pass


            comptable.to_sql(Traildb, TrialdbConn, index=False,if_exists='append')
                #This gets the following xlsxwriter objects
                # workbook = writer.book
                # worksheet = writer.sheets['Not Uploaded']

                # #creates red tab
                # tabcolour = '#FF0000'
                # tabformat = workbook.add_format({'tabcolor': tabcolour})

                # worksheet.set_tab_colour(tabcolour)

        else:
            print("No new trails found\n")
            dbrq = int(input("Would you like a complete list trials in the database?\n\nType 1 for yes, 2 for no: "))
            if dbrq == 1:
                dbprint = pd.read_sql("SELECT * FROM TRIALS", TrialdbConn)

                dbcsvcopy = os.path.join(POADir, "Upload to Google - ALL current Trials as of " + str(datetime.today().date().strftime('%b %#d, %Y')) + ".csv")
                dbexcelcopy = os.path.join(POADir, "ALL current Trials as of " + str(datetime.today().date().strftime('%b %#d, %Y')) + ".xlsx")

                dbprint.to_csv(dbcsvcopy,index=False, sep=",")
                dbprint.to_excel(dbexcelcopy,sheet_name="All Trials in DB")
                                
                TrialdbCursor.close()
                TrialdbConn.close()

            else:
                with open('No new trails found.txt', 'w') as file:
                    file.write(f"No new trials found in {FileSelect}")

                TrialdbCursor.close()
                TrialdbConn.close()

    else:
        df.to_sql('Trials', TrialdbConn, index=False, if_exists='append')

        TrialdbCursor.close()
        TrialdbConn.close()

        df.to_csv(csvfiledir,index=False, sep=",")


        with pd.ExcelWriter(TrialListFile, engine='openpyxl') as writer:

            excelexport.to_excel(writer, sheet_name="List of Trials", index=True)

            DataMissingdf.to_excel(writer,sheet_name="Not Uploaded", index=True)


except Exception as e:
    df.to_sql('Trials', TrialdbConn, index=False, if_exists='append')

    TrialdbCursor.close()
    TrialdbConn.close()

    df.to_csv(csvfiledir,index=False, sep=",")
    try:

        with pd.ExcelWriter(TrialListFile, engine='openpyxl') as writer:

            excelexport.to_excel(writer, sheet_name="List of Trials", index=True)

            DataMissingdf.to_excel(writer,sheet_name="Not Uploaded", index=True)

    except PermissionError:
        with open("Please close the excel document POA Clients.txt", 'w') as file:
            file.write(f"Please close {FileSelect} to allow for updating.")



############################################################################################################



# POADir, File = os.path.split(file)

# csvfiledir = os.path.join(POADir, "Upload to google.csv")

# POAMissing = os.path.join(POADir, "POAs that were can't be processed.txt")

# df.to_csv(csvfiledir,index=False, sep=",")

# i = 0

# This itemized every column
# missingcaselist = []

# for case in DataMissingdf:
#     missingcaselist.append(str(i+1) + ". " + str(case) + "\n")


# DataMissingdf = DataMissingdf.reset_index(drop=True)
# #dont forget to add .index to the variable at the start
# DataMissingdf.index = DataMissingdf.index +1
# DataMissingdfString = DataMissingdf.to_string(index=False)
# print(DataMissingdfString)

# df = df.reset_index(drop=True)

# print("final df")
# print(df)

# print("missing entries")
# print(DataMissingdf)

# with open(POAMissing, 'w') as file:
#     file.write("The following cases were not able to be added to your calendar:\n")
#     file.write(DataMissingdfString)
#     # for case in missingcaselist:
#     #     file.write(case)


#     #ERROR CAME FORE THIS STATING WRITE ONLY TAKES 1 ARGUMENT
#     # for case in DataMissing:
#     #     file.write(str(i+1), ". " + str(case) + "\n")


# # print("this is the final df")
# # print(df)


# this copies single columns at a time
# updf = []

# for cols in importcol:
#     df = pd.read_excel(file,sheet_name="POA Clients", usecols=[cols])
#     updf.append(df)

# for x in updf:
#     print(x)