
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
  0: '0',
  1: '1',
  2: '2',
  3: '3',
  4: '4',
  5: '5'
  }

ColCoordNames = {
  0: 'a',
  1: 'b',
  2: 'c',
  3: 'd',
  4: 'e'
  }

ColorNames = {
  'b': 'black',
  'w': 'white'
}


class ChessPiece:
  """
  Piece Type for storing information on the different pieces on board
  """

  def __init__(self, piece_type, row_coord, col_coord, color) -> None:
    """
    :param piece_type: ('k', 'q', 'b', 'n', 'r', 'p')
    :param row_coord: (0, 1, 2, 3, 4, 5)
    :param col_coord: (0, 1, 2, 3, 4)
    :param color: ('b', 'w')
    """
    self.piece_type = piece_type
    self.row_coord = row_coord
    self.col_coord = col_coord
    self.color = color

  def __str__(self):
    return ('Piece( ' +
            ColorNames[self.color] + ' ' +
            PieceTypeNames[self.piece_type] + ', ' +
            RowCoordNames[self.row_coord] + '' +
            ColCoordNames[self.col_coord] + ' )')

  __repr__ = __str__


if __name__ == "__main__":
    new_test_piece = ChessPiece('k', 1, 2, 'b')
    print(new_test_piece)
