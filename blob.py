import math


class Blob:
    """
    A class representing a group of pixels connected together.
    All functions have constant running complexity.
    """

    def __init__(self):
        self.pix_list = []
        self.avg_x = 0
        self.avg_y = 0
        self.mass_val = 0
        pass

    def add(self, x, y):
        """
        Adds the pixel with the specified coordinates x and y to the Blob
        :param x: The x of the pixel
        :param y: The y of the pixel
        """

        self.avg_x = ((self.avg_x * self.mass()) + x) / (self.mass()+1)
        self.avg_y = ((self.avg_y * self.mass()) + y) / (self.mass()+1)
        self.mass_val += 1
        self.pix_list += [[x, y]]

    def mass(self):
        """
        :return: Returns the number of pixels in this Blob
        """
        return self.mass_val

    def str(self):
        """
        :return: Returns the string form of this Blob
        """
        return '{} ({:.4f}, {:.4f})'.format(self.mass(), self.avg_x, self.avg_y)

    def distanceTo(self, c):
        """
        Computes the distance of center of this Blob with the other Blob c
        """
        return math.sqrt((self.avg_x - c.avg_x) ** 2 + (self.avg_y - c.avg_y) ** 2)

    def __str__(self):
        return self.str()
