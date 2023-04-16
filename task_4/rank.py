#!/usr/bin/env python3
"made each number float to simplify operations "
        
def main(args):

    
    args.pop(0) #deleted file name from args
    reverse = True
    if "--inv" in args:
        reverse = False
        args.pop(0)#deleted --inv from args
    
    names = []
    salary = []
    for element in args:
        split_element = element.split(":")
        names.append(split_element[0])
        salary.append(float(split_element[1]))

        
    sorted_arrays = sorted(zip(salary, names), reverse=reverse)
    salary, names = zip(*sorted_arrays)
    
    for i in range(len(names)):
        space_num = max(len(word) for word in names)-len(names[i])
        print(names[i].title(), int(space_num) * " ", salary[i])
        
if __name__ == '__main__':
    import sys
    main(sys.argv)
