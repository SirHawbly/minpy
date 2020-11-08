# imports


# class object
class coord_class:

    # constructor
    def __init__(self, yi, xi) -> None:
        """
            args:
                yi - an integer the x part of the coordinate
                xi - an integer the x part of the coordinate
        """

        assert(isinstance(yi, int))
        assert(isinstance(xi, int))

        self.y = yi
        self.x = xi

        self.assert_member_types()


    # type checker
    def assert_member_types(self) -> None:
        """
        """

        assert(isinstance(self.y, int))
        assert(isinstance(self.x, int))


    # string function
    def toString(self) -> str:
        """
        """
        
        self.assert_member_types()

        return "({}:{})".format(self.y, self.x)


# ---

def main() -> None:
    """
    """

    c1 = coord_class(1,2)
    print(c1.toString())

    try:
        print('testing a 2nd coord: {}'.format(coord_class('a', [])))
    except:
        print('can\'t create 2nd coord, assertions held.')
        

# ---

if __name__ == '__main__':
    main()
