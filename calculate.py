import sys

import cal_sum
import add_expend
import check_records_exist

if __name__ == "__main__":
	try:
		check_records_exist.checkFile()

		fw = open ('records.txt', 'a+b')
		add_expend.add(fw)
		fw.close()

		fr = open ('records.txt', 'r')
		cal_sum.calSum(fr)
		fr.close()

	except IOError as e:
  	  print "I/O error({0}): {1}".format(e.errno, e.strerror)
	except ValueError:
  	  print "Could not convert data to an integer."
	except:
  	  print "Unexpected error:", sys.exc_info()[0]