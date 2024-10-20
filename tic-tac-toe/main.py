from board import Board
from player import Player, PlayerPiece


def main():

    player1 = Player(PlayerPiece.X)
    player2 = Player(PlayerPiece.O)

    players = (player1, player2)

    board = Board(size=3, players=players)

    print("player1: ", player1.piece().value)
    print("player2: ", player2.piece().value)


    board.print_board()

    turn = 0
    while board.empty_position():
        
        player = players[turn]

        pos = tuple(
            map(int, input(f"{turn} chance,Choose Position: ").strip().split(", "))
        )

        player.move(board, pos)

        board.print_board()
        if board.winner(player=player):
            print("Winner: ", player)
            break

        turn = (turn + 1) % len(players)


if __name__ == "__main__":
    main()
