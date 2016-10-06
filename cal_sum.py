from itertools import groupby

def calSum():
	recordDict = {}
	eachList = []
	recordlist = []
	resultDict = {}

	fr = open ('records.txt', 'r')

	for line in fr:
		eachList = line.strip().split()
		recordDict = {'name':eachList[1], 'money':eachList[2]}
		recordlist.append(recordDict)

	category = lambda x: x['name']

	for key, values in groupby(sorted(recordlist, key=category), category):
		sum = 0.00

		for value in values:
			sum = sum + float(value['money'])
		resultDict[key] = "{0:.2f}".format(sum)
		print resultDict
	return resultDict