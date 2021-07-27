""" File for Point related functions"""

import csv
from auxiliary import Point


def get_points(filename: str) -> list[Point]:
    with open(filename, newline="") as File:
        return [Point(*map(int, coord)) for coord in csv.reader(File)]
