# The data we need to retrieve.
import csv
import os

file_to_load = os.path.join("Resources","Election_Results.csv")
file_to_save = os.path.join("Analysis","Election_Analysis.txt")

# with open(file_to_save, "w") as txt_file:

#     txt_file.write("Counties in the Election\n\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")
    
with open(file_to_load) as election_data:

# To Do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)

# Assign a variable for the file to load and the path.
# 1. The total number of votes cast.
# 2. A complete list of candidates who receive votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

    print(election_data)
