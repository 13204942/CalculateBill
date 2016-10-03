import check_records_exist

def add(date,name,amount):
	check_records_exist.checkFile()

	fw = open('records.txt', 'a+b')

	if date == "" or name == "" or amount == "":
		print ("Empty input")
		fw.close()
	else:
		fw.write(date + "\t" + name + "\t" + amount + "\n")
		fw.close()
		print "Add new record successfully"