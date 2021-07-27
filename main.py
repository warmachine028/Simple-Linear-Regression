from tkinter import Tk
from tkinter.filedialog import askopenfilename as aofn
from statistics import stdev, mean
import math

from modules.auxiliary import Point, BooleanVar, Line
from modules import points as pt
from modules import preview
from modules import predict

regret = BooleanVar()
points: list[Point] = []
reg_line = Line()


# STEP 1: Obtain Points
# STEP 2: Calculate Co-relation Coefficient, r
# STEP 3: Find the slope, b
# STEP 4: Find the y-intercept
# STEP 5: Set the a and b variable in reg_line

def construct_line() -> None:
    points.clear()
    points.extend(pt.get_points(csv_file))
    x_cords = [point.x for point in points]
    y_cords = [point.y for point in points]
    r = co_relation(x_cords, y_cords)
    reg_line.b = r * stdev(x_cords) / stdev(y_cords)  # y-intercept
    reg_line.a = mean(y_cords) - reg_line.b * mean(x_cords)  # slope
    print("Regression Line successfully Constructed")
    regret.set(True)


def co_relation(x_val: list[int], y_val: list[int]) -> float:
    mean_x, mean_y = mean(x_val), mean(y_val)  # mean of xs, mean of ys
    diff_x = [xc - mean_x for xc in x_val]  # differences of x
    diff_y = [yc - mean_y for yc in y_val]  # differences of y
    n = sum(_x * _y for _x, _y in zip(diff_x, diff_y))  # product of differences
    sq_diff_x = map(lambda x: x * x, diff_x)  # squares of differences
    sq_diff_y = map(lambda x: x * x, diff_y)  # squares of differences
    return n / math.sqrt(sum(sq_diff_x) * sum(sq_diff_y))


if __name__ == '__main__':
    Tk().withdraw()
    print(" ** \n Welcome to Simple Linear Regression.\n **\n")
    file_path = aofn(initialdir='data', title="Select a csv file", filetypes=(("csv files", "*.csv"),))
    csv_file = file_path[file_path.rfind('/') - 4:]
    print(f"Working on student records at {csv_file}..")

    while True:
        print("\n  * (1) for Previewing the records")
        print("  * (2) for Constructing Regression Line")
        print("  * (3) for Exiting the program")

        if regret.get():
            print("  * (4) for Getting Prediction")
            print("  * (5) for Rich preview")

        choice = int(input("Enter action: "))

        if choice == 1:  # Previewing the records
            preview.preview(csv_file)

        elif choice == 2:  # Training data
            construct_line()

        elif choice == 3:  # Exiting Program
            break

        elif choice == 4:  # Predict Cluster of Student
            predict.predict(reg_line)

        elif choice == 5:  # Plots more detailed preview
            preview.rich_preview(points, reg_line)

    print("\nThank you for using the predictor! ")
