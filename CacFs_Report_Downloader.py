import PyPDF2
import os
import sys
import shutil # Used for copy files from SRC to DST.

#######################################################################
#Collecting Path

pathFile = raw_input("Please Enter Your PDF Report File Path :  ")
fileType = raw_input("Select the type of the file you want to download : \nPress 1 for PDF. \nPress 2 for Word\n")
clientName = os.path.basename(pathFile)
#######################################################################
#Downloaded Report Path

pathname = os.path.dirname(sys.argv[0])
pathname = os.path.abspath(pathname)
downDir = pathname+"\Downloaded_Reports"

if not os.path.exists(downDir+"\\"+clientName):
	os.makedirs(downDir+"\\"+clientName)
else:
	pass

downDir = os.getcwd()+"\Downloaded_Reports\\"+clientName

########################################################################
#Checking All the PDF files
if fileType == "1":
	fileFormat = ".pdf"
elif fileType == "2":
	fileFormat = ".docm"
else:
	print "Please select the right type of file you want to download."
	sys.exit()
	
for root, dirs, files in os.walk(pathFile):
    path = root.split(os.sep)
    for file in files:
        if file.endswith(fileFormat):
            print "Downloading file....... :"+file
            shutil.copy2(root+'//'+file,downDir)
        else:
            pass


print "All file downloaded to the folder : "+downDir