# Agent that solves Sudoku puzzles





""" Reads sudoku puzzle from file, each row represents one section, 9 sections total
	
Ex. 
For the puzzle:
8 0 0   4 0 6   0 0 7   
0 0 0   0 0 0   4 0 0   
0 1 0   0 0 0   6 5 0   

5 0 9   0 3 0   7 8 0   
0 0 0   0 7 0   0 0 0   
0 4 8   0 2 0   1 0 3   

0 5 2   0 0 0   0 9 0   
0 0 1   0 0 0   0 0 0   
3 0 0   9 0 2   0 0 5  

8,0,0,0,0,0,0,1,0 would be line 1 of input,
4,0,6,0,0,0,0,0,0 would be line 2 of input,
etc.

Stored in nested array with each index representing a section which contains another array.
For the puzzle above, resulting data structure is:
[['8', '0', '0', '0', '0', '0', '0', '1', '0'], ['4', '0', '6', '0', '0', '0', '0', '0', '0'], ['0', '0', '7', '4', '0', '0', '6', '5', '0'], 
['5', '0', '9', '0', '0', '0', '0', '4', '8'], ['0', '3', '0', '0', '7', '0', '0', '2', '0'], ['7', '8', '0', '0', '0', '0', '1', '0', '3'], 
['0', '5', '2', '0', '0', '1', '3', '0', '0'], ['0', '0', '0', '0', '0', '0', '9', '0', '2'], ['0', '9', '0', '0', '0', '0', '0', '0', '5']]

"""
sudoku_file = open("input_sudoku_puzzle.txt", "r")
sudoku_table = [0]*9
for i in range(len(sudoku_table)):
	sudoku_table[i]  = sudoku_file.readline().rstrip('\n').split(',')



# Prints Sudoku in a nice, standard format

for sections_of_three in range(3):
	for row in range(3):
		for i in range(0+sections_of_three*3,3*(sections_of_three+1)):
			if i % 3 ==0 :
				print ""
				for z in range(0+(row*3),3*(row+1)):
					#print "\nrow is %s " % row
					#print "\ntimes run %s"  % z
					#print "\n i is %s" % i
					print "%s" % sudoku_table[i][z],

				print " ",
			else:
				for z in range(0+(row*3),3*(row+1)):
					#print "\nrow is %s " % row
					#print "\ntimes run %s"  % z
					#print "\n i is %s" % i
					print "%s" % sudoku_table[i][z],
				print " ",
	print ""

