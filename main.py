import random

import numpy as np
import matplotlib.pyplot as plt


def func_exp(x):
    return np.exp(x)


def draw_function(left_point, right_point):
    array_x = np.linspace(left_point, right_point, 10000)
    array_y = [np.exp(x) for x in array_x]
    plt.plot(array_x, array_y)


def draw_rectangle(x, segment_length, tagging_koef):
    plt.plot((x, x), (0, func_exp(x + segment_length * tagging_koef)), color="Black")
    plt.plot((x + segment_length, x + segment_length), (0, func_exp(x + segment_length * tagging_koef)), color="Black")
    plt.plot((x, x + segment_length),
             (func_exp(x + segment_length * tagging_koef), func_exp(x + segment_length * tagging_koef)), color="Black")


def draw_rectangles(left_point, right_point, number_of_points, way_of_tagging):
    segment_length = (right_point - left_point) / number_of_points
    array_left_x = np.linspace(left_point, right_point, number_of_points + 1)[:-1]
    if way_of_tagging == 777:
        for x in array_left_x:
            tagging_koef = random.random()
            draw_rectangle(x, segment_length, tagging_koef)
    else:
        for x in array_left_x:
            draw_rectangle(x, segment_length, way_of_tagging)


def rectangle_integration(left_point, right_point, number_of_points, way_of_tagging):
    draw_function(left_point, right_point)
    draw_rectangles(left_point, right_point, number_of_points, way_of_tagging)
    summ = 0
    curr_x = left_point
    segment_length = (right_point - left_point) / number_of_points
    if way_of_tagging == 777:
        for i in range(1, number_of_points + 1):
            summ += func_exp(curr_x + segment_length * random.random())
            curr_x += segment_length
    else:
        for i in range(1, number_of_points + 1):
            summ += func_exp(curr_x + segment_length * way_of_tagging)
            curr_x += segment_length
    return summ * segment_length


def draw_trapezoid(x, segment_length):
    plt.plot((x, x), (0, func_exp(x)), color="Black")
    plt.plot((x + segment_length, x + segment_length), (0, func_exp(x + segment_length)), color="Black")
    plt.plot((x, x + segment_length), (func_exp(x), func_exp(x + segment_length)), color="Black")


def draw_trapezoids(left_point, right_point, number_of_points):
    segment_length = (right_point - left_point) / number_of_points
    array_left_x = np.linspace(left_point, right_point, number_of_points + 1)[:-1]
    for x in array_left_x:
        draw_trapezoid(x, segment_length)


def trapezoid_integration(left_point, right_point, number_of_points):
    draw_function(left_point, right_point)
    draw_trapezoids(left_point, right_point, number_of_points)
    summ = 0
    curr_x = left_point
    segment_length = (right_point - left_point) / number_of_points
    for i in range(1, number_of_points + 1):
        summ += (func_exp(curr_x) + func_exp(curr_x + segment_length)) / 2
        curr_x += segment_length
    return summ * segment_length


def main():
    plt.title('Plot for partition into 50 parts')
    str = input("Enter the way of integration (\"trapezoid\" or \"rectangle\"): ").strip()
    if str.__eq__("rectangle"):
        segment_points = list(map(int, input("Enter endpoints of the interval for calculating the integral: ").split()))
        left_point, right_point = segment_points[0], segment_points[1]
        number_of_points = int(input("Enter the number of points in partition: "))
        way_of_tagging = float(input("Enter the way of tagging (number between 0 and 1, or 777 if points are random):"))
        a = rectangle_integration(left_point, right_point, number_of_points, way_of_tagging)
        truth_result = func_exp(right_point) - func_exp(left_point)
        print("Result:            ", a, "\nTruth result:      ", truth_result)
        print("Calculation error: ", abs(truth_result - a))
        plt.show()
    if str.__eq__("trapezoid"):
        segment_points = list(map(int, input("Enter endpoints of the interval for calculating the integral: ").split()))
        left_point, right_point = segment_points[0], segment_points[1]
        number_of_points = int(input("Enter the number of points in partition: "))
        a = trapezoid_integration(left_point, right_point, number_of_points)
        truth_result = func_exp(right_point) - func_exp(left_point)
        print("Result:            ", a, "\nTruth result:      ", truth_result)
        print("Calculation error: ", abs(truth_result - a))
        plt.show()


if __name__ == '__main__':
    main()
