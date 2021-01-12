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

        self.avg_x = ((self.avg_x * self.mass()) + x) / (self.mass() + 1)
        self.avg_y = ((self.avg_y * self.mass()) + y) / (self.mass() + 1)
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


def main():
    b1 = Blob()
    b1.add(20, 20)
    b1.add(20, 21)
    b1.add(20, 22)
    b1.add(21, 20)
    b1.add(21, 21)
    b2 = Blob()
    b2.add(40, 40)
    b2.add(20, 41)
    b2.add(40, 42)
    b2.add(41, 40)
    b2.add(41, 41)

    print('blob 1: ' + b1)
    print('blob 2: ' + b2)
    print('Distance form b1 to b2 : ' + b1.distanceTo(b2))


if __name__ == '__main__':
    main()
