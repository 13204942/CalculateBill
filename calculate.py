import sys

import cal_sum
#import get_input
import check_records_exist

if __name__ == "__main__":
	try:
		check_records_exist.checkFile()

#		get_input.getInput()

		fr = open ('records.txt', 'r')
		cal_sum.calSum(fr)
		fr.close()

	except IOError as e:
  	  print "I/O error({0}): {1}".format(e.errno, e.strerror)
	except ValueError:
  	  print "Could not convert data to an integer."
	except:
  	  print "Unexpected error:", sys.exc_info()[0]