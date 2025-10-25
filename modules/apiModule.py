import os
import pandas as pd
import json

from tkinter import filedialog
from modules.userDefaultsModule import createConfigFolder, setDefault, createJson, updateJsonExcel, loadJson, defaultCheck
# from modules.cliMenuModule import cliMenu
from modules.columnFormatModule import columnFormat
from modules.exportFileModule import exportFile
from modules.blankFillerModule import blankFiller
from modules.missingIndexModule import missingIndex
from modules.chartPrepModule import chartPrep
from modules.exportStandardFileModule import exportStandardFile


templateFolderDir, jsonFileName, jsonFilePath, templateFolderStat = createConfigFolder("profiles", "profiles")
createJson(templateFolderStat, templateFolderDir, jsonFilePath)


class Api:
    # def __init__(self, window, jsonPath=jsonFile):
    def __init__(self, window, jsonFilePath=jsonFilePath):
        self.jsonFilePath = jsonFilePath
        self.balanceFilePath = None
        self.window = window
        self.sheetName = None
        self.headerInput = None

    def loadUserDefaults(self, jsonValue):
        try:
            if os.path.exists(self.jsonPath):
                # if there is a json file load it
                userDefaults = loadJson(self)

                # check value sent from json to see if it is present
                print(userDefaults)
                requestedValue = defaultCheck(jsonValue, userDefaults)
                return requestedValue

            # if there is no json file, make one
            else:
                userDefaults = createJson()
                requestedValue = False
                # need to send a request to select model
                return requestedValue
            
        except Exception as e:
            print(e)
            return {"location": "exception block",
                    "value": "create key, value pair"}

    def checkUserDefaults(self, jsonValue):
        try:
            print(jsonValue)
            if os.path.exists(self.jsonPath):
                # if there is a json file load it
                userDefaults = loadJson(self)

                # check value sent from json to see if it is present
                print(userDefaults)
                requestedValue = defaultCheck(jsonValue, userDefaults)
                return requestedValue
            else:
                createJson()
                requestedValue = defaultCheck(jsonValue, userDefaults)
                return requestedValue
            
        except Exception as e:
            print(e)
            return requestedValue


    def selectExcelFile(self):
        # use os.path.normpath to standardize path formats
        self.excelFilePath = os.path.normpath(filedialog.askopenfilename(
            title="Select a Balance file",
            filetypes=[("Excel Files", "*.xls *.xlsx")]
        ))
        print(self.excelFilePath)

        # return Excel pages found
        excelFile = pd.ExcelFile(self.excelFilePath)
        sheetNames = excelFile.sheet_names
        print(sheetNames)
        jsonSheetNames = json.dumps(sheetNames)
        print(jsonSheetNames)

        pathAndSheets = [self.excelFilePath, jsonSheetNames]
        print(pathAndSheets)

        # return with json to use as array in JS, NOT string
        return {
            "path": self.excelFilePath,
            "sheets": jsonSheetNames
        }
    
    def selectSheetName(self, sheetName):
        self.sheetName = sheetName
        print(self.sheetName)
        return self.sheetName


    def selectHeaderInput(self, headerInput):
        self.headerInput = int(headerInput)

        print(self.headerInput)
    
        df = pd.read_excel(self.excelFilePath, sheet_name=self.sheetName, header=self.headerInput - 1)
        headers = df.columns.tolist()

        # setDefault("Year", self.yearValue, jsonFile)

        # return self.headerInput
        return headers
    
    def selectEventNameInput(self, eventNameSelector):
        self.eventNameInput = eventNameSelector
        print(self.eventNameInput)

        return self.eventNameInput
    
    def selectEventStartDateInput(self, eventStartDateSelector):
        self.eventStartDateInput = eventStartDateSelector
        print(self.eventStartDateInput)

        return self.eventStartDateInput
    
    def selectEventStartTimeInput(self, eventStartTimeSelector):
        self.eventStartTimeInput = eventStartTimeSelector
        print(self.eventStartTimeInput)

        return self.eventStartTimeInput
    
    def selectEventEndDateInput(self, eventEndDateSelector):
        self.eventEndDateInput = eventEndDateSelector
        print(self.eventEndDateInput)

        return self.eventEndDateInput

    def selectEventEndTimeInput(self, eventEndTimeSelector):
        self.eventEndTimeInput = eventEndTimeSelector
        print(self.eventEndTimeInput)

        return self.eventEndTimeInput
    
    def selectEventDescription1(self, eventDesriptionSelector1):
        self.eventDescriptionInput1 = eventDesriptionSelector1
        print(eventDesriptionSelector1)

        return self.eventDescriptionInput1
    
    def selectEventDescription2(self, eventDesriptionSelector2):
        self.eventDescriptionInput2 = eventDesriptionSelector2
        print(self.eventDescriptionInput2)

        return self.eventDescriptionInput2
    
    def selectEventDescription3(self, eventDesriptionSelector3):
        self.eventDescriptionInput3 = eventDesriptionSelector3
        print(self.eventDescriptionInput3)

        return self.eventDescriptionInput3
    
    def startCalendar(self):
        # mandatory fields:
        # Subject, start datetime *add note, events will be created as ALL day if time is not given

        # df = pd.read_excel(FileSelect, sheet_name="POA Clients", usecols=importcol)
        fields = [
            getattr(self, "eventNameInput", ""), 
            getattr(self, "eventStartDateInput", ""),
            getattr(self, "eventStartTimeInput", ""),
            getattr(self, "eventEndDateInput", ""),
            getattr(self, "eventEndTimeInput", ""),
            getattr(self, "eventDescriptionInput1",""),
            getattr(self, "eventDescriptionInput2",""),
            getattr(self, "eventDescriptionInput3","")
            ]
        
        # googleProps = {
        #     "Subject": self.eventNameInput,
        #     "Start Date": self.eventStartDateInput,
        #     "Start Time": self.eventStartTimeInput,
        #     "End Date": self.eventEndDateInput,
        #     "End Time": self.eventEndTimeInput,
        #     "Description1": self.eventDescriptionInput1,
        #     "Description2": self.eventDescriptionInput2,
        #     "Description3": self.eventDescriptionInput3
        # }


        importcol = [val for val in fields if val != ""]
        print(importcol)

        fileSelect = self.excelFilePath
        print(fileSelect)

        df = pd.read_excel(self.excelFilePath, sheet_name=self.sheetName, usecols=importcol, header=self.headerInput-1)
        print(df)

        if (importcol == ["Subject", "Offence Number", "Start Date", "Start Time", "Description"]):
            DirMain = os.getcwd()
            df = blankFiller(df)
            df = columnFormat(df)
            df, DataMissingidx, DataMissingdf = missingIndex(df)
            df, excelexport = chartPrep(df)
            exportFile(DirMain, df, excelexport, DataMissingdf, fileSelect)
        else:
            # RETURN values for user to select
            # export selection
            eventsFound = exportStandardFile(df, fileSelect, self)
            # check what values are given
            return eventsFound
