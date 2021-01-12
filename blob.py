import math


class Blob:

    def __init__(self):
        self.pix_list = []
        self.avg_x = 0
        self.avg_y = 0
        self.mass_val = 0
        pass

    def add(self, x, y):

        self.avg_x = ((self.avg_x * self.mass()) + x) / (self.mass()+1)
        self.avg_y = ((self.avg_y * self.mass()) + y) / (self.mass()+1)
        self.mass_val += 1
        self.pix_list += [[x, y]]

    def mass(self):
        return self.mass_val

    def str(self):
        return '{} ({:.4f}, {:.4f})'.format(self.mass(), self.avg_x, self.avg_y)

    def distanceTo(self, c):
        return math.sqrt((self.avg_x - c.avg_x) ** 2 + (self.avg_y - c.avg_y) ** 2)

    def __str__(self):
        return self.str()

