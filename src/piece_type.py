# imports
import coord
import piece 


# class object
class piece_type:

    # constructor
    def __init__(self) -> None:
        """
            create a list of basic chess pieces
        """

        c = coord.coord_class(-1, -1)

        self.king = piece.piece_class("k", c, -1, 20)
        self.queen = piece.piece_class("q", c, -1, 5)
        self.bishop = piece.piece_class("b", c, -1, 4)
        self.knight = piece.piece_class("n", c, -1, 3)
        self.rook = piece.piece_class("r", c, -1, 2)
        self.pawn = piece.piece_class("p", c, -1, 1)
        self.blank = piece.piece_class('-', c, -1, -1)

    # string function
    def toString(self) -> str:
        """
        """
        
        return ""


# - - -

piece_type_list = piece_type()