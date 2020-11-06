from coord import coord_class 
from piece import piece_class 

class piece_type:

    # constructor
    def __init__(self):
        """
            create a list of basic chess pieces
        """
        c = coord_class(-1, -1)

        self.king = piece_class("k", -1, c, 20)
        self.queen = piece_class("q", -1, c, 5)
        self.bishop = piece_class("b", -1, c, 4)
        self.knight = piece_class("n", -1, c, 3)
        self.rook = piece_class("r", -1, c, 2)
        self.pawn = piece_class("p", -1, c, 1)


    # string function
    def toString(self):
        """
        """
        
        return ""


# - - -

piece_type_list = piece_type()