from itertools import groupby

def calSum(fr):
	recordDict = {}
	eachList = []
	recordlist = []

	for line in fr:
		eachList = line.strip().split()
		recordDict = {'name':eachList[1], 'money':eachList[2]}
		recordlist.append(recordDict)

	category = lambda x: x['name']

	for key, values in groupby(sorted(recordlist, key=category), category):
		print "--------------------------"
		print key
		sum = 0.00

		for value in values:
			sum = sum + float(value['money'])
		print sum
		print "\n"