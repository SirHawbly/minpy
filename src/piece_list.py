from coord import coord_class 
from piece import piece_class 
from piece_type import piece_type_list

class piece_list_class:

    # constructor
    def __init__(self, piece_list=[], piece_color=-1):
        """
        """

        # verify that the passed piece list is a list, and that
        # all pieces inside are actually pieces.
        assert isinstance(piece_list, list)

        for piece in piece_list:
            assert(isinstance(piece, piece_class))

        # verify that the passed color is an int.
        assert isinstance(piece_color, int)

        # set data members of class to passed values.
        self.pieces = piece_list
        self.list_color = piece_color

        # run through the list to doublecheck the contents.
        self.assert_member_types()

    
    # check list for each item's type + color
    def assert_member_types(self, ):
        """
        """
        
        for piece in self.pieces:
            assert(isinstance(piece, piece_class))
            assert(piece.color == self.list_color)


    # check for king
    def has_king(self, ):
        """
        """

        for piece in self.pieces:
            if piece.is_of_type(piece_type_list.king):
                return True
        
        return False
    

    # total points of pieces in list
    def get_total_points(self, ):
        """
        """

        total = 0
        
        for piece in self.pieces:
            total += piece.weight
        
        return total

    # string function
    def toString(self, ):
        """
        """

        return ""


# ---

def main():
    print("")
        

# ---

if __name__ == '__main__':
    main()
