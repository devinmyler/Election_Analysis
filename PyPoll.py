# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read and Print the header row.
    headers = next(file_reader)
    print(headers)


# Using the with statement open the file as a text file.
# outfile = open(file_to_save, "w")
# change method of opening file
# with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    # outfile.write("Hello World")
    # Change method pf writing to file
    # txt_file.write("Hello World")

    #Write three counties to the file.
    # txt_file.write("Arapahoe\nDenver\nJefferson")
    # txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
# Close the file
# outfile.close()