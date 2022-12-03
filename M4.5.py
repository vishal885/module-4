#Write a Python program to read last n lines of a file.

def read_last_lines(filename, no_of_lines=1):
	file = open(filename,'r')
	lines = file.readlines()
	last_lines = lines[-no_of_lines:]
	for line in last_lines:
		print(line)
	file.close()
filename = "file2.txt"
read_last_lines(filename,1)
