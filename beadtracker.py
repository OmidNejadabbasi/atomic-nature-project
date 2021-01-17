import sys
import beadfinder
import blob
import picture


def least_distance(b, blobs, delta):
    """
    Finding the closest blob in blobs list to the Blob b. If no blob is in blobs list that has a distance less
    than delta with b, we return None
    """
    least_dist = delta + 1
    for bl in blobs:
        if b.distanceTo(bl) < least_dist:
            least_dist = b.distanceTo(bl)

    if least_dist == delta + 1:
        return None
    else:
        return least_dist


def main():
    # getting inputs
    min_pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    files = sys.argv[4:]

    # -------- We will calculate the distance of each blob in sequential frames --------

    # we store the first beadFinder in beadFinder1
    beadFinder1 = beadfinder.BeadFinder(picture.Picture(files[0]), tau)

    for i in range(1, len(files)):
        bf = beadfinder.BeadFinder(picture.Picture(files[i]), tau)
        for b in beadFinder1.getBeads(min_pixels):
            distance = least_distance(b, bf.getBeads(min_pixels), delta)
            if distance is not None:
                print('{:.4f}'.format(distance))

        beadFinder1 = bf


if __name__ == '__main__':
    main()
