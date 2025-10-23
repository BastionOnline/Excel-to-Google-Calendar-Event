document.addEventListener("DOMContentLoaded", async () => {
    const uploadExcelFileBtn = document.getElementById("uploadExcelFileBtn");
    const sheetNameSelector = document.getElementById("sheetNameSelector");


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
                alert(sheet)
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