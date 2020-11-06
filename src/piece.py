from coord import coord_class as coord

class piece_class:

    # constructor
    def __init__(self, di, pi, ci, wi):
        """
            args:
                di - a character that defines the piece
                pi - a coord to describe the pieces location
                wi - an integer for the piece's value
        """

        assert(isinstance(di, str) and len(di) == 1)
        assert(isinstance(pi, coord))
        assert(isinstance(ci, int))
        assert(isinstance(wi, int))
        
        self.data = di
        self.position = pi
        self.color = ci
        self.weight = wi


    # type check
    def is_of_type(self, p):
        """
        """

        assert(isinstance(p, piece_class))

        if self.data == p.data:
            return True
        else:
            return False


    # string function
    def toString(self):
        """
        """
        
        return "[{},{},{}]{}".format(self.data, self.color, self.weight, self.position.toString())


# ---

def main():
    p1 = piece_class("a", 10, coord(0,0), 2)
    print(p1.toString())

    try:
        print('testing a 2nd piece: {}'.format(piece_class(-8, {}, 'a', [])))
    except:
        print('can\'t create 2nd piece, assertions held.')
        

# ---

if __name__ == '__main__':
    main()

