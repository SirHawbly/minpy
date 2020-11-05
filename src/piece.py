class piece:

    # constructor
    def __init__(self, pi, di, wi):
        """
            args:
                pi - a coord to describe the pieces location
                di - a character that defines the piece
                wi - an integer for the piece's value
        """

        self.position = pi
        self.data = di
        self.weight = wi

    # getters
    def get_weight(self):
        return self.weight

    def get_data(self):
        return self.data

    def get_pos(self):
        return self.position
