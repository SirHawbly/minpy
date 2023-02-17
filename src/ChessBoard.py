from ChessPiece import ChessPiece

board_header = " | a | b | c | d | e |\n"


class ChessBoard:

  def __init__(self, turn: int = 0) -> None:

    self.board = []
    self.turn = turn
    self.turn_limit = 40 # 20 per player

    for j in range(0, 6):
      row = []

      for i in range(0, 5):
        row += [ChessPiece('.', j, i, 'n'), ]

        # print(row)
        self.board += [row, ]

    # print(self.board)

  def __str__(self) -> str:
    ret_str = 'turn: ' + str(self.turn) + '\n' + board_header

    for j in range(0, 6):

      ret_str += str(j) + '| '

      for i in range(0 ,5):
        ret_str += self.board[j][i].piece_type + ' | '

      ret_str += '\n'

    return ret_str

  def reset_board(self) -> None:
    return

  def import_board(self, board_state: str) -> None:
    return

  def export_board(self) -> str:
    ret_str = ''
    return ret_str


if __name__ == "__main__":
  test_chess_board = ChessBoard(11)
  print(test_chess_board)
