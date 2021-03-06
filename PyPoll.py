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
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

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
            
            # Add candidate to list of candidates
            candidate_options.append(candidate_name)
            
            # Add candidate to dictionary
            candidate_votes[candidate_name] = 0
        
        # Add a vote to candidate count
        candidate_votes[candidate_name] += 1

with open(file_to_save,"w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 3. The percentage of votes each candidate won.
    # 4. The total number of votes each candidate won.
    for candidate_name in candidate_votes:
        
        # Retrieve vote count.
        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes) / float(total_votes) * 100

        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)
        txt_file.write(candidate_results)

    # 5. The winner of the election based on popular vote.

        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # print(election_data)
    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
