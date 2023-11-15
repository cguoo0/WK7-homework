from logic import check_winner
#test None
test_board = [[None,"O","X"], ["O",None,"X"],["O","X","O"]]
winner = check_winner(test_board)
print(winner)

#test O
test_board = [["O","O","X"], ["O","X","X"],["O","X","O"]]
winner = check_winner(test_board)
print(winner)

#test X
test_board = [["O","X","O"], ["O","X","X"],["X","X","O"]]
winner = check_winner(test_board)
print(winner)
