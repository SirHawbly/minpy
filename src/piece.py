from coord import coord_class as coord

class piece_class:

    # constructor
    def __init__(self, pi, di, wi):
        """
            args:
                pi - a coord to describe the pieces location
                di - a character that defines the piece
                wi - an integer for the piece's value
        """

        assert(isinstance(pi, coord))
        assert(isinstance(di, str) and len(di) == 1)
        assert(isinstance(wi, int))
        
        self.position = pi
        self.data = di
        self.weight = wi

    # string function
    def toString(self):
        return "[{},{}]{}".format(self.data, self.weight, self.position.toString())


# ---

def main():
    p1 = piece_class(coord(0,0), "a", 2)
    print(p1.toString())

    try:
        print('testing a 2nd piece: {}'.format(piece_class(-8, 'a', [])))
    except:
        print('can\'t create 2nd piece, assertions held.')
        

# ---

if __name__ == '__main__':
    main()

