from typing import Protocol, Tuple, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from player import Player


class BoardProtocol(Protocol):

    def print_board(self) -> None: ...

    def play(self, player: "Player", pos: Tuple[int, int]) -> None: ...

    def winner(self, *, player: "Player") -> Optional["Player"]: ...

    def empty_position(self) -> bool: ...


class Board(BoardProtocol):

    def __init__(self, *, size: int = 3, players: Tuple["Player"]) -> None:
        self.size = size
        self.board = [["_" for _ in range(size)] for _ in range(size)]
        self._winner: "Player" | None = None
        self._remaining_posistions = size * size
        self.players = players

    def play(self, player: "Player", pos: Tuple[int, int]) -> None:
        x, y = pos
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            raise ValueError("Position out of bounds")

        if self.board[x][y] != "_":
            raise Exception("Invalid Move: Position already taken")

        self.board[x][y] = player.piece().value
        self._remaining_posistions -= 1
        self.winner(player=player)

    def print_board(self) -> None:

        for irx, row in enumerate(self.board):
            for icx, col in enumerate(row):
                print("   " if col == "_" else " " + col + " ", end="")
                if icx != self.size - 1:
                    print(end="|")
            if irx != self.size - 1:
                print("\n--", end="")
                print("---" * self.size)
        print()

    def winner(self, *, player: "Player"):
        if self._winner is not None:
            return self._winner

        # check diagonally
        for i in range(self.size):
            if self.board[i][i] != player.piece().value:
                break
            if i == self.size - 1:
                self._winner = player
                return player

        # check anti-diagonally
        for i in range(self.size):
            if self.board[i][self.size - 1 - i] != player.piece().value:
                break
            if i == self.size - 1:
                self._winner = player
                return player

        # check horizontally
        for row in self.board:
            if row.count(player.piece().value) == self.size:
                self._winner = player
                return player

        # check vertically
        for col in range(self.size):
            if [row[col] for row in self.board].count(
                player.piece().value
            ) == self.size:
                self._winner = player
                return player

        return None

    def empty_position(self) -> bool:

        if self._remaining_posistions == 0:
            return False
        return True
