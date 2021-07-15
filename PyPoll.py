# The data we need to retrieve.
import csv
import os

file_to_load = os.path.join("Resources","Election_Results.csv")
file_to_save = os.path.join("Analysis","Election_Analysis.txt")

# with open(file_to_save, "w") as txt_file:

#     txt_file.write("Counties in the Election\n\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")

# Assign a variable for the file to load and the path.

total_votes = 0

candidate_options = []

# Open the results and read file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

 # 1. The total number of votes cast.

    # Print each row in the csv file.
    for row in file_reader:
        total_votes += 1


# 2. A complete list of candidates who receive votes.
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

print(candidate_options)


# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

    # print(election_data)
