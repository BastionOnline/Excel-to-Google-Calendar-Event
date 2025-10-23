import os
import pandas as pd

def cliMenu():

    importcol = ["Subject", "Offence Number", "Start Date", "Start Time", "Description"]

    DirMain = os.getcwd()

    FileList = [f for f in os.listdir(DirMain) if f.endswith('.xlsx')]

    i = 0

    print("The following are the list of excel files in this folder:\n")

    while i < len(FileList):
        for files in FileList:
            print(f"{i+1}. {files}")
            i += 1


    while True:
        try:
            UserSelection = int(input("\nWhich file do you want trials for? "))

            if UserSelection < 0:
                print("File does not exist")
            elif UserSelection > len(FileList):
                print("File does not exist")
            else:
                try:
                    FileSelect = FileList[UserSelection-1]
                    filedir = os.path.join(DirMain, FileSelect)

                    df = pd.read_excel(FileSelect, sheet_name="POA Clients", usecols=importcol)

                    print(f"{FileList[UserSelection-1]} will be prepared to upload.\n")
                    break
                except Exception as e:
                    print(f"{type(e).__str__} {e}")
                    print("\nThis file is not formated correctly. Please ensure the sheet in excel is titled:\n\nPOA Clients\n")
        except Exception as e:
            print(f"Invalid entry: {type(e).__name__}: {e}")


    return df, FileSelect, DirMain