"""
# Copyright Nick Cheng, Ibrahim Jomaa, 2017
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSCA48, Winter 2017
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

from salboard import SALboard
from salbnode import SALBnode

# Add your functions here.

# Function used for docstring examples


def salbLL2salb(LL_head):
    '''(SALBnode) -> SALboard
    Given a linked list head of a linked list representation of a snakes
    and ladders board game, based on the SALBnode class, LL_head: Returns the
    dictionary representation of the snakes and ladders board game, based on
    the SALboard class.

    REQ: LL_head.next != NoneType

    >>> num_squares = 10
    >>> SDLs = {1: 5, 4: 6, 6: 8, 7: 2, 9: 3}
    >>> expected = SALboard(num_squares, SDLs)
    >>> board = salb2salbLL(expected)
    >>> result = salbLL2salb(board)
    >>> result.numSquares == num_squares
    True
    >>> result.snadders == SDLs
    True
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
    while ((curr is not None) and (curr.next is not LL_head)):
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
        if (node.snadder is not None):
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


def salb2salbLL(salb):
    '''(SALboard) -> SALBnode
    Given a dictionary representation of the snakes and ladders board game,
    salb: Returns the head of a linked list representation of said board game.
    REQ: Number of squares within salb's board game >= 1
    REQ: There exists unique snadders within salb's board game such that:
         1. Any square has a max of 1 source and 1 destination snadder links.
         2. The last square on the board has no snadder links.

    >>> num_squares = 10
    >>> SDLs = {1: 5, 4: 6, 6: 8, 7: 2, 9: 3}
    >>> expected = SALboard(num_squares, SDLs)
    >>> board = salb2salbLL(expected)
    >>> result = salbLL2salb(board)
    >>> result.numSquares == num_squares
    True
    >>> result.snadders == SDLs
    True

    >>> num_squares = 1
    >>> SDLs = dict()
    >>> expected = SALboard(num_squares, SDLs)
    >>> board = salb2salbLL(expected)
    >>> result = salbLL2salb(board)
    >>> result.numSquares == num_squares
    True
    >>> result.snadders == SDLs
    True

    >>> num_squares = 5
    >>> SDLs = {2: 3, 3: 4}
    >>> expected = SALboard(num_squares, SDLs)
    >>> board = salb2salbLL(expected)
    >>> result = salbLL2salb(board)
    >>> result.numSquares == num_squares
    True
    >>> result.snadders == SDLs
    True
    '''
    # NOTE: All references to "node" is synonymous with "square"
    # Obtain the number of squares on the board
    num_of_squares = salb.numSquares
    # Obtain the snadders of the board
    snadder_links = salb.snadders
    # Create the last square of the board; denoted by a node
    board_tail_reference = SALBnode()
    # If the board contains more than 1 square
    if (num_of_squares > 1):
        # Create another reference to the last square
        board_tail = board_tail_reference
        # Keeps the positions of all the squares on the board; We add the
        # last square first
        node_positions = [board_tail_reference]
        # Create the rest of the board's squares with a linked list
        for square in range(num_of_squares - 1):
            # Add a node to the head of the linked list
            new_node = SALBnode(next=board_tail)
            # Update the tail's position in the linked list
            board_tail = new_node
            # Then add the node to our regular list to store its position
            node_positions.append(new_node)
        # Form the linked list to a circular linked list
        board_tail_reference.next = new_node
        # Add None to the end of the position list...
        node_positions.append(None)
        # ...So that when we reverse the list it forces the index to move up
        # by 1
        # Note: Reversing the list orders the linked list, starting at our
        # designated linked list head at index 1.
        node_positions.reverse()
        # Go through each snadder that the board has
        for snadder_source in snadder_links:
            # Add the destination link to the node's snadder data
            node_positions[snadder_source].snadder = (
                node_positions[snadder_links[snadder_source]])
    # Else, we have a 1 square board
    else:
        # We create a circular list with the one node
        board_tail_reference.next = board_tail_reference
        new_node = board_tail_reference
    # Obtain a reference to the head of the linked list
    head = new_node
    # Returns the head of the circular linked list representing the board
    return head


def willfinish(first, stepsize, is_returning_turns_taken=False):
    '''(SALBnode, int[, bool]) -> (bool or [int])
    Given the head of a linked list representation of a snakes and ladders
    board game, first; and the step size for a player, stepsize: Returns
    True if the player will ever land on the last square of the board with
    said step size.
    NOTE: If is_returning_turns_taken == True:
          1. If player can land on the last square, instead return the number
             of steps taken by said player to reach the end square.
          2. If player cannot land on the last square, instead return
            -1.
    REQ: stepsize >= 1
    REQ: Number of squares within first's board game >= 1
    REQ: There exists unique snadders within first's board game such that:
         1. Any square has a max of 1 source and 1 destination snadder links.
         2. The last square on the board has no snadder links.

    >>> num_squares = 10
    >>> SDLs = {1: 5, 4: 6, 6: 8, 7: 2, 9: 3}
    >>> step_size = 17
    >>> board = SALboard(num_squares, SDLs)
    >>> LLboard = salb2salbLL(board)
    >>> expected = True
    >>> result = willfinish(LLboard, step_size)
    >>> revert_LLboard = salbLL2salb(LLboard)
    >>> result == expected
    True
    >>> board == revert_LLboard
    True

    >>> num_squares = 10
    >>> SDLs = {1: 5, 4: 6, 6: 8, 7: 2, 9: 3}
    >>> step_size = 6
    >>> board = SALboard(num_squares, SDLs)
    >>> LLboard = salb2salbLL(board)
    >>> expected = False
    >>> result = willfinish(LLboard, step_size)
    >>> revert_LLboard = salbLL2salb(LLboard)
    >>> result == expected
    True
    >>> board == revert_LLboard
    True

    >>> num_squares = 10
    >>> SDLs = {1: 5, 4: 6, 6: 8, 7: 2, 9: 3}
    >>> step_size = 4
    >>> board = SALboard(num_squares, SDLs)
    >>> LLboard = salb2salbLL(board)
    >>> expected = True
    >>> result = willfinish(LLboard, step_size)
    >>> revert_LLboard = salbLL2salb(LLboard)
    >>> result == expected
    True
    >>> board == revert_LLboard
    True
    '''
    # NOTE: All references to "node" is synonymous with "square"
    # Keyword used to refer to a snadder that has already been used
    keyword = 5
    # Keeps track of the number of snadders used by the player
    snadders_used = 0
    # Keeps track of the number of turn the player takes
    turns_taken = 0
    # States if the player is in an infinite loop or not
    is_player_in_infinite_loop = False
    # Represents the player
    player_reference = first
    # Simulate the player playing the snakes and ladders board game
    while ((player_reference.next is not first) and
           (not is_player_in_infinite_loop)):
        # If its the player's first turn
        if (turns_taken == 0):
            # Move the player one node less than there step size
            for step in range(stepsize - 1):
                player_reference = player_reference.next
        # Else, Move the player to the next node based on their step size
        else:
            for step in range(stepsize):
                player_reference = player_reference.next
        # Increment the number of turns taken
        turns_taken += 1
        # If the node's snadder is not referencing to None, and the node's
        # snadder's snadder is not referencing to the keyword
        if ((player_reference.snadder is not None) and
            (player_reference.snadder.snadder != keyword)):
            # Create a new node with its snadder value referencing the keyword
            dummy_node = SALBnode(snadder=keyword)
            # Connect the new node to the current node's snadder value
            dummy_node.next = player_reference.snadder
            # Connect the current node's snadder reference to the new node
            player_reference.snadder = dummy_node
            # Transfer the player along the snadder link
            player_reference = player_reference.snadder.next
            # Increment the snadder usage
            snadders_used += 1
        # Else, if the node's snadder is not referencing to None, and the
        # node's snadder's snadder is referencing the keyword
        elif ((player_reference.snadder is not None) and
              (player_reference.snadder.snadder == keyword)):
            # We can conclude that the player is visiting this node a second
            # time, inferring that they are stuck in an infinite loop.
            # Therefore we must indicate this fact
            is_player_in_infinite_loop = True
            # And void the turns taken counter
            turns_taken = -1
    # Since we altered the original linked list, we must revert our changes.
    # Starting from node one, we go through the linked list based on the
    # player's step size.
    # Keeps track of where we are in the linked list
    corrector_reference = first
    # Indicates that it is the first turn
    is_first_turn = True
    while (snadders_used):
        # If its the first turn
        if (is_first_turn):
            # Move the player one node less than there step size
            for step in range(stepsize - 1):
                corrector_reference = corrector_reference.next
            # Then remove this if statement branch
            is_first_turn = False
        # Else, Move the player to the next node based on their step size
        else:
            for step in range(stepsize):
                corrector_reference = corrector_reference.next
        # If the node's snadder is not referencing to None, and the node's
        # snadder's snadder is referencing the keyword
        if ((corrector_reference.snadder is not None) and
            (corrector_reference.snadder.snadder == keyword)):
            # Connect the current node's snadder reference to the node that
            # the node's snadder is pointing to
            corrector_reference.snadder = corrector_reference.snadder.next
            # Transfer the corrector along the snadder link
            corrector_reference = corrector_reference.snadder
            # Then indicate that a snadder has been corrected
            snadders_used -= 1
    # Holds the return value
    result = True and (not is_player_in_infinite_loop)
    # If we are to return the alternate return value
    if (is_returning_turns_taken):
        # Change the return value accordingly
        result = turns_taken
    # Returns whether or not the player can land on the last square;
    # [OR] the number of turns taken by the player until they landed on the
    # last square;
    # [OR] Nonetype;
    # Based on the optional parameter is_returning_turns_taken
    return result


def whowins(first, step1, step2):
    '''(SALBnode, int, int) -> int
    Given the head of a linked list representation of a snakes and ladders
    board game, first; and the step sizes for a player one and two,
    step1, step2: Returns 1 if player one wins the game, or 2 if player two
    wins the game, based on each player's step size respectively.
    REQ: stepsize >= 1
    REQ: Number of squares within first's board game >= 1
    REQ: There exists unique snadders within first's board game such that:
         1. Any square has a max of 1 source and 1 destination snadder links.
         2. The last square on the board has no snadder links.

    >>> num_squares = 10
    >>> SDLs = {1: 5, 4: 6, 6: 8, 7: 2, 9: 3}
    >>> P1_step_size = 3
    >>> P2_step_size = 6
    >>> board = SALboard(num_squares, SDLs)
    >>> LLboard = salb2salbLL(board)
    >>> expected = 2
    >>> result = whowins(LLboard, P1_step_size, P2_step_size)
    >>> revert_LLboard = salbLL2salb(LLboard)
    >>> result == expected
    True
    >>> board == revert_LLboard
    True

    >>> num_squares = 10
    >>> SDLs = {1: 5, 4: 6, 6: 8, 7: 2, 9: 3}
    >>> P1_step_size = 6
    >>> P2_step_size = 4
    >>> board = SALboard(num_squares, SDLs)
    >>> LLboard = salb2salbLL(board)
    >>> expected = 2
    >>> result = whowins(LLboard, P1_step_size, P2_step_size)
    >>> revert_LLboard = salbLL2salb(LLboard)
    >>> result == expected
    True
    >>> board == revert_LLboard
    True

    >>> num_squares = 10
    >>> SDLs = {1: 5, 4: 6, 6: 8, 7: 2, 9: 3}
    >>> P1_step_size = 17
    >>> P2_step_size = 3
    >>> board = SALboard(num_squares, SDLs)
    >>> LLboard = salb2salbLL(board)
    >>> expected = 1
    >>> result = whowins(LLboard, P1_step_size, P2_step_size)
    >>> revert_LLboard = salbLL2salb(LLboard)
    >>> result == expected
    True
    >>> board == revert_LLboard
    True
    '''
    # Check if player one can land on the last square
    turns_req_for_p1 = willfinish(first, step1, is_returning_turns_taken=True)
    # Check if player two can land on the last square
    turns_req_for_p2 = willfinish(first, step2, is_returning_turns_taken=True)
    # If player one have a negative turn count or if player two won in less
    # turns than player one and if player two's turn count is not negative
    if ((turns_req_for_p1 < 0) or
        ((turns_req_for_p2 < turns_req_for_p1) and
         (turns_req_for_p2 > 0))):
        # Then player 2 won
        winner = 2
    # Else, player 1 won
    else:
        winner = 1
    # Returns 1 if player one won, or 2 if player two won
    return winner


def dualboard(first):
    '''(SALBnode) -> SALBnode
    Given the head of a linked list representation of a snakes and ladders
    board game, first: Returns the head of a linked list
    representation of the snakes and ladders board game that matches the
    inputted linked list representation, such that all the snadder links
    are reversed.
    REQ: Number of squares within first's board game >= 1
    REQ: There exists unique snadders within first's board game such that:
         1. Any square has a max of 1 source and 1 destination snadder links.
         2. The last square on the board has no snadder links.

    >>> orig_num_squares = 10
    >>> orig_SDLs = {1: 5, 4: 6, 6: 8, 7: 2, 9: 3}
    >>> dual_num_squares = 10
    >>> dual_SDls = {5: 1, 6: 4, 8: 6, 2: 7, 3: 9}
    >>> expected = SALboard(dual_num_squares, dual_SDls)
    >>> Board = SALboard(orig_num_squares, orig_SDLs)
    >>> LLboard = salb2salbLL(Board)
    >>> DualLLboard = dualboard(LLboard)
    >>> result = salbLL2salb(DualLLboard)
    >>> result.numSquares == expected.numSquares
    True
    >>> result.snadders == expected.snadders
    True

    >>> orig_num_squares = 5
    >>> orig_SDLs = {4: 3, 3: 2}
    >>> dual_num_squares = 5
    >>> dual_SDls = {3: 4, 2: 3}
    >>> expected = SALboard(dual_num_squares, dual_SDls)
    >>> Board = SALboard(orig_num_squares, orig_SDLs)
    >>> LLboard = salb2salbLL(Board)
    >>> DualLLboard = dualboard(LLboard)
    >>> result = salbLL2salb(DualLLboard)
    >>> result.numSquares == expected.numSquares
    True
    >>> result.snadders == expected.snadders
    True

    >>> orig_num_squares = 3
    >>> orig_SDLs = dict()
    >>> dual_num_squares = 3
    >>> dual_SDls = dict()
    >>> expected = SALboard(dual_num_squares, dual_SDls)
    >>> Board = SALboard(orig_num_squares, orig_SDLs)
    >>> LLboard = salb2salbLL(Board)
    >>> DualLLboard = dualboard(LLboard)
    >>> result = salbLL2salb(DualLLboard)
    >>> result.numSquares == expected.numSquares
    True
    >>> result.snadders == expected.snadders
    True
    '''
    # NOTE: All references to "node" is synonymous with "square"

    
    