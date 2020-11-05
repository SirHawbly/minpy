

class coord:

    def __init__(self, yi, xi):
        self.y = yi
        self.x = xi

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def toString(self):
        return "({}:{})".format(self.y, self.x)