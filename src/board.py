# imports
import coord
import piece
import piece_list

from piece_list import piece_list_class


# class object
class board_class:

    # constructor
    def __init__(self, ):
        """
        """

        # constatnts
        self.y_dim = 6
        self.x_dim = 5

        self.player_one_color = 1
        self.player_two_color = 2

        self.piece_array = []
        
        self.player_one_pieces = piece_list.piece_list_class()
        self.player_two_pieces = piece_list.piece_list_class()


    # check list for each item's type + color
    def assert_member_types(self, ) -> None:
        """
        """

        assert self.y_dim == 6
        assert self.x_dim == 5

        assert len(self.piece_array) == self.y_dim

        for row in self.piece_array:
            assert len(row) == self.x_dim

        assert self.player_one_color != self.player_two_color

        assert self.player_one_pieces.list_color == self.player_one_color
        assert self.player_two_pieces.list_color == self.player_two_color

        self.player_one_pieces.assert_member_types()
        self.player_two_pieces.assert_member_types()


    # string function
    def toString(self):
        """
        """
        
        return ""


# ---

def main():
    """
    """

    return    

# ---

if __name__ == '__main__':
    main()
