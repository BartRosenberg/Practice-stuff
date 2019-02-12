import itertools


def win(current_game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # Poniżej są podane warunki wygranej

    # Horizontal
    for row in game:
        print(row)
        if all_same(row):
            print(f"Player {row[0]} wins horizontally!")
            return True

    # Diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} wins diagonally (/)!")
        return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} wins diagonally (\\)!")
        return True

    # Vertical
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if all_same(check):
            print(f"Player {check[0]} wins vertically (|)!")
            return True

    return False


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupied, choose another")
            return game_map, False
        print("   A  B  C")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True

    except IndexError as e:
        print("Error: Make sure you input 0, 1 or 2 c:")
        return game_map, False

    except Exception as e:
        print("Something went very wrong!", e)
        return game_map, False


play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won: bool = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        column_choice = int(input("What column do you want to play? (0, 1 , 2): "))
        row_choice = int(input("What row do you want to play? (0, 1 , 2): "))
        game, _ = game_board(game, current_player, row_choice, column_choice)
        print(f"Current Player: {current_player}")
        if win(game):
            game_won = True

    while not game_won:
        column_choice = int(input("What column do you want to play? (0, 1 , 2): "))
        row_choice = int(input("What row do you want to play? (0, 1 , 2): "))
        game, played = game_board(game, current_player, row_choice, column_choice)
        if game:
            played = True

    if win(game):
        game_won = True
        again = input("Congraturation, the winner is you! Wanna play again? (y/n) ")
        if again.lower() == "y":
            print("Restarting the game")
        elif again.lower() == "n":
            print("Buh bye")
            play = False
        else:
            print("Invalid answer, you are terminated. Baby la vista, hasta.")
            play = False
