import os
from datetime import datetime
import sqlite3 as sq
import pandas as pd

def exportFile(DirMain, df, excelexport, DataMissingdf, FileSelect):

    
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