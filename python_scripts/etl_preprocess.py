import pandas as pd
import cassandra
import re
import os
import glob
import numpy as np
import json
import csv


def collect_file_path_list(filepath):
    """
    Create a for loop to create a list of files and collect each filepath
    """
    file_path_list = []

    # collect each filepath
    for root, dirs, files in os.walk(filepath):
        # join the file path and roots with the subdirectories using glob
        file_path_list = glob.glob(os.path.join(root, '*'))

    return file_path_list

def create_file_csv(file_path_list):
    """
    Processing the files to create the data file csv that will be used for Apache Casssandra tables
    """
    # initiating an empty list of rows that will be generated from each file
    full_data_rows_list = []

    # for every filepath in the file path list
    for f in file_path_list:
        # reading the csv file
        with open(f, 'r', encoding='utf8', newline='') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)
            # skip header row
            next(csvreader)

            # extracting each data row one by one and append it
            for line in csvreader:
                # print(line)
                full_data_rows_list.append(line)

    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    
    # creating a smaller event data csv file called event_datafile_full csv that will be used to insert data into the \
    # Apache Cassandra tables
    with open('event_datafile_new.csv', 'w', encoding = 'utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(['artist','firstName','gender','itemInSession','lastName','length',\
                    'level','location','sessionId','song','userId'])
        for row in full_data_rows_list:
            if (row[0] == ''):
                continue
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))
    
    # check the number of rows in your csv file
    with open('event_datafile_new.csv', 'r', encoding = 'utf8') as f:
        print("Number of rows in your csv file:",sum(1 for line in f))


def main():
    
    # Get your current folder and subfolder event data
    filepath = '../event_data'

    file_path_list = collect_file_path_list(filepath)
    create_file_csv(file_path_list)
    
if __name__ == '__main__':
    main()
