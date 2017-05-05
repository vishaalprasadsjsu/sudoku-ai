# Agent that solves Sudoku puzzles




class Sudoku:
    def __init__(self):
        self.sudoku_table = [0]*9
        self.read_table()
        for i in range(0,len(self.sudoku_table)):
            for j in range(0,len(self.sudoku_table)):
                if self.sudoku_table[i][j] == "0":
                    
                    self.sudoku_table[i][j]+= self.get_possibilities(i,j,self.sudoku_table)

    def get_possibilities(self,i,j,board):
        possibilites = ""
        for potential_poss in range(1,10):
            # get first character of each location of section
            first_character_list = list()
            for x in range(0,9):
                first_character_list.append(board[i][x][0])
            # check section
            if str(potential_poss) not in first_character_list:
                # check row
                row = list()
                row_i_start = 3 * (i/3)
                row_j_start = 3 * (j/3)

                for row_i_iterator in range(row_i_start, row_i_start + 3): 
                    for row_j_iterator in range(row_j_start, row_j_start + 3): 
                        row.append(board[row_i_iterator][row_j_iterator][0])
    
                if str(potential_poss) not in row:
                    # check columns
                    column = list()
                    col_i_start = i%3;
                    col_j_start = j%3;

                    for col_i_iter in xrange(col_i_start, col_i_start + 7, 3):
                        for col_j_iter in xrange(col_j_start, col_j_start + 7, 3):
                            column.append(board[col_i_iter][col_j_iter][0])
            
                    if str(potential_poss) not in column:
                        possibilites+=str(potential_poss)
                  
                    
                
                
        
        return possibilites
        
    def read_table(self):
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
        self.sudoku_table = [0]*9
        for i in range(len(self.sudoku_table)):
       	    self.sudoku_table[i]  = sudoku_file.readline().rstrip('\n').split(',')
        
        
        
    # Prints Sudoku in a nice, standard format
    def print_table_with_possibilities(self):
            for sections_of_three in range(3):
           	    for row in range(3):
          		for i in range(0+sections_of_three*3,3*(sections_of_three+1)):
         			if i % 3 ==0 :
            				print ""

            				for z in range(0+(row*3),3*(row+1)):
           					#print "\nrow is %s " % row
           					#print "\ntimes run %s"  % z
           					#print "\n i is %s" % i
           					if self.sudoku_table[i][z][1:] != "":
           					    print "(%s: poss %9s)" % (self.sudoku_table[i][z][0], self.sudoku_table[i][z][1:]),
           					else:
                                                    print "(%s: %14s)" % (self.sudoku_table[i][z][0], ""),
            				print "            ",
         			else:
            				for z in range(0+(row*3),3*(row+1)):
           					#print "\nrow is %s " % row
           					#print "\ntimes run %s"  % z
           					#print "\n i is %s" % i
           					if self.sudoku_table[i][z][1:] != "":
           					    print "(%s: poss %9s)" % (self.sudoku_table[i][z][0], self.sudoku_table[i][z][1:]),
           					else:
                                                    print "(%s: %14s)" % (self.sudoku_table[i][z][0], ""),
            				print "            ",
           	    print ""
           	    print ""
           	    print ""
            



    def print_table(self):
            for sections_of_three in range(3):
           	    for row in range(3):
          		for i in range(0+sections_of_three*3,3*(sections_of_three+1)):
         			if i % 3 ==0 :
            				print ""
            				for z in range(0+(row*3),3*(row+1)):
           					#print "\nrow is %s " % row
           					#print "\ntimes run %s"  % z
           					#print "\n i is %s" % i
           					
           					print "%s" % self.sudoku_table[i][z][0],
           					
            				print " ",
         			else:
            				for z in range(0+(row*3),3*(row+1)):
           					#print "\nrow is %s " % row
           					#print "\ntimes run %s"  % z
           					#print "\n i is %s" % i
           					
           					print "%s" % self.sudoku_table[i][z][0],
           					
            				print " ",
           	    print ""
            
    # TO BE DONE
    def get_cells_with_allowed_num_poss(self):
        return

    # TO BE DONE
    def board_filled(self):
        return
        
    def solve(self,board):
        if self.board_filled():
            return True
        
        for i in range(1,10):
            allowed_possibilities = self.get_cells_with_allowed_num_poss()
        #REST OF CODE TO BE DONE


"""
Test
"""
s = Sudoku()
print s.sudoku_table[0]
print s.print_table()
print s.print_table_with_possibilities()
