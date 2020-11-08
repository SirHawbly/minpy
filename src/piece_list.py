# imports
import coord
import piece

from piece_type import piece_type_list


# class object
class piece_list_class:

    # constructor
    def __init__(self, piece_list=[], piece_color=-1) -> None:
        """
        """

        # verify that the passed piece list is a list, and that
        # all pieces inside are actually pieces.
        assert isinstance(piece_list, list)

        for piece_i in piece_list:
            assert(isinstance(piece_i, piece.piece_class))

        # verify that the passed color is an int.
        assert isinstance(piece_color, int)

        # set piece list max size
        self.max_size = 10

        # set data members of class to passed values.
        self.pieces = piece_list
        self.list_color = piece_color

        # run through the list to doublecheck the contents.
        self.assert_member_types()

    
    # check list for each item's type + color
    def assert_member_types(self, ) -> None:
        """
        """
        
        assert isinstance(self.pieces, list)

        # loop through the pieces in the list, verify color and type
        for piece_i in self.pieces:
            assert(isinstance(piece_i, piece.piece_class))
            assert(piece_i.color == self.list_color)
        
        assert self.max_size == 10

        assert isinstance(self.list_color, int)


    # add piece
    def add_piece(self, new_piece) -> None:
        """
        """

        self.assert_member_types()

        if len(self.pieces) > self.max_size:
            assert False
        else:
            self.pieces += [new_piece, ]
    

    # remove piece
    def remove_piece(self, new_piece) -> None:
        """
        """

        self.assert_member_types()

        if len(self.pieces) > 0:
            for piece_i in self.pieces:
                if piece_i == new_piece:
                    self.pieces.remove(new_piece)
        else:
            assert False


    # check for king
    def has_king(self, ) -> bool:
        """
        """

        self.assert_member_types()

        for piece_i in self.pieces:
            if piece_i.is_of_type(piece_type_list.king):
                return True
        
        return False
    

    # total points of pieces in list
    def get_total_points(self, ) -> int:
        """
        """

        self.assert_member_types()

        total = 0
        
        for piece_i in self.pieces:
            total += piece_i.weight
        
        return total


    # string function
    def toString(self, ) -> str:
        """
        """

        self.assert_member_types()

        ret_str = '{} - < '.format(self.list_color) 

        if len(self.pieces) == 0:
            ret_str += ' '

        else:
            for piece_i in self.pieces:
                ret_str += '{} '.format(piece_i.toString())

        return ret_str + '>'


# ---

def main() -> None:
    """
    """

    pl = piece_list_class()

    pl.add_piece(piece_type_list.king)
    
    print(pl.toString())

# ---

if __name__ == '__main__':
    main()
