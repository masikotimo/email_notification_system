import xlrd
import json
import SendEmail

path_to_clientExcel = "3Dclientelle.xlsx"
path_to_adminExcel = "Administrators.xlsx"

#For Clientelle excel document
wbClient = xlrd.open_workbook(path_to_clientExcel)
sheet_client = wbClient.sheet_by_index(0)

#For Administrator excel document
wbAdmin = xlrd.open_workbook(path_to_adminExcel)
sheet_admin = wbAdmin.sheet_by_index(0)
 


client=[]
email=[]
admin=[]
admin_address=[]


#looping through client records
for i in range(1,sheet_client.nrows):

    if(int(sheet_client.cell_value(i,3))<=7):
        client.append( sheet_client.cell_value(i,0))
        email.append((sheet_client.cell_value(i,1)))


client_dictionary=(dict(zip(client,email))) 


#Getting Admin 
for i in range(1,sheet_admin.nrows):
    admin.append( sheet_admin.cell_value(i,0))
    admin_address.append((sheet_admin.cell_value(i,1)))


admin_dictionary=(dict(zip(admin,admin_address)))


#send to administrator
for key, value in admin_dictionary.items():
    SendEmail.sendEmailToCMS(str (key),str (value),client_dictionary)

# #send to client
# for key, value in client_dictionary.items():
#     SendEmail.sendEmailToClient(str (key),str (value))

