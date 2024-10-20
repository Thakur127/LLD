from enum import Enum
from typing import Protocol, Tuple
from board import Board


class PlayerPiece(Enum):
    X = "X"
    O = "O"  # noqa: E741


class PlayerProtocol(Protocol):

    def move(self, board: Board, pos: Tuple[int, int]): ...

    def piece(self) -> PlayerPiece: ...


class Player(PlayerProtocol):

    def __init__(self, piece: PlayerPiece) -> None:
        self._piece = piece

    def move(self, board: Board, pos: Tuple[int, int]) -> None:
        board.play(self, pos)

    def piece(self):
        return self._piece

    def __repr__(self) -> str:
        return "Player(piece={})".format(self._piece)
