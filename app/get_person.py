
import check_person_exist 

def get():
	check_person_exist.checkFile()

	fr = open('person.txt', 'r')

	for line in fr:
		personNames = line.strip().split()

	fr.close()
	return personNames
