import gspread
from oauth2client.service_account import ServiceAccountCredentials
 
# Make sure to name your sheet    
sheet_name = ''    
 
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
 
# Find a workbook by name and open the first sheet
sheet = client.open(sheet_name).sheet1
 
# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)