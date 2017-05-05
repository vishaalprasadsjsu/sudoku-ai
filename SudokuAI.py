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
                if j<3:
                     if i<3:
                         for k in range(0,3):
                            row.append(board[k][0][0])
                            row.append(board[k][1][0])                
                            row.append(board[k][2][0])  
                     elif i>=3 and i <6:
                         for k in range(3,6):
                            row.append(board[k][0][0])
                            row.append(board[k][1][0])                
                            row.append(board[k][2][0])   
                     elif i>=6:
                         for k in range(6,9):
                            row.append(board[k][0][0])
                            row.append(board[k][1][0])                
                            row.append(board[k][2][0])                            
                            
                elif j>=3 and j<6:
                     if i<3:
                         for k in range(0,3):
                            row.append(board[k][3][0])
                            row.append(board[k][4][0])                
                            row.append(board[k][5][0])                
                     elif i>=3 and i <6:
                         for k in range(3,6):
                            row.append(board[k][3][0])
                            row.append(board[k][4][0])                
                            row.append(board[k][5][0])   
                     elif i>=6:
                         for k in range(6,9):
                            row.append(board[k][3][0])
                            row.append(board[k][4][0])                
                            row.append(board[k][5][0])                            
                elif j>=6:
                     if i<3:
                         for k in range(0,3):
                            row.append(board[k][6][0])
                            row.append(board[k][7][0])                
                            row.append(board[k][8][0])                
                     elif i>=3 and i <6:
                         for k in range(3,6):
                            row.append(board[k][6][0])
                            row.append(board[k][7][0])                
                            row.append(board[k][8][0])   
                     elif i>=6:
                         for k in range(6,9):
                            row.append(board[k][6][0])
                            row.append(board[k][7][0])                
                            row.append(board[k][8][0])              
                if str(potential_poss) not in row:
                    # check columns
                    column = list()
                    if j%3==0:
                        if i%3 ==0:
                            for k in xrange(0,7,3):
                                column.append(board[k][0][0])
                                column.append(board[k][3][0])                
                                column.append(board[k][6][0])  
                        elif i==1 or i==4 or i==7:
                            for k in xrange(1,8,3):
                                column.append(board[k][0][0])
                                column.append(board[k][3][0])                
                                column.append(board[k][6][0])   
                        elif i==2 or i==5 or i==8:
                            for k in xrange(2,9,3):
                                column.append(board[k][0][0])
                                column.append(board[k][3][0])                
                                column.append(board[k][6][0])                            
                                
                    elif j==1 or j==4 or j==7:
                        if i%3 ==0:
                            for k in xrange(0,7,3):
                                column.append(board[k][1][0])
                                column.append(board[k][4][0])                
                                column.append(board[k][7][0])  
                        elif i==1 or i==4 or i==7:
                            for k in xrange(1,8,3):
                                column.append(board[k][1][0])
                                column.append(board[k][4][0])                
                                column.append(board[k][7][0])   
                        elif i==2 or i==5 or i==8:
                            for k in xrange(2,9,3):
                                column.append(board[k][1][0])
                                column.append(board[k][4][0])                
                                column.append(board[k][7][0])                             
                    elif j==2 or j==5 or j==8:
                        if i%3 ==0:
                            for k in xrange(0,7,3):
                                column.append(board[k][2][0])
                                column.append(board[k][5][0])                
                                column.append(board[k][8][0])  
                        elif i==1 or i==4 or i==7:
                            for k in xrange(1,8,3):
                                column.append(board[k][2][0])
                                column.append(board[k][5][0])                
                                column.append(board[k][8][0])   
                        elif i==2 or i==5 or i==8:
                            for k in xrange(2,9,3):
                                column.append(board[k][2][0])
                                column.append(board[k][5][0])                
                                column.append(board[k][8][0])             
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

    #Returns a boolean depending upon if each cell has a single possibility
    def board_filled(self):
        for i in range(9):
            for j in range(9):
                if len(self.sudoku_table[i][j]) > 1:
                    return False
        return True
        
    # TO BE DONE
    def place_cell_in_board(self,section, position, board):
        return
        
    # TO BE DONE
    def violation_occured(self,section, position, board):
        return
    
    # TO BE DONE
    def remark_board(self, section, position, board):
        return
    
    def solve(self,board):
        if self.board_filled():
            return True
        
        for i in range(1,10):
            allowed_possibilities = self.get_cells_with_allowed_num_poss(i, board)
            for cell in allowed_possibilities:
                for charPos in range(1,len(cell[2])):
                    # cell[2] should contain possibilites, starting for loop at 1 to skip 0 value
                    newBoard = self.place_poss_in_board(cell[2][charPos],cell[0], cell[1], board)
                    if not self.violation_occured(cell[0],cell[1], newBoard):
                        self.remark_board(cell[0],cell[1],newBoard)
                        if self.solve(newBoard):
                            return True


        return False 
       
"""
Test
"""
s = Sudoku()

s.print_table()
s.print_table_with_possibilities()