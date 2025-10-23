document.addEventListener("DOMContentLoaded", async () => {
    const uploadExcelFileBtn = document.getElementById("uploadExcelFileBtn");

    uploadExcelFileBtn.addEventListener("click", async () => {
        try {
            alert("click")
            const excelFilePath = await window.pywebview.api.selectExcelFile()
            alert(excelFilePath)
        }
        catch {

        }
        
    }
    )
})