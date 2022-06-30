# We're working with a list of name and some information about each one. 
# The create_file function writes this information to a CSV file. 
# The contents_of_file function reads this file into records and returns the information in a nicely formatted block. 
# Fill in the gaps of the contents_of_file function to turn the data in the CSV file into a dictionary using DictReader.

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,lname,type\n")
    file.write("Mike,Dussey,Designer\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open (filename) as file:
    # Read the rows of the file into a dictionary
    f=csv.DictReader(file)
    # Process each item of the dictionary
    for row in f:
      return_string += " {} {} is {}\n".format(row["name"], row["lname"], row["type"])
  return return_string

#Call the function
print(contents_of_file("test.csv"))