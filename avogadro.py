import sys
import stdio
from math import pi


def variance_f(array):
    """
    This function returns the variance of numbers in array assuming their average is 0.
    """
    total = 0
    pixel_to_meter_const = 0.175e-6
    for r in range(len(array)):
        total += (array[r] * pixel_to_meter_const) ** 2

    return total / (2 * len(array))


def main():
    """
    In the main method we receive the data of beadtracker.py program and calculate the Boltzmann constant
    and the Avogadro number.
    The formula we will use is:
    D = kT / 6Ƞπρ
    """
    # We get the inputs from standard input and store them in data_arr
    data_arr = []
    while not stdio.isEmpty():
        data_arr .append(stdio.readFloat())
    variance = variance_f(data_arr)

    T = 297  # water temperature
    viscosity = 9.135e-4  # the viscosity of water
    p = .5e-6  # the radius of bid

    # D= k*T / (6*pi*viscosity*p)

    k = variance * 6 * pi * viscosity * p / T
    print("Boltzmann : {:.4e}".format(k))
    R = 8.31446
    Avogadro = R / k
    print("Avogadro  : {:.4e}".format(Avogadro))


if __name__ == '__main__':
    main()
