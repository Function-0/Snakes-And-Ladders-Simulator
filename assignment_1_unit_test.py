# Import required modules
import unittest
from salbLLfunctions import *

def salbLL2salb(LL_head):
    '''(SALBnode) -> SALboard
    Given a linked list head of a linked list representation of a snakes 
    and ladders board game, based on the SALBnode class, LL_head: Returns the 
    dictionary representation of the snakes and ladders board game, based on 
    the SALboard class.
    
    REQ: LL_head.next != NoneType
    '''
    # Holds the SDLs of the snakes and ladders board game
    SDLs = dict()
    # Holds the list representation of the board without its SDLs;
    # Include the head of the linked list at position 1
    board_with_no_SDLs = [None, LL_head]
    # Holds the number of squares the board game has; All boards have a default
    # size of 1
    num_squares = 1
    # State the initial node
    curr = LL_head
    # Go through each node of the linked list representation of the snakes
    # and ladders board game until we have looped around the entire board
    while ((curr != None) and (curr.next is not LL_head)):
        # Move on to the next node
        curr = curr.next
        # Increment 1 square to the total squares on the board
        num_squares += 1
        # Then add the node to the initial board we are creating
        board_with_no_SDLs.append(curr)
    # Holds the dictionary representation of all SDL found on the board
    SDLs = dict()
    # Go through each position of our list representation of the board
    # to extract any SDLs found on said board
    for node in board_with_no_SDLs[1:]:
        # If the node exists
        if (node.snadder != None):
            # Obtain the node's index
            node_index = board_with_no_SDLs.index(node)
            # Obtain the node's SDL value
            SDL_value = node.snadder            
            # Find the index position of the other snadder connection
            SDL_destination = board_with_no_SDLs.index(SDL_value)
            # And add this SDL to collection of the board's SDLs
            SDLs[node_index] = SDL_destination
    # Create the SALboard based on our given information
    board = SALboard(num_squares, SDLs)
    # Returns the dictionary representation of the snakes and ladders board
    # game
    return board

# class Test_salb2salbLL(unittest.TestCase):
    # pass
    # def test_1_1_square_board(self):
        # num_squares = 1
        # SDLs = dict()
        # expected = SALboard(num_squares, SDLs)
        # board = salb2salbLL(expected)
        # result = salbLL2salb(board)
        # message = "1 square on board"
        # self.assertEqual(result.numSquares, num_squares, message)
        # self.assertEqual(result.snadders, SDLs, message)
        
    # def test_2_3_square_board(self):
        # num_squares = 3
        # SDLs = dict()
        # expected = SALboard(num_squares, SDLs)
        # board = salb2salbLL(expected)
        # result = salbLL2salb(board)
        # message = "3 squares with no SDLs"
        # self.assertEqual(result.numSquares, num_squares, message)
        # self.assertEqual(result.snadders, SDLs, message)
        
    # def test_3_3_square_board(self):
        # num_squares = 3
        # SDLs = {1: 2}
        # expected = SALboard(num_squares, SDLs)
        # board = salb2salbLL(expected)
        # result = salbLL2salb(board)
        # message = "3 squares with 1 LL from {1:2} of SDL"
        # self.assertEqual(result.numSquares, num_squares, message)
        # self.assertEqual(result.snadders, SDLs, message)
        
    # def test_4_3_square_board(self):
        # num_squares = 3
        # SDLs = {2: 1}
        # expected = SALboard(num_squares, SDLs)
        # board = salb2salbLL(expected)
        # result = salbLL2salb(board)
        # message = "3 squares with 1 SL from {2:1} of SDL"
        # self.assertEqual(result.numSquares, num_squares, message)
        # self.assertEqual(result.snadders, SDLs, message)
        
    # def test_5_3_square_board(self):
        # num_squares = 3
        # SDLs = {1: 2, 2: 1}
        # expected = SALboard(num_squares, SDLs)
        # board = salb2salbLL(expected)
        # result = salbLL2salb(board)
        # message = "3 squares with 1 LL from {1:2} and 1 SL from {2:1} of SDL"
        # self.assertEqual(result.numSquares, num_squares, message)
        # self.assertEqual(result.snadders, SDLs, message)
        
    # def test_6_4_square_board(self):
        # num_squares = 4
        # SDLs = {2: 3}
        # expected = SALboard(num_squares, SDLs)
        # board = salb2salbLL(expected)
        # result = salbLL2salb(board)
        # message = "4 squares with 1 LL from {2:3} of SDL"
        # self.assertEqual(result.numSquares, num_squares, message)
        # self.assertEqual(result.snadders, SDLs, message)
        
    # def test_7_4_square_board(self):
        # num_squares = 4
        # SDLs = {3: 2}
        # expected = SALboard(num_squares, SDLs)
        # board = salb2salbLL(expected)
        # result = salbLL2salb(board)
        # message = "4 squares with 1 SL from {3:2} of SDL"
        # self.assertEqual(result.numSquares, num_squares, message)
        # self.assertEqual(result.snadders, SDLs, message)
        
    # def test_8_4_square_board(self):
        # num_squares = 4
        # SDLs = {2: 3, 3: 2}
        # expected = SALboard(num_squares, SDLs)
        # board = salb2salbLL(expected)
        # result = salbLL2salb(board)
        # message = "4 squares with 1 LL from {2:3} and 1 SL from {3:2} of SDL"
        # self.assertEqual(result.numSquares, num_squares, message)
        # self.assertEqual(result.snadders, SDLs, message)
        
    # def test_9_4_square_board(self):
        # num_squares = 4
        # SDLs = {1: 2, 2: 3}
        # expected = SALboard(num_squares, SDLs)
        # board = salb2salbLL(expected)
        # result = salbLL2salb(board)
        # message = "4 squares with 2 LL from {1:2} and {2:3} of SDL"
        # self.assertEqual(result.numSquares, num_squares, message)
        # self.assertEqual(result.snadders, SDLs, message)
        
    # def test_10_4_square_board(self):
        # num_squares = 4
        # SDLs = {3: 2, 2: 1}
        # expected = SALboard(num_squares, SDLs)
        # board = salb2salbLL(expected)
        # result = salbLL2salb(board)
        # message = "4 squares with 2 SL from {3:2} and {2:1} of SDL"
        # self.assertEqual(result.numSquares, num_squares, message)
        # self.assertEqual(result.snadders, SDLs, message)
        
    # def test_11_5_square_board(self):
        # num_squares = 5
        # SDLs = {2: 3, 3: 4}
        # expected = SALboard(num_squares, SDLs)
        # board = salb2salbLL(expected)
        # result = salbLL2salb(board)
        # message = "5 squares with 2 LL from {2:3} and {3:4} of SDL"
        # self.assertEqual(result.numSquares, num_squares, message)
        # self.assertEqual(result.snadders, SDLs, message)
        
    # def test_12_5_square_board(self):
        # num_squares = 5
        # SDLs = {4: 3, 3: 2}
        # expected = SALboard(num_squares, SDLs)
        # board = salb2salbLL(expected)
        # result = salbLL2salb(board)
        # message = "5 squares with 2 SL from {4:3} and {3:2} of SDL"
        # self.assertEqual(result.numSquares, num_squares, message)
        # self.assertEqual(result.snadders, SDLs, message)
        
    # def test_13_10_square_board(self):
        # num_squares = 10
        # SDLs = {1: 5, 4: 6, 6: 8, 7: 2, 9: 3}
        # expected = SALboard(num_squares, SDLs)
        # board = salb2salbLL(expected)
        # result = salbLL2salb(board)
        # message = ("10 squares with 2 LL from {1:5}, {4:6}, {6:8}, and 2 SL \
        # from {7:2}, {9:3}")
        # self.assertEqual(result.numSquares, num_squares, message)
        # self.assertEqual(result.snadders, SDLs, message)
    
    

# class Test_willfinish(unittest.TestCase):
    
    # def test_1_1_square_board(self):
        # num_squares = 1
        # SDLs = dict()
        # step_size = 1
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = True
        # result = willfinish(LLboard, step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("1 square with step size 1 => True \
                   # [steps_taken = 1]")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
        
    # def test_2_2_square_board(self):
        # num_squares = 2
        # SDLs = dict()
        # step_size = 1
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = True
        # result = willfinish(LLboard, step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("2 squares with step size 1 => True \
                   # [steps_taken = 1]")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_3_2_square_board(self):
        # num_squares = 2
        # SDLs = dict()
        # step_size = 3
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = True
        # result = willfinish(LLboard, step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("2 squares with step size 3 => True \
                   # [steps_taken = 1]")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_4_3_square_board(self):
        # num_squares = 3
        # SDLs = dict()
        # step_size = 2
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = True
        # result = willfinish(LLboard, step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("3 squares with step size 2 => True \
                   # [steps_taken = 2]")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_5_3_square_board(self):
        # num_squares = 3
        # SDLs = {1: 2}
        # step_size = 2
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = False
        # result = willfinish(LLboard, step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("3 squares with 1 LL from {1:2} of SDL with step size 2 \
                   # => False")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_6_3_square_board(self):
        # num_squares = 3
        # SDLs = {2: 1}
        # step_size = 1
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = False
        # result = willfinish(LLboard, step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("3 squares with 1 SL from {2:1} of SDL with step size 1 \
                   # => False")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_7_3_square_board(self):
        # num_squares = 3
        # SDLs = {1: 2, 2: 1}
        # step_size = 1
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = True
        # result = willfinish(LLboard, step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("3 squares with 1 LL from {1:2} and 1 SL from {2:1} \
                   # of SDL with step size 2 => True [steps_taken = 1]")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_8_4_square_board(self):
        # num_squares = 4
        # SDLs = {2: 3}
        # step_size = 3
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = False
        # result = willfinish(LLboard, step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("4 squares with 1 LL from {2:3} of SDL with step size 3 \
                   # => False")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_9_4_square_board(self):
        # num_squares = 4
        # SDLs = {3: 2}
        # step_size = 3
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = True
        # result = willfinish(LLboard, step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("4 squares with 1 SL from {3:2} of SDL with step size 3 \
                   # => True [steps_taken = 2]")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_10_4_square_board(self):
        # num_squares = 4
        # SDLs = {2: 3, 3: 2}
        # step_size = 2
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = True
        # result = willfinish(LLboard, step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("4 squares with 1 LL from {2:3} and 1 SL from {3:2} \
                   # of SDL with step size 2 => True [steps_taken = 3]")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_11_4_square_board(self):
        # num_squares = 4
        # SDLs = {1: 2, 2: 3}
        # step_size = 3
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = False
        # result = willfinish(LLboard, step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("4 squares with 2 LL from {1:2} and {2:3} \
                   # of SDL with step size 3 => False")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_12_4_square_board(self):
        # num_squares = 4
        # SDLs = {3: 2, 2: 1}
        # step_size = 3
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = True
        # result = willfinish(LLboard, step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("4 squares with 2 SL from {3:2} and {2:1} \
                   # of SDL with step size 3 => True [steps_taken = 2]")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_13_5_square_board(self):
        # num_squares = 5
        # SDLs = {2: 3, 3: 4}
        # step_size = 1
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = True
        # result = willfinish(LLboard, step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("5 squares with 2 LL from {2:3} and {3:4} \
                   # of SDL with step size 1 => True [steps_taken = 3]")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_14_5_square_board(self):
        # num_squares = 5
        # SDLs = {4: 3, 3: 2}
        # step_size = 4
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = True
        # result = willfinish(LLboard, step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("5 squares with 2 SL from {4:3} and {3:2} \
                   # of SDL with step size 4 => True [steps_taken = 3]")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_15_10_square_board(self):
        # num_squares = 10
        # SDLs = {1: 5, 4: 6, 6: 8, 7: 2, 9: 3}
        # step_size = 17
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = True
        # result = willfinish(LLboard, step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("10 squares with 3 LL from {1:5}, {4:6}, {6:8}, \
                   # and 2 SL from {7:2}, {9:3} with step size 17 => True \
                   # [steps_taken = 3]")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_16_10_square_board(self):
        # num_squares = 10
        # SDLs = {1: 5, 4: 6, 6: 8, 7: 2, 9: 3}
        # step_size = 6
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = False
        # result = willfinish(LLboard, step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("10 squares with 3 LL from {1:5}, {4:6}, {6:8}, \
                   # and 2 SL from {7:2}, {9:3} with step size 6 => False")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_17_10_square_board(self):
        # num_squares = 10
        # SDLs = {1: 5, 4: 6, 6: 8, 7: 2, 9: 3}
        # step_size = 4
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = True
        # result = willfinish(LLboard, step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("10 squares with 3 LL from {1:5}, {4:6}, {6:8}, \
                   # and 2 SL from {7:2}, {9:3} with step size 4 => True \
                   # [steps_taken = 1]")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_18_10_square_board(self):
        # num_squares = 10
        # SDLs = {1: 5, 4: 6, 6: 8, 7: 2, 9: 3}
        # step_size = 9
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = False
        # result = willfinish(LLboard, step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("10 squares with 3 LL from {1:5}, {4:6}, {6:8}, \
                   # and 2 SL from {7:2}, {9:3} with step size 9 => False")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_19_10_square_board(self):
        # num_squares = 10
        # SDLs = {1: 5, 4: 6, 6: 8, 7: 2, 9: 3}
        # step_size = 7
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = True
        # result = willfinish(LLboard, step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("10 squares with 3 LL from {1:5}, {4:6}, {6:8}, \
                   # and 2 SL from {7:2}, {9:3} with step size 7 => True \
                   # [steps_taken = 2]")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_20_10_square_board(self):
        # num_squares = 10
        # SDLs = {1: 5, 4: 6, 6: 8, 7: 2, 9: 3}
        # step_size = 3
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = False
        # result = willfinish(LLboard, step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("10 squares with 3 LL from {1:5}, {4:6}, {6:8}, \
                   # and 2 SL from {7:2}, {9:3} with step size 3 => False")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    

# class Test_whowins(unittest.TestCase):
    # def test_1_1_square_board(self):
        # num_squares = 1
        # SDLs = dict()
        # P1_step_size = 1
        # P2_step_size = 1
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = 1
        # result = whowins(LLboard, P1_step_size, P2_step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("1 square with P1 step size = 1, P2 step size = 1 \
                   # => P1 wins")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_2_2_square_board(self):
        # num_squares = 2
        # SDLs = dict()
        # P1_step_size = 1
        # P2_step_size = 1
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = 1
        # result = whowins(LLboard, P1_step_size, P2_step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("2 squares with P1 step size = 1, P2 step size = 1 \
                   # => P1 wins")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_3_4_square_board(self):
        # num_squares = 4
        # SDLs = dict()
        # P1_step_size = 1
        # P2_step_size = 2
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = 2
        # result = whowins(LLboard, P1_step_size, P2_step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("4 squares with P1 step size = 1, P2 step size = 2 \
                   # => P2 wins")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_4_10_square_board(self):
        # num_squares = 10
        # SDLs = {1: 5, 4: 6, 6: 8, 7: 2, 9: 3}
        # P1_step_size = 17
        # P2_step_size = 3
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = 1
        # result = whowins(LLboard, P1_step_size, P2_step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("10 squares with 3 LL from {1:5}, {4:6}, {6:8}, \
                   # and 2 SL from {7:2}, {9:3} with P1 step size = 17, \
                   # P2 step size = 3 => P1 wins")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_5_10_square_board(self):
        # num_squares = 10
        # SDLs = {1: 5, 4: 6, 6: 8, 7: 2, 9: 3}
        # P1_step_size = 6
        # P2_step_size = 4
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = 2
        # result = whowins(LLboard, P1_step_size, P2_step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("10 squares with 3 LL from {1:5}, {4:6}, {6:8}, \
                   # and 2 SL from {7:2}, {9:3} with P1 step size = 6, \
                   # P2 step size = 4 => P2 wins")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
    
    # def test_6_10_square_board(self):
        # num_squares = 10
        # SDLs = {1: 5, 4: 6, 6: 8, 7: 2, 9: 3}
        # P1_step_size = 3
        # P2_step_size = 6
        # board = SALboard(num_squares, SDLs)
        # LLboard = salb2salbLL(board)
        # expected = 2
        # result = whowins(LLboard, P1_step_size, P2_step_size)
        # revert_LLboard = salbLL2salb(LLboard)
        # message = ("10 squares with 3 LL from {1:5}, {4:6}, {6:8}, \
                   # and 2 SL from {7:2}, {9:3} with P1 step size = 3, \
                   # P2 step size = 6 => P2 wins")
        # self.assertEqual(result, expected, message)
        # self.assertEqual(board, revert_LLboard, message)
        

class Test_dualboard(unittest.TestCase):

    # def test_1_1_square_board(self):
        # orig_num_squares = 1
        # orig_SDLs = dict()
        # dual_num_squares = 1
        # dual_SDls = dict()
        # expected = SALboard(dual_num_squares, dual_SDls)
        # Board = SALboard(orig_num_squares, orig_SDLs)
        # LLboard = salb2salbLL(Board)
        # DualLLboard = dualboard(LLboard)
        # result = salbLL2salb(DualLLboard)
        # message = "1 square on board"
        # self.assertEqual(result.numSquares, expected.numSquares, message)
        # self.assertEqual(result.snadders, expected.snadders, message)
        
    # def test_2_3_square_board(self):
        # orig_num_squares = 3
        # orig_SDLs = dict()
        # dual_num_squares = 3
        # dual_SDls = dict()
        # expected = SALboard(dual_num_squares, dual_SDls)
        # Board = SALboard(orig_num_squares, orig_SDLs)
        # LLboard = salb2salbLL(Board)
        # DualLLboard = dualboard(LLboard)
        # result = salbLL2salb(DualLLboard)
        # message = "3 squares with no SDLs"
        # self.assertEqual(result.numSquares, expected.numSquares, message)
        # self.assertEqual(result.snadders, expected.snadders, message)
        
    # def test_3_3_square_board(self):
        # orig_num_squares = 3
        # orig_SDLs = {1: 2}
        # dual_num_squares = 3
        # dual_SDls = {2: 1}
        # expected = SALboard(dual_num_squares, dual_SDls)
        # Board = SALboard(orig_num_squares, orig_SDLs)
        # LLboard = salb2salbLL(Board)
        # DualLLboard = dualboard(LLboard)
        # result = salbLL2salb(DualLLboard)
        # message = "3 squares with 1 LL from {1:2} of SDL"
        # self.assertEqual(result.numSquares, expected.numSquares, message)
        # self.assertEqual(result.snadders, expected.snadders, message)
        
    # def test_4_3_square_board(self):
        # orig_num_squares = 3
        # orig_SDLs = {2: 1}
        # dual_num_squares = 3
        # dual_SDls = {1: 2}
        # expected = SALboard(dual_num_squares, dual_SDls)
        # Board = SALboard(orig_num_squares, orig_SDLs)
        # LLboard = salb2salbLL(Board)
        # DualLLboard = dualboard(LLboard)
        # result = salbLL2salb(DualLLboard)
        # message = "3 squares with 1 SL from {2:1} of SDL"
        # self.assertEqual(result.numSquares, expected.numSquares, message)
        # self.assertEqual(result.snadders, expected.snadders, message)
        
    # def test_5_3_square_board(self):
        # orig_num_squares = 3
        # orig_SDLs = {1: 2, 2: 1}
        # dual_num_squares = 3
        # dual_SDls = {2: 1, 1: 2}
        # expected = SALboard(dual_num_squares, dual_SDls)
        # Board = SALboard(orig_num_squares, orig_SDLs)
        # LLboard = salb2salbLL(Board)
        # DualLLboard = dualboard(LLboard)
        # result = salbLL2salb(DualLLboard)
        # message = "3 squares with 1 LL from {1:2} and 1 SL from {2:1} of SDL"
        # self.assertEqual(result.numSquares, expected.numSquares, message)
        # self.assertEqual(result.snadders, expected.snadders, message)
        
    # def test_6_4_square_board(self):
        # orig_num_squares = 4
        # orig_SDLs = {2: 3}
        # dual_num_squares = 4
        # dual_SDls = {3: 2}
        # expected = SALboard(dual_num_squares, dual_SDls)
        # Board = SALboard(orig_num_squares, orig_SDLs)
        # LLboard = salb2salbLL(Board)
        # DualLLboard = dualboard(LLboard)
        # result = salbLL2salb(DualLLboard)
        # message = "4 squares with 1 LL from {2:3} of SDL"
        # self.assertEqual(result.numSquares, expected.numSquares, message)
        # self.assertEqual(result.snadders, expected.snadders, message)
        
    # def test_7_4_square_board(self):
        # orig_num_squares = 4
        # orig_SDLs = {3: 2}
        # dual_num_squares = 4
        # dual_SDls = {2: 3}
        # expected = SALboard(dual_num_squares, dual_SDls)
        # Board = SALboard(orig_num_squares, orig_SDLs)
        # LLboard = salb2salbLL(Board)
        # DualLLboard = dualboard(LLboard)
        # result = salbLL2salb(DualLLboard)
        # message = "4 squares with 1 SL from {3:2} of SDL"
        # self.assertEqual(result.numSquares, expected.numSquares, message)
        # self.assertEqual(result.snadders, expected.snadders, message)
        
    # def test_8_4_square_board(self):
        # orig_num_squares = 4
        # orig_SDLs = {2: 3, 3: 2}
        # dual_num_squares = 4
        # dual_SDls = {3: 2, 2: 3}
        # expected = SALboard(dual_num_squares, dual_SDls)
        # Board = SALboard(orig_num_squares, orig_SDLs)
        # LLboard = salb2salbLL(Board)
        # DualLLboard = dualboard(LLboard)
        # result = salbLL2salb(DualLLboard)
        # message = "4 squares with 1 LL from {2:3} and 1 SL from {3:2} of SDL"
        # self.assertEqual(result.numSquares, expected.numSquares, message)
        # self.assertEqual(result.snadders, expected.snadders, message)
        
    # def test_9_4_square_board(self):
        # orig_num_squares = 4
        # orig_SDLs = {1: 2, 2: 3}
        # dual_num_squares = 4
        # dual_SDls = {2: 1, 3: 2}
        # expected = SALboard(dual_num_squares, dual_SDls)
        # Board = SALboard(orig_num_squares, orig_SDLs)
        # LLboard = salb2salbLL(Board)
        # DualLLboard = dualboard(LLboard)
        # result = salbLL2salb(DualLLboard)
        # message = "4 squares with 2 LL from {1:2} and {2:3} of SDL"
        # self.assertEqual(result.numSquares, expected.numSquares, message)
        # self.assertEqual(result.snadders, expected.snadders, message)
        
    # def test_10_4_square_board(self):
        # orig_num_squares = 4
        # orig_SDLs = {3: 2, 2: 1}
        # dual_num_squares = 4
        # dual_SDls = {2: 3, 1: 2}
        # expected = SALboard(dual_num_squares, dual_SDls)
        # Board = SALboard(orig_num_squares, orig_SDLs)
        # LLboard = salb2salbLL(Board)
        # DualLLboard = dualboard(LLboard)
        # result = salbLL2salb(DualLLboard)
        # message = "4 squares with 2 SL from {3:2} and {2:1} of SDL"
        # self.assertEqual(result.numSquares, expected.numSquares, message)
        # self.assertEqual(result.snadders, expected.snadders, message)
        
    # def test_11_5_square_board(self):
        # orig_num_squares = 5
        # orig_SDLs = {2: 3, 3: 4}
        # dual_num_squares = 5
        # dual_SDls = {3: 2, 4: 3}
        # expected = SALboard(dual_num_squares, dual_SDls)
        # Board = SALboard(orig_num_squares, orig_SDLs)
        # LLboard = salb2salbLL(Board)
        # DualLLboard = dualboard(LLboard)
        # result = salbLL2salb(DualLLboard)
        # message = "5 squares with 2 LL from {2:3} and {3:4} of SDL"
        # self.assertEqual(result.numSquares, expected.numSquares, message)
        # self.assertEqual(result.snadders, expected.snadders, message)
        
    # def test_12_5_square_board(self):
        # orig_num_squares = 5
        # orig_SDLs = {4: 3, 3: 2}
        # dual_num_squares = 5
        # dual_SDls = {3: 4, 2: 3}
        # expected = SALboard(dual_num_squares, dual_SDls)
        # Board = SALboard(orig_num_squares, orig_SDLs)
        # LLboard = salb2salbLL(Board)
        # DualLLboard = dualboard(LLboard)
        # result = salbLL2salb(DualLLboard)
        # message = "5 squares with 2 SL from {4:3} and {3:2} of SDL"
        # self.assertEqual(result.numSquares, expected.numSquares, message)
        # self.assertEqual(result.snadders, expected.snadders, message)
        
    def test_13_10_square_board(self):
        orig_num_squares = 10
        orig_SDLs = {1: 5, 4: 6, 6: 8, 7: 2, 9: 3}
        dual_num_squares = 10
        dual_SDls = {5: 1, 6: 4, 8: 6, 2: 7, 3: 9}
        expected = SALboard(dual_num_squares, dual_SDls)
        Board = SALboard(orig_num_squares, orig_SDLs)
        LLboard = salb2salbLL(Board)
        DualLLboard = dualboard(LLboard)
        result = salbLL2salb(DualLLboard)
        message = ("10 squares with 2 LL from {1:5}, {4:6}, {6:8}, and 2 SL \
        from {7:2}, {9:3}")
        self.assertEqual(result.numSquares, expected.numSquares, message)
        self.assertEqual(result.snadders, expected.snadders, message)


if (__name__ == "__main__"):
    unittest.main(exit=False)
 