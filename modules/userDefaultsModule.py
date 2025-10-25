import os
import json
from datetime import datetime

def createConfigFolder(folderName, fileName):
    # load json file path
    templateFolderDir = os.path.join(os.getcwd(), folderName)

    jsonFileName = fileName

    jsonFilePath = os.path.join(templateFolderDir, jsonFileName)
    print(jsonFilePath)

    print(os.path.exists(templateFolderDir))
    templateFolderStat = os.path.exists(templateFolderDir)

    return templateFolderDir, jsonFileName, jsonFilePath, templateFolderStat


def setDefault(key, value, jsonFilePath):
    try:
        with open(jsonFilePath, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    # Update the dictionary
    data[key] = value

    # Write the updated data back to the file (pretty format)
    with open(jsonFilePath, "w") as f:
        json.dump(data, f, indent=4)
    return


def createJson(templateFolderStat, templateFolderDir, jsonFilePath):
    if templateFolderStat == False:
        os.mkdir(templateFolderDir)

    print(os.path.exists(jsonFilePath))
    if os.path.exists(jsonFilePath) == False:
        data = {
            "Profiles": "",
            "Excel File": "",
            "Sheet Name": "",
            "Header Row Number": "",
            "Subject": "",
            "Start Date": "",
            "Start Time": "",
            "End Date": "",
            "End Time": "",
            "Description1": "",
            "Description2": "",
            "Description3": ""
        }

        with open(jsonFilePath, "w") as f:
            json.dump(data, f, indent=4)  
    return

# createJson()

def updateJsonExcel(templateFolderDir, jsonFilePath):
    presentExcelFiles = [
                            [["Balance"], ["1. Balance.xlsx"]],
                            [["Schedules"], ["2. Schedules.xlsx"]],
                            [["Sales"], ["3. Sales.xlsx"]],
                            [["Invoices"], ["4. Invoices.xlsx"]],
                            [["Hotel - Schedule"], ["5. Hotel - Schedule.xlsx"]]
                        ]

    # check if files exist in template folder
    for file in presentExcelFiles:
        filePath = os.path.join(templateFolderDir, file[1][0])
        if os.path.exists(filePath) == True:
            setDefault(file[0][0], filePath, jsonFilePath)
        else:
            setDefault(file[0][0], "", jsonFilePath)
    return

# updateJsonExcel()


def loadJson(self):
    with open(self.jsonFilePath, "r") as f:
        # userDefault is the entire json
        # jsonValue is the key
        userDefaults = json.load(f)
    return userDefaults

def defaultCheck(jsonValue, userDefaults):
    print(jsonValue)
    print(userDefaults)

    if jsonValue == "Customize Date":
        path = userDefaults.get(jsonValue)
        print(path)
        if path == "true":
            return {"location": "defaultCheck, key found, path valid", 
                    "error": "None",
                    "value": path,
                    "bool": True}
        else:
            return {"location": "defaultCheck, key found, path not valid",
                    "error": "create key, value pair",
                    "value": path,
                    "bool": False}
    elif jsonValue == "Header Row Number":
        path = userDefaults.get(jsonValue)

        # print(path, type(path))
        try:
            headerRow = int(path)

            if type(headerRow) == int:
                return {"location": "defaultCheck, key found, path valid", 
                        "error": "None",
                        "value": path,
                        "bool": True}
            else:
                return {"location": "defaultCheck, key found, path not valid",
                        "error": "create key, value pair",
                        "value": path,
                        "bool": False}
        except Exception as e:
            print(e)
            return {"location": "defaultCheck, exception block",
                    "error": "create key, value pair",
                    "value": path,
                    "bool": False}

    # check if the value is inside
    if jsonValue in userDefaults or userDefaults[jsonValue]:
        # best way to get a json value
        path = userDefaults.get(jsonValue)

        # tests to see if path returns None and a number
        if not path or not isinstance(path, str): # if path returns None, it is True, because None is falsy
            return {"location": "defaultCheck, path blank",
                    "error":"create key, value pair",
                    "value": path,
                    "bool": False}
        elif (os.path.exists(path) == True):
            return {"location": "defaultCheck, key found, path valid", 
                    "error": "None",
                    "value": path,
                    "bool": True}
        else:
            return {"location": "defaultCheck, key found, path not valid",
                    "error": "create key, value pair",
                    "value": path,
                    "bool": False}
    else:
        return {"location": "defaultCheck, key not seen",
                "error":"create key, value pair",
                "value": path,
                "bool": False}
