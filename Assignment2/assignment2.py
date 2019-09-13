"""
@author Michael Thompson (mjt106)
@file assignment2.py
@date 9/13/2019
@details This file outlines the script used for assignment 2 of EECS 397
"""

import sys


def main():
    argument_values = sys.argv
    print(argument_values)

    schema_file = file_opener(argument_values[1])
    data_file = file_opener(argument_values[2])


def file_opener(file_name):
    try:
        f = open(str(file_name), "r")
        print("succesfully opened: {}".format(file_name))
        return f
    except:
        print("could not open file {}".format(file_name))
        print("exiting")
        exit(1)


if __name__ == "__main__":
    main()
