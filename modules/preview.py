import csv
import matplotlib.pyplot as plt  # type: ignore
from auxiliary import Line, Point


def preview(csv_file: str) -> None:
    print("Previewing the records: ")
    x_val, y_val = [], []
    with open(csv_file, newline="") as File:
        for x, y in csv.reader(File):
            x_val.append(int(x))
            y_val.append(int(y))
    plt.scatter(x_val, y_val)
    plt.xlabel("x Values")
    plt.ylabel("y Values")
    plt.show()


# To preview with colors and legend
def rich_preview(points: list[Point], line: Line) -> None:
    x_cords, y_cords = [], []
    for point in points:
        x_cords.append(point.x)
        y_cords.append(point.y)
    plt.scatter(x_cords, y_cords, color='green', label='Data points')

    x = range(max(x_cords + y_cords) + 1)  # finding maximum range
    y = [line.b * _ + line.a for _ in x]  # y = bx + a
    plt.plot(x, y, color='red', label='y = bx + a')
    plt.xlabel("x Values")
    plt.ylabel("y Values")
    plt.legend(loc="upper left")
    plt.show()
