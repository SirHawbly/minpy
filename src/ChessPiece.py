

PieceTypeNames = {
  'k': 'king',
  'q': 'queen',
  'b': 'bishop',
  'n': 'knight',
  'r': 'rook',
  'p': 'pawn',
  '.': 'blank',
  }

RowCoordNames = {
  '0': '0',
  '1': '1',
  '2': '2',
  '3': '3',
  '4': '4',
  '5': '5'
  }

ColCoordNames = {
  '0': 'a',
  '1': 'b',
  '2': 'c',
  '3': 'd',
  '4': 'e'
  }


class ChessPiece:
  """
  Piece Type for storing information on the different pieces on board
  """

  def __init__(self, piece_type, row_coord, col_coord, color) -> None:
    """
    :param piece_type:
    :param row_coord:
    :param col_coord:
    :param color:
    """
    self.piece_type = piece_type
    self.row_coord = row_coord
    self.col_coord = col_coord
    self.color = color

  @property
  def __str__(self) -> str:
    return ("[ "
            + self.piece_type + ', '
            + str(self.row_coord) + ', '
            + str(self.col_coord) + ', '
            + self.color + ' ]')


if __name__ == "__main__":
  test_piece = ChessPiece('k', 1, 2, 'black')
  print(test_piece)
