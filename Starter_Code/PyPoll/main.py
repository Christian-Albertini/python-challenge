# Import modules
import os
import csv

# Path to collect data from the Resource folder and create new file in analysis folder
pypoll_csv = os.path.join("Resources", "election_data.csv")
file_path = "analysis/analysis.txt"

# Set values and dictionary
total_votes = 0
candidates = {}

# Read in CSV file
with open(pypoll_csv) as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter = ",")
    # Get header
    csv_header = next(csvreader)
    # Loop through the file
    for rows in csvreader:
        # Check to see if value in 3rd column of rows is in candidates dictionary
        if rows[2] not in candidates:
            # If not, create new row in candidate that has the name and sets the count to 0
            candidates[rows[2]] = 0
        # Adds one to the vote count for the candidate in the row
        candidates[rows[2]] = candidates[rows[2]] + 1
        # Add one to total votes
        total_votes += 1
    
    # Create a value that sees who won by finding the max value in the candidates list
    winner = max(candidates, key=candidates.get)
    # Creates a list that holds the keys from the candidates dictionary, which are the names of the candidates
    names = list(candidates.keys())
    # Creates a list that holds the values from the candidates dictionary, which is the vote counts
    votes = list(candidates.values())
    
# Create new text file in analysis and write in results
with open(file_path, 'w') as file:
    file.write("Election Results\n")
    file.write("\n")
    file.write("--------------------------------------------------\n")
    file.write("\n")
    file.write("Total Votes: " + str(total_votes) +"\n")
    file.write("\n")
    file.write("--------------------------------------------------\n")
    file.write("\n")
    file.write(names[0] + ": " + str(round(((votes[0]/total_votes)*100), 3)) + "% ("+ str(votes[0])+ ")\n")
    file.write("\n")
    file.write(names[1] + ": " + str(round(((votes[1]/total_votes)*100), 3)) + "% ("+ str(votes[1])+ ")\n")
    file.write("\n")
    file.write(names[2] + ": " + str(round(((votes[2]/total_votes)*100), 3)) + "% ("+ str(votes[2])+ ")\n")
    file.write("\n")
    file.write("--------------------------------------------------\n")
    file.write("\n")
    file.write("Winner: " + winner + "\n")
    file.write("\n")
    file.write("--------------------------------------------------\n")

# Print same results from text file in the terminal
print("Election Results")
print("")
print("--------------------------------------------------")
print("")
print("Total Votes: " + str(total_votes))
print("")
print("--------------------------------------------------")
print("")
print(names[0] + ": " + str(round(((votes[0]/total_votes)*100), 3)) + "% ("+ str(votes[0])+ ")")
print("")
print(names[1] + ": " + str(round(((votes[1]/total_votes)*100), 3)) + "% ("+ str(votes[1])+ ")")
print("")
print(names[2] + ": " + str(round(((votes[2]/total_votes)*100), 3)) + "% ("+ str(votes[2])+ ")")
print("")
print("--------------------------------------------------\n")
print("")
print("Winner: " + winner)
print("")
print("--------------------------------------------------\n")

