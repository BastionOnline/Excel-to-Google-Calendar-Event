import webview

from modules.apiModule import Api
from modules.pyinstallerBoilerplate import resource_path

################################################################################################
#how to add colour
#add reminders in time
#add coloured tabs, need openpyxl installed
# ADD NOTIFICATIONS FOR EVENTS, SET CALENDAR BEFORE CSV UPLOAD
################################################################################################

# enable for debugging
html_file = resource_path(r'.\frontend\index.html')
css_file = resource_path(r'.\frontend\assets\style.css')
js_file = resource_path(r'.\frontend\assets\script.js')


if __name__ == '__main__':
    api = Api(None)

    # api.jsonFilePath = jsonFilePath

    # Open the HTML file in a webview window
    window = webview.create_window("Google Calendar Event Maker", f"file://{html_file}", js_api=api)
    
    # Set the api self.window so python can push to it
    webview.start()
    # webview.start(debug=True)