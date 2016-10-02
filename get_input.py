import add_expend

def getInput():
	date = raw_input("Enter the date (dd/mm/yyyy): ")
	name = raw_input("Enter user name: ")
	amount = raw_input("Enter amount of money expended: ")

	fw = open('records.txt', 'a+b')
	add_expend.add(fw,date,name,amount)
	fw.close()
