import os

def checkFile():
	if os.path.isfile('./records.txt'):
		print "records.txt is found"
	else:
		createFile()
		print "Create file records.txt."

def createFile():
	newFile = open("records.txt","w")
	newFile.close()