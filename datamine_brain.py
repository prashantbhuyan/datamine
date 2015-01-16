__author__ = 'MicrostrRes'

import math
import sys

# In this application I'm reading in data for brain and body values
# and finding the slope and intercept of the regression line using the
# determinant method.

# This function converts elements of an input list to type float.
def convert(arr):
    floatConv = []
    for i in arr[1:]:
        floatConv.append(float(i))
    return floatConv

# This regression function takes as input two arrays of type string,
# calls the convert function to make them of type float,
# maps the values of brain and body such that the values of each variable are iterable tuples,
# and performs operations on the tuples to get the values needed to compute a determinant value.
# The function then uses the determinant value to get the slope (m) and the intercept (b) of the
# regression equation that best fits the data.

def regress(arr1,arr2):

    # Error Handling.
    if len(arr1) != len(arr2):
        print("Cannot Operate on Different Size Arrays . . . ")
        return
    arr_length = len(arr1)

    # Store converted values to new arrays.
    floatList1 = []
    floatList2 = []

    # Initialize variables that will store sums.
    sum_x = 0.0
    sum_y = 0.0
    sum_xx = 0.0
    sum_yy = 0.0
    sum_xy = 0.0

    # Populate float arrays by calling conversion function above.
    floatList1 = convert(arr1)
    floatList2 = convert(arr2)

    # Iterate over tuples and apply get the values needed for the determinant equation.
    for i,j in map(None,floatList1,floatList2):
        sum_x += i
        sum_y += j
        sum_xx += i**2
        sum_yy += j**2
        sum_xy += i*j

    # Compute the determinant.
    d = arr_length*sum_xx - sum_x*sum_x

    print "Determinant Value: ", d, "\n"
    # Compute the slope.
    m = (sum_xy * arr_length - sum_y * sum_x)/d

    print "Slope Value: ", m, "\n"

    # Compute the y - intercept.
    b = (sum_xx * sum_y - sum_x * sum_xy)/d

    print "Y Intercept Value: ", b

    # In Slope Intercept Form . . .
    print("")
    print "In Form y = mx + b:"
    print "y = " , m,"x +",b


def main():

    brain = []
    body = []

    try:
        file = open('/Users/MicrostrRes/Downloads/brainandbody.csv')
        try:
            for line in file:
                args = line.rstrip("\n").split(",")
                brain.append(args[1])
                body.append(args[2])
        finally:
            file.close()
    except:
        print "File Error . . ."
        return

    regress(brain,body)

if __name__ == '__main__':
    main()

