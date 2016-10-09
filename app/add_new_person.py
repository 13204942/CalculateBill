
import check_person_exist

def add_person(newName):
	check_person_exist.checkFile()

	fw = open('person.txt','a+b')

	if newName == "":
		return "Empty input"
		fw.close()
	else:
		fw.write("\t" + newName)
		fw.close()
		return "Add new person successfully."