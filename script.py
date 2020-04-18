#Christina Aiello
#2020
#Protected under MIT license

import os
import sys
import csv
from datetime import datetime

class DataPoint:
    # 'self' is a python thing you always need.
    # some_date, some_data_name, and some_data_value are all the data points being passed in to the object
    def __init__(self, some_date, some_data_name, some_data_value):
        self.date = some_date
        self.data_name = some_data_name
        self.data_value = some_data_value

# This will hold all of our new data rows
data_list = []
data_point_names = []

# ./script/input is where you put your initial data
for file_name in os.listdir('./input'):
    # a_file is the file in your directory that you're currently looking at
    a_file = open(sys.path[0] + "/input/" + file_name, "r")
    # The data becomes a list of lists. Each item in the outer list is a row. Each item in the inner list is a cell within that row.
    file_as_list_of_lists = list(csv.reader(a_file))
    # This tells us how many rows the spreadsheet has
    number_of_rows = len(file_as_list_of_lists)
    
    # First row has the titles of all of the columns
    titles_of_columns = file_as_list_of_lists[0]
    number_of_columns = len(titles_of_columns)
    # To slice a list, the syntax is: array[start:stop:step]
    # Here I'm starting at index 1, and I'm just stopping whenever it ends.
    # This gets rid of the "Time Stamp" cell, cell A1, from that first row.
    data_point_names = titles_of_columns[1:]

    # Iterate over each row in the file. 
    # We want to start at the second row (index one) in the list of rows,
    # # and we end once we hit number_of_rows.
    # You can think of the row_index as being the column number in the spreadsheet.
    for row_index in range(1, number_of_rows):
        # Grab the date from the start of the row
        row = file_as_list_of_lists[row_index]
        # First item in the row is the first column's value, which is the date
        date = row[0]
        # We want to start at the second thing (index one) in the row,
        # and we end once we hit number_of_columns
        for cell_index in range(1, number_of_columns - 1):
            # Only process rows that actually have data in them
            if (row[cell_index] != ""):
                # Make a new data point.
                # Remember, data_point_names is a new array I made that starts at index 0,
                # and the original data set that had the column names in it starts at index
                # 1 because of the time stamp column. So when you're grabbing data from 
                # row[cell_index], the corresponding data_point_name's index is one less than that.
                data_point = DataPoint(date, data_point_names[cell_index - 1], row[cell_index])
                # Add this data point to our list of data points
                data_list.append(data_point)
            else:
                # If a row has no data in it, we break out of this loop.
                # This keeps us from iterating over a bunch of empty cells.
                break

# Make this directory if it doesn't exist
if not os.path.exists("./output"):
    # ./script/output is where your output is going
    os.mkdir("./output")

# Make a new file
with open("output/" + datetime.now().strftime("%d-%m-%Y") + "-fixed-data.csv", "w") as csv_file:
    # Each new line ends with a new line
    # Each data point has a comma after it
    wr = csv.writer(csv_file, lineterminator='\n', delimiter=',')
    # Looping over each data point in our list of DataPoints
    for data in data_list:
        # Write a new row to the csv file
        wr.writerow([data.data_name, data.date, data.data_value])
