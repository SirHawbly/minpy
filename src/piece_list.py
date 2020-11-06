from coord import coord_class 
from piece import piece_class 
from piece_type import piece_type_list

class piece_list_class:

    # constructor
    def __init__(self, ):
        """
        """

        self.pieces = []
        self.piece_color = -1

    
    # check list for each item's type
    def assert_pieces(self, ):
        """
        """
        
        for p in self.pieces:
            assert(isinstance(p, piece_class))


    # check for color
    def assert_piece_color(self, ):
        """
        """

        for p in self.pieces:
            assert(p.color == self.piece_color)


    # check for king
    def has_king(self, ):
        """
        """

        for p in self.pieces:
            if p.is_of_type(piece_type_list.king):
                return True
        
        return False
    

    # total points of pieces in list
    def get_total_points(self, ):
        """
        """

        t = 0
        
        for p in self.pieces:
            t += p.weight
        
        return t

    # string function
    def toString(self):
        return ""


# ---

def main():
    print("")
        

# ---

if __name__ == '__main__':
    main()
