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



def exportStandardFile(df, filePath, self):
    # drop or replace mandatory rows
    # df.loc[df["Subject"] == ' ', "Subject"] = "No Title"
    # today = datetime.now().date()
    # df.loc[df["Start Date"] == ' ', "Start Date"] = today

    def sameInputCheck(df, selfDate, selfTime, dateCol, timeCol):
        print(selfDate)
        print(selfTime)
        print(dateCol)
        print(timeCol)
        # print(self.eventStartDateInput)
        # print(self.eventStartTimeInput)
        # print(self.eventEndDateInput)
        # print(self.eventEndTimeInput)

        # If Start Date and Start Time come from the same column
        # if self.eventStartDateInput == self.eventStartTimeInput:
        if selfDate == selfTime:
            # Duplicate that column into both standardized names


            # If "Start Date" column exists, build "Start Time" from it
            if dateCol in df.columns:
                # df[dateCol] = df[date]
                df[timeCol] = df[dateCol]
                # df.rename(columns={date: dateCol}, inplace=True)
                # df.drop(columns=date, inplace=True)

            # If "Start Time" column exists, build "Start Date" from it
            # elif time in df.columns:
            else:
                df[dateCol] = df[timeCol]
                # df.rename(columns={time: "Start Time"}, inplace=True)

                # df[timeCol] = df[time]
                # df.drop(columns=time, inplace=True)

            # else:
            #     pass
            
        print(df)

            # # If "Start Date" column exists, build "Start Time" from it
            # if self.eventStartDateInput in df.columns and self.eventStartTimeInput not in df.columns:
            #     df["Start Time"] = df[self.eventStartDateInput]

            # # If "Start Time" column exists, build "Start Date" from it
            # elif self.eventStartTimeInput in df.columns and self.eventStartDateInput not in df.columns:
            #     df["Start Date"] = df[self.eventStartTimeInput]



            # startDateTimeCol = [self.eventStartDateInput, self.eventStartTimeInput]
            # existingCols = [c for c in startDateTimeCol if c in df.columns]
            # print(existingCols)
            
            # if (existingCols == "Start Date"):
            #     df["Start Time"] = df[self.eventStartTimeInput]
            # else:
            #     df["Start Date"] = df[self.eventStartDateInput]
            
            # df.drop(columns=[self.eventStartTimeInput, self.eventStartDateInput], inplace=True)


        # same with end date and end time
        # if (self.eventEndDateInput == self.eventEndTimeInput):
        #     df["End Date"] = df[self.eventEndDateInput]
        #     df["End Time"] = df[self.eventEndTimeInput]

        # print(df)



    # cols = ["Description1", "Description2", "Description3"]
    def mergeDescriptions(df, self):
        descriptionCols = [self.eventDescriptionInput1, self.eventDescriptionInput2, self.eventDescriptionInput3]
        existingCols = [c for c in descriptionCols if c in df.columns]
        print(existingCols)

        # fills blanks in
        # converts to string
        df["Description"] = df[existingCols].fillna('').astype(str).agg('\n'.join, axis=1)
        # df["Description"] = df[existingCols].fillna('').agg('\n'.join, axis=1)

        df.drop(columns=existingCols, inplace=True)

        print(df)
    
        # replace user heading with correct heading
    
    # add condition in case something is not present
    # make sure description is optional
    df.rename(columns={
        self.eventNameInput: "Subject",
        self.eventStartDateInput: "Start Date",
        self.eventStartTimeInput: "Start Time",
        self.eventEndDateInput: "End Date",
        self.eventEndTimeInput: "End Time"
        # self.eventDescriptionInput1: "Description1",
        # self.eventDescriptionInput2: "Description2",
        # self.eventDescriptionInput3: "Description3"
    }, inplace=True)

    print(df)


    # date, time, dateCol, timeCol
    sameInputCheck(df, self.eventStartDateInput, self.eventStartTimeInput, "Start Date", "Start Time")
    sameInputCheck(df, self.eventEndDateInput, self.eventEndTimeInput, "End Date", "End Time")
    mergeDescriptions(df, self)



    
    print(df)

    # once correct headings are given, then dump empty
    df = df.dropna(subset=["Subject"])
    df = df.dropna(subset=['Start Date'])

    print(df)

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

    path, fileNameExt = os.path.split(filePath)
    fileName, ext = os.path.splitext(fileNameExt)

    currentDatetime = datetime.today().strftime('%b %#d, %Y %I-%M %p')
    googleFileName = f"Upload to Google - {fileName} - {currentDatetime}.csv"
    googleFilePath = os.path.join(path, googleFileName)
    
    df.to_csv(googleFilePath, index=False, sep=",")

    eventsFound = df.shape[0]

    return eventsFound