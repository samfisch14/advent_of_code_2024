"""
This script reads in a text file of reports (lines of integers) and filters for 'safe' reports. Reports are defined as safe if they are sequentially increasing or decreasing and if their increase/decreases are at least 1 and not greater than 3. 

Example implementation: python3 safe_reports.py

Last updated: Samantha Fischer 02DEC2024
"""

# we are using numpy for convenient use of array operations
import numpy as np

# define function to read-in file as list of lists
def convert_data(file):

    # initialize list for data
    data = []

    # open file and loop thru lines
    with open(file) as f:
        for line in f:
            
            # split each line into a list which will be mapped to int from str
            row = list(map(int, line.split()))
            data.append(row)

    return data

# define function to check if increasing, decreasing, or neither
def check_order(data_array):
    # intialize list for all the reports which meet 'safe' criteria 
    safe_reports = []
    
    # loop through each report (row) in array of reports
    for row in data_array:
        
        # use np.diff to determine the pairwise difference of sequential integers
        diff = np.diff(row)

        # if all differences are negative or positive this means they are either increasing or decreasing
        if np.all(diff < 0) or np.all(diff > 0):
            
            # we use the absolute value of the pairwise differences to filter for increases/decreases w/i range(0,3)
            if np.all((np.abs(diff) >= 1) & (np.abs(diff) <= 3)):
                
                # collect all reports which meet this criteria
                safe_reports.append(row)


    return safe_reports

# input report data
report_data = convert_data('../half_examples.txt')

# filter for safe reports
safe = check_order(report_data)

# print the answer
print(f"Number of safe reports {len(safe)}")
