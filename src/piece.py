# imports
import coord


# class object
class piece_class:

    # constructor
    def __init__(self, ki, pi, ci, wi) -> None:
        """
            args:
                di - a character that defines the piece
                pi - a coord to describe the pieces location
                wi - an integer for the piece's value
        """

        assert(isinstance(ki, str) and len(ki) == 1)
        assert(isinstance(pi, coord.coord_class))
        assert(isinstance(ci, int))
        assert(isinstance(wi, int))
        
        self.key = ki
        self.position = pi
        self.color = ci
        self.weight = wi

        self.assert_member_types()


    # type checker
    def assert_member_types(self) -> None:
        """
        """

        assert(isinstance(self.key, str) and len(self.key) == 1)
        assert(isinstance(self.position, coord.coord_class))
        assert(isinstance(self.color, int))
        assert(isinstance(self.weight, int))

        
    # piece key check
    def is_of_type(self, new_piece=None) -> bool:
        """
        """

        assert(isinstance(new_piece, piece_class))

        self.assert_member_types()

        if self.key == new_piece.key:
            return True
        else:
            return False


    # setter for position
    def set_position(self, new_coord=coord.coord_class(0,0)) -> None:
        """
        """

        assert(isinstance(new_coord, coord))

        self.assert_member_types()

        self.position = new_coord


    # setter for color
    def set_color(self, new_color=-1) -> None:
        """
        """

        assert(isinstance(new_color, int))

        self.assert_member_types()

        self.color = new_color


    # string functions
    def toString(self) -> str:
        """
        """
        
        self.assert_member_types()

        return "[{},{},{}]{}".format(self.key, self.color, self.weight, self.position.toString())


    # function to get key with case
    def print_key(self, is_capital=False) -> str:
        """
        """

        assert(isinstance(is_capital, bool))

        self.assert_member_types()

        if is_capital:
            return self.key.lower()
        else:
            return self.key.upper()


# ---

def main() -> None:
    """
    """

    p1 = piece_class("a", coord.coord_class(0,0), 10, 2)

    print(p1.toString())

    try:
        print('testing a 2nd piece: {}'.format(piece_class(-8, {}, 'a', [])))
    except:
        print('can\'t create 2nd piece, assertions held.')
        

# ---

if __name__ == '__main__':
    main()

