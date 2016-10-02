
import check_person_exist

def add_person(newName):
	check_person_exist.checkFile()

	fw = open('person.txt','a+b')

	if newName == "":
		print ("Empty input")
		fw.close()
	else:
		fw.write("\t" + newName)
		fw.close()
		print ("Add new person successfully.")