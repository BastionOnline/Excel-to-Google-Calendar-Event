import os
import pandas as pd
from datetime import datetime
import sqlite3 as sq
from datetime import datetime
import json
import webview
import os
import sys
import threading
import traceback

from tkinter import filedialog
from modules.fileSelect import cliMenu
from modules.formatting import columnFormat
from modules.export import exportFile
from modules.blankFillerModule import blankFiller
from modules.missingIndexModule import missingIndex
from modules.chartPrepModule import chartPrep
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


class Api:
    # def __init__(self, window, jsonPath=jsonFile):
    def __init__(self, window, jsonPath):
        self.jsonPath = jsonPath
        self.balanceFilePath = None
        self.window = window


    def selectExcelFile(self):
        # use os.path.normpath to standardize path formats
        self.excelFilePath = os.path.normpath(filedialog.askopenfilename(
            title="Select a Balance file",
            filetypes=[("Excel Files", "*.xls *.xlsx")]
        ))
        print(self.excelFilePath)

        # setDefault("Balance", self.balanceFilePath, jsonFile)

        return self.excelFilePath

################################################################################################

def resource_path(relative_path):
    """ Get the absolute path to a resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temporary folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# enable for debugging
html_file = resource_path(r'.\frontend\index.html')
css_file = resource_path(r'.\frontend\assets\style.css')
js_file = resource_path(r'.\frontend\assets\script.js')


if __name__ == '__main__':
    # main()
    api = Api(None)

    # Open the HTML file in a webview window
    window = webview.create_window("Google Calendar Event Maker", f"file://{html_file}", js_api=api)
    
    # Set the api self.window so python can push to it
    webview.start()
    # webview.start(debug=True)
################################################################################################


df, FileSelect, DirMain = cliMenu()

df = columnFormat(df)

df, DataMissingidx, DataMissingdf = missingIndex(df)

df, excelexport = chartPrep(df)

#####################################################################################

df = blankFiller(df)

exportFile(DirMain, df, excelexport, DataMissingdf, FileSelect)
