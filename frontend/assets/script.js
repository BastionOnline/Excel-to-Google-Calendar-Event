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


    sheetNameSelector.addEventListener("change", async () => {
        try {
            // alert(sheetNameSelector.value)
            const sheetNameSelected = await window.pywebview.api.selectSheetName(sheetNameSelector.value)
            alert(sheetNameSelected)
        } catch {

        }
    })

    headerInputSelector.addEventListener("change", async () => {
        // alert("change detected!")
        try{
            headerInputValue = headerInputSelector.value
            alert(headerInputValue)
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
                
                // eventStartDateSelector.appendChild(option);
                // eventStartTimeSelector.appendChild(option);
                // eventEndDateSelector.appendChild(option);
                // eventEndTimeSelector.appendChild(option);
                // eventDescriptionSelector.appendChild(option);
            })
        } catch {

        }
    })


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
})