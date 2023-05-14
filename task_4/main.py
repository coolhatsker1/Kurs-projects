#!/usr/bin/env python3
"made each number float to simplify operations "
"didn't add output of the duplicated names in the form of a range"


def main(args):
    args.pop(0)  # deleted file name from args
    reverse = True
    if "--inv" in args:
        reverse = False
        args.pop(0)  # deleted --inv from args

    names = []
    salary = []
    for element in args:  # creating arrays of names and salaries
        split_element = element.split(":")
        names.append(split_element[0])
        salary.append(float(split_element[1]))

    sorted_arrays = sorted(zip(salary, names), reverse=reverse)  # sorting arrays and unpacking them
    salary, names = list(zip(*sorted_arrays))
    list_all = []

    for i in range(len(names)):
        space_num = max(len(word) for word in names) - len(names[i])  # calculating needed spaces
        if names[i] in names:
            if names[i] in list_all:
                min_value = min(salary[list_all.index(names[i])], salary[i])
                max_value = max(salary[list_all.index(names[i])], salary[i])
                print(f"{names[i].title():5}  {min_value} ... {max_value}")
            list_all.append(names[i])
        if names[i] in list_all:
            print(names[i].title(), int(space_num) * " ", salary[i])




if __name__ == '__main__':
    import sys

    main(sys.argv)
