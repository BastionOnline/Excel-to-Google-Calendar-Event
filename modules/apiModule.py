from modules.userDefaultsModule import createConfigFolder, setDefault, createJson, updateJsonExcel, loadJson, defaultCheck
import os
from tkinter import filedialog

templateFolderDir, jsonFileName, jsonFilePath, templateFolderStat = createConfigFolder("profiles", "profiles")
createJson(templateFolderStat, templateFolderDir, jsonFilePath)


class Api:
    # def __init__(self, window, jsonPath=jsonFile):
    def __init__(self, window, jsonFilePath=jsonFilePath):
    # def __init__(self, window):
        self.jsonFilePath = jsonFilePath
        self.balanceFilePath = None
        self.window = window

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

        # setDefault("Balance", self.balanceFilePath, jsonFile)

        return self.excelFilePath
    
    # get df
    # set self values
    # Return sheets
    # get row number of headers
    # return headers
    # select headers for 
