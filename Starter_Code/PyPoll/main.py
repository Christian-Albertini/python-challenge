import os
import csv


pypoll_csv = os.path.join("Resources", "election_data.csv")
file_path = "analysis/analysis.txt"

total_votes = 0
candidates = {}

with open(pypoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)

    for rows in csvreader:
        if rows[2] not in candidates:
            candidates[rows[2]] = 0
        candidates[rows[2]] = candidates[rows[2]] + 1
        total_votes += 1
    
    final_list = [{"candidate" : rows, "count" : candidates[rows]} for rows in candidates]
    winner = max(candidates, key=candidates.get)
    names = list(candidates.keys())
    votes = list(candidates.values())
    
    
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

