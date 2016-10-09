import os

def checkFile():
	if os.path.isfile('./person.txt'):
		print "person.txt is found"
	else:
		createFile()
		print "Create file person.txt."

def createFile():
	newFile = open("person.txt","w")
	newFile.close()