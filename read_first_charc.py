#!/bin/python

def read_first_letter(filename):
	"""
	Alternate solution to print 
	first character of the string
	read from a file.
	"""

	with open(filename) as fd:
		lines = fd.readlines()

	print "First letter from file : "
	for item in lines:
		strs = item.strip('\n')
		print "first letter :", strs[0]


def reverse_text(filename):
	"""
	Alternate solution to print 
	first character of the string
	read from a file.
	"""

	with open(filename) as fd:
		lines = fd.readlines()

	# List lines already a list
	file_lines_no_newline = [ item.strip('\n') for item in lines ]
	print
	print "Text from file : "
	for item in file_lines_no_newline:
		print item

        print
	# Prints to std-out.
	print "Reversed lines : "
	for item in file_lines_no_newline[::-1]:
		print item

def alternate(filename):
	"""
	Alternate solution to print 
	first character of the string
	read from a file.
	"""

	with open(filename) as fd:
		lines = fd.read()

	print 
	print "Alternate solution : "
	for item in lines.split("\n"):
		if item != "":
			print "first letter : ", item[0]


if __name__ == '__main__':

        filename = "first_letter_read.txt"
	read_first_letter(filename)
	alternate(filename)
	reverse_text(filename)

