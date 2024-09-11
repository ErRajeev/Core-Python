# import sys
# n = len(sys.argv)
# sum = 0
# for i in range(1, n):
#     sum += int(sys.argv[i])

# print(sum)
# # print(sys.argv[1] + ' Ranjan')

# import sys

# n = sys.argv
# print("Your Id is : ", sys.argv[1])
# print("Your Name is : ", sys.argv[2])




# Python program to demonstrate
# command line arguments


import getopt, sys


# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]

# Options
options = "hmo:"

# Long options
long_options = ["Help", "My_file", "Output="]

try:
	# Parsing argument
	arguments, values = getopt.getopt(argumentList, options, long_options)
	
	# checking each argument
	for currentArgument, currentValue in arguments:

		if currentArgument in ("-h", "--Help"):
			print ("Displaying Help")
			
		elif currentArgument in ("-m", "--My_file"):
			print ("Displaying file_name:", sys.argv[0])
			
		elif currentArgument in ("-o", "--Output"):
			print (("Enabling special output mode (% s)") % (currentValue))
			
except getopt.error as err:
	# output error, and return with an error code
	print (str(err))
