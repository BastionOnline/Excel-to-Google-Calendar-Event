document.addEventListener("DOMContentLoaded", async () => {
    const uploadExcelFileBtn = document.getElementById("uploadExcelFileBtn");
    const sheetNameSelector = document.getElementById("sheetNameSelector");
    const headerInputSelector = document.getElementById("headerInputSelector");
    const eventNameSelector = document.getElementById("eventNameSelector");
    const eventStartDateSelector = document.getElementById("eventStartDateSelector");
    const eventStartTimeSelector = document.getElementById("eventStartTimeSelector");
    const eventEndDateSelector = document.getElementById("eventEndDateSelector");
    const eventEndTimeSelector = document.getElementById("eventEndTimeSelector");
    const eventDescriptionSelector = document.getElementById("eventDescriptionSelector");
    const startBtn = document.getElementById("start");

    uploadExcelFileBtn.addEventListener("click", async () => {
        try {
            // alert("click")
            const excelData = await window.pywebview.api.selectExcelFile()
            const excelSheets = JSON.parse(excelData.sheets)
            const excelFilePath = excelData.path
            // alert(excelData)
            // alert(excelFilePath)
            // alert(excelSheets)
            // alert(excelSheets[0])

            excelSheets.forEach(sheet => {
                // alert(sheet)
                const option = document.createElement("option")
                option.value = sheet
                option.textContent = sheet
                sheetNameSelector.appendChild(option)
            });
        }
        catch {
        }
       
    }
    )

    startBtn.addEventListener("click", async () => {
        try {
            // alert("start clicked")
            const start = await window.pywebview.api.startCalendar()
            alert(start)
        } catch {

        }
    })

    sheetNameSelector.addEventListener("change", async () => {
        try {
            // alert(sheetNameSelector.value)
            const sheetNameSelected = await window.pywebview.api.selectSheetName(sheetNameSelector.value)
            // alert(sheetNameSelected)
        } catch {

        }
    })


    headerInputSelector.addEventListener("change", async () => {
        // alert("change detected!")
        try{
            // clear all children options for selector
            headerInputValue = headerInputSelector.value
            // alert(headerInputValue)
            const headerJson = await window.pywebview.api.selectHeaderInput(headerInputValue)
            // alert(headerJson)

            // se

            headerJson.forEach(header => {
                // alert(`header is ${header}`)
                const selectors = [
                    eventNameSelector,
                    eventStartDateSelector,
                    eventStartTimeSelector,
                    eventEndDateSelector,
                    eventEndTimeSelector,
                    eventDescriptionSelector
                ];

                selectors.forEach( selector => {
                    // alert(`selector is ${selector}`)
                    const option = document.createElement("option");
                    option.value = header;
                    option.innerHTML = header;
                    selector.appendChild(option);    
                });
            })
        } catch {

        }
    })

    eventNameSelector.addEventListener("change", async () => {
        try {
            const eventName = await window.pywebview.api.selectEventNameInput(eventNameSelector.value)
            // alert(eventName)
        } catch {

        }
    })

    eventStartDateSelector.addEventListener("change", async () => {
        try {
            const eventStartDate = await window.pywebview.api.selectEventStartDateInput(eventStartDateSelector.value)
            // alert(eventStartDate)
        } catch {

        }
    })

    eventStartTimeSelector.addEventListener("change", async () => {
        try {
            const eventStartTime = await window.pywebview.api.selectEventStartTimeInput(eventStartTimeSelector.value)
            // alert(eventStartTime)
        } catch {

        }
    })

    eventEndDateSelector.addEventListener("change", async () => {
        try {
            const eventEndDate = await window.pywebview.api.selectEventEndDateInput(eventEndDateSelector.value)
            // alert(eventEndDate)
        } catch {

        }
    })

    eventEndTimeSelector.addEventListener("change", async () => {
        try {
            const eventEndTime = await window.pywebview.api.selectEventEndTimeInput(eventEndTimeSelector.value)
            // alert(eventEndTime)
        } catch {

        }
    })

    eventDescriptionSelector.addEventListener("change", async () => {
        try {
            const eventDescription = await window.pywebview.api.selectEventDescription(eventDescriptionSelector.value)
            // alert(eventDescription)
        } catch {
            
        }
    })

})