import sys
import blob
import picture


class BeadFinder:
    def __init__(self, pic: picture.Picture, tau):
        """
        Initializing a BeadFinder objec.
        We find all the blobs here.
        """
        self.pic = pic
        self.blobs = []
        self.height = pic.height()
        self.width = pic.width()
        # the table of the picture. When the pixel in (i, j) is above tau, index (i, j) will be true in bmp_table
        self.bmp_table = [[False] * self.width for i in range(self.height)]

        # the table for keeping track of which cells in bmp_table is recorded as blob
        self.found = [[False] * self.width for i in range(self.height)]

        for i in range(self.height):
            for j in range(self.width):
                pixel = pic.get(j, i)
                if (pixel.getRed() + pixel.getGreen() + pixel.getBlue()) / 3 > tau:
                    self.bmp_table[i][j] = True

        # start to find blobs with recursion
        for i in range(self.height):
            for j in range(self.width):
                if self.bmp_table[i][j] and not self.found[i][j]:
                    blob1 = blob.Blob()
                    _find_blobs(self, blob1, i, j)
                    self.blobs.append(blob1)

    def getBeads(self, min_pixels):
        """
        Returns the blobs that has a mass more than min_pixels as an array.
        """
        result = []
        for i in self.blobs:
            if i.mass() >= min_pixels:
                result += [i]
        return result


def _find_blobs(bead_finder: BeadFinder, blob, i, j):
    """
    This is a recursive method to find the blob that pixel at (i, j) is a part of it.
    On each call we add the pixel to the blob if it is connected to it.
    """
    max_i = bead_finder.height
    max_j = bead_finder.width
    # if the index is out of range we return.
    if i < 0 or i >= max_i or j < 0 or j >= max_j:
        return

    # if the cell is not white or it's already been visited we return
    if not bead_finder.bmp_table[i][j] or bead_finder.found[i][j]:
        return
    # if we find a cell that is white and added to the blob we add it and mark it as visited
    if bead_finder.bmp_table[i][j] and not bead_finder.found[i][j]:
        blob.add(j, i)
        bead_finder.found[i][j] = True

    _find_blobs(bead_finder, blob, i, j + 1)
    _find_blobs(bead_finder, blob, i, j - 1)
    _find_blobs(bead_finder, blob, i + 1, j)
    _find_blobs(bead_finder, blob, i - 1, j)


def main():
    min_pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    file_name = sys.argv[3]

    bf = BeadFinder(picture.Picture(file_name), tau)
    beads = bf.getBeads(min_pixels)
    for i in beads:
        print(i)

    print(len(beads))


if __name__ == '__main__':
    main()
