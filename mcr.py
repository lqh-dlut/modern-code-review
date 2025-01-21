def print_board(game):
    
    print("  1 2 3")
    for i, row in enumerate(game):
        print(f"{i + 1} {' '.join(row)}")

def is_win(game):
    
    for row in game:
        if row[0] == row[1] == row[2] and row[0] in ['X', 'O']:
            return True

    
    for col in range(3):
        if game[0][col] == game[1][col] == game[2][col] and game[0][col] in ['X', 'O']:
            return True

    
    if game[0][0] == game[1][1] == game[2][2] and game[0][0] in ['X', 'O']:
        return True
    if game[0][2] == game[1][1] == game[2][0] and game[0][2] in ['X', 'O']:
        return True

    return False

def main():
    game = [[' ' for _ in range(3)] for _ in range(3)]  
    player1 = 'X'
    player2 = 'O'
    turn = False  

    print("X = Player 1")
    print("O = Player 2")
    print_board(game)  

    for n in range(9):
        turn = not turn  
        player = player1 if not turn else player2
        print(f"Player {player}: ", end="")
        print("Which cell to mark? i:[1..3], j:[1..3]: ")
        i, j = map(int, input().split())
        i -= 1
        j -= 1

        
        if i < 0 or i >= 3 or j < 0 or j >= 3 or game[i][j] != ' ':
            print("Invalid move! Try again.")
            turn = not turn  
            continue

        game[i][j] = player
        print_board(game)  

        if is_win(game):
            print(f"Player {player} wins!")
            break

    else:  
        print("It's a tie!")

if __name__ == "__main__":
    main()
//test test test
//get the first response
