"""
This script reads in a text file where there are two values per line. These values are split into two lists of integers and the similarity between the two lists is calculated. The similarity score is defined as sum of all values in the first list multiplied by the number of their occurences in the second list. Here, we use functions from the standard Python library. 

To run simply update the filepath for list_file and run from the terminal. Example: python3 determine_list_similarity.py

Last updated by: Samantha Fischer 01DEC2024
"""
# import modules - collections will allow us to be more efficient than using built-in .count() function
from collections import Counter

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

    # sort the lists in ascending order; not necessary, but nice for spot-checking
    first_list.sort()
    second_list.sort()
    
    # initiate score at 0
    similarity_score = 0

    # count the insances of different integers in second list
    counter = Counter(second_list)

    for num in first_list:
        # if num isn't in the second list, counter will return 0
        similarity_score += (num * counter[num])

    # prin the total similarity score
    print(f"The similarity between the lists is: {similarity_score}")
