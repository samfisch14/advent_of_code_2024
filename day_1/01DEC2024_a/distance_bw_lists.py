"""
This script reads in a text file where there are two values per line. These values are split into two lists of integers and the distance between the two lists is calculated. The distance is defined as the sum of absolute differences. Here, we use only built-in Python functions. 

To run simply update the filepath for list_file and run from the terminal. Example: python3 distance_bw_lists.py

Last updated by: Samantha Fischer 01DEC2024
"""

# manually created file with copied input from advent of code day 1 (2024)
list_file = '../list_input.txt'

# intiate the two lists outside of loop
first_list = []
second_list = []

# read the file 
with open(list_file, 'r') as file:
    
    # pull the text out into two lists by looping through through the file lines
    for line in file:
        line = line.strip().split()

        # try to convert to integer, if can't file isn't structured properly
        try:
            first_list.append(int(line[0]))
            second_list.append(int(line[1]))
        # else print an error message because this means file is not formatted as expected
        except:
            print("Error, unexpected formatting issues!")

    # sort the lists in ascending order using built-in function
    first_list.sort()
    second_list.sort()
    
    # initiate list for distances
    distances = []

    # check to make sure lists are of equal length or else this won't work
    if len(first_list) == len(second_list):
        for i in range(len(first_list)):
            distance = abs(first_list[i] - second_list[i])
            distances.append(distance)

    # else return an error
    else:
        print('Error, lists are not of equal length! You need to check formatting of input file!')

    # get the sum
    answer = sum(distances)

    print(f"The total distances between lists is: {answer}")
