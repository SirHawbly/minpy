class coord:

    # constructor
    def __init__(self, yi, xi):
        """
            args:
                yi - an integer the x part of the coordinate
                xi - an integer the x part of the coordinate
        """

        assert(isinstance(yi, int))
        assert(isinstance(xi, int))

        self.y = yi
        self.x = xi

    # getters
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    # string function
    def toString(self):
        return "({}:{})".format(self.y, self.x)


# ---

def main():
    c1 = coord(1,2)
    print(c1.toString())


# ---

if __name__ == "__main__":
    main()
