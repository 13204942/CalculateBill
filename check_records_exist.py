import os

def checkFile():
	if os.path.isfile('./records.txt'):
		print "records.txt is found"
	createFile()

def createFile():
	newFile = open("records.txt","w")
	print "Create file records.txt."
	newFile.close()