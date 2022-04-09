#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
Written by Albert Ong

Created: 2022.04.05
"""

import numpy as np
from itertools import cycle
from tile import Tile


class Board:
    
    def __init__(self):
        
        self.ROWS = 6
        self.COLUMNS = 7
        
        self.board = np.array([[Tile() for x in range(self.COLUMNS)] for y in range(self.ROWS)])
        
        self.player_cycle = cycle(["Player 1", "Player 2"])
        self.current_player = next(self.player_cycle)
        
    
    def check_win(self):
        
        row_wins = []
        
        for row in self.board:
            for num in range(4):    
                row_wins.append(row[num: num + 4])
        
        
        column_wins = []
        
        for column in self.board.T:
            
            for num in range(3):
                column_wins.append(column[num: num + 4])
        
        
        diagonal_wins = []
        
        for num in range(-2, 4):
            
            diagonal = self.board.diagonal(num)
            diag_len = len(diagonal)
            
            for x in range(0, diag_len - 3):
                
                diag_win = diagonal[x: x + 4]
                diagonal_wins.append(diag_win)
        
        
        flipped_board = np.fliplr(self.board)
        
        for index in range(-2, 4):
            
            flipped_diagonal = flipped_board.diagonal(index)
            diag_len = len(flipped_diagonal)
            
            for x in range(0, diag_len - 3):
                
                diag_win = flipped_diagonal[x: x + 4]
                diagonal_wins.append(diag_win)
        
        
        total_wins = row_wins + column_wins + diagonal_wins
        
        
        for win in total_wins:
            
            player1_win = all([tile.color == "red" for tile in win])
            player2_win = all([tile.color == "black" for tile in win])
            
            if player1_win or player2_win:
                return True
                
        return False
            
        
    
    def play(self):
        
        print("Welcome to Connect Four!")
        print(self.board)
        print()
        
        while True:
            
            try:
                column = int(input(self.current_player + " turn: "))
                
            except ValueError:
                print("Invalid input: value must be an integer\n")
                continue
            
            
            if column < 1 or column > 7:
                
                print("Invalid input: integer must be between 1 and 7\n")
                continue
            
            
            else:
                
                column -= 1
                
                board_column = self.board[:, column]
                
                column_full = all([tile.filled() for tile in board_column])
                
                if column_full:
                    print("Invalid input: column is full\n")
                    continue
                
                
                else:
                    
                    if self.current_player == "Player 1":
                        new_color = "red"
                    else:
                        new_color = "black"
                    
                    
                    for row in range(5, -1, -1):
                        
                        if not board_column[row].filled():
                            
                            self.board[row][column].color = new_color
                            break
                    
                    if self.check_win():
                        print("\n" + self.current_player + " wins!")
                        print(self.board)
                        
                        break
                        # ~ play_again = input("\nPlay again? (y/n): ")
                        
                        # ~ if play_again == "y":
                            # ~ self.__init__()
                            # ~ self.play()
                        # ~ else:
                            # ~ break
                
                print(self.board)
                print()
            
                self.current_player = next(self.player_cycle)


#=======================================================================


def main():
    
    game = Board()
    game.play()


if __name__ == "__main__":
    main()
    


