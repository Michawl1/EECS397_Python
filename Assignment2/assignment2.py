"""
@author Michael Thompson (mjt106)
@file assignment2.py
@date 9/13/2019
@details This file outlines the script used for assignment 2 of EECS 397
"""

import sys


def main():
    argument_values = sys.argv

    if len(argument_values) > 2:
        schema_file = file_opener(argument_values[1])
        schema_total = schema_interpreter(schema_file)
        schema_file.close()
        data_file = file_opener(argument_values[2])
        data_values = data_interpreter(data_file, schema_total)
        data_file.close()

        print("{} {}".format(data_values[0], data_values[1]))
    else:
        print("0, 0")


def file_opener(file_name):
    """
    :param file_name: path to a file
    :return: an opened file if successful
    """
    try:
        f = open(str(file_name), "r")
        return f
    except:
        print("0, 0")
        exit(1)


def schema_interpreter(schema_file):
    """
    :param schema_file: an opened schema file
    :return: an (int) value of all the width sums
    """
    schema_list = schema_file.readlines()
    return_list = []
    search_flag = False

    for sch in schema_list:
        # reformat lines to be more uniform
        sch = sch.replace("\t", " ")
        sch = sch.replace("\n", "")

        # split reformatted lines into substrings
        for sub_string in sch.split(" "):
            if sub_string is '#':
                break
            if sub_string.__contains__("width"):
                search_flag = True
            if search_flag and sub_string.isnumeric():
                return_list.append(int(sub_string))
                search_flag = False

    return sum(return_list)


def data_interpreter(data_file, valid_length):
    """
    :param data_file: an opened data file
    :param valid_length: the length of the string for a line to be valid
    :return: a tuple containing the int of valid lines and the int of invalid lines
    """
    data_list = data_file.readlines()
    valid_lines = 0
    invalid_lines = 0

    for data in data_list:
        data = data.replace("\n", "")
        if len(data) is valid_length:
            valid_lines += 1
        else:
            invalid_lines += 1

    return valid_lines, invalid_lines


if __name__ == "__main__":
    main()
