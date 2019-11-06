import os 
import csv

votes_in_total = 0 
candidates = {}
winner = ''
currentMax = 0

csv_path = os.path.join("..","Resources" , 'election_data.csv')

with open(csv_path, newline = "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csv_reader)

    for row in csv_reader: 
        votes_in_total = votes_in_total + 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 0


print("Election Results")
print("-------------------------------------------------")
print("Total Votes: %d" %votes_in_total)
print("-------------------------------------------------")
print("Candidates     Percentages    Total Votes")
for key, value in candidates.items():
    if value > currentMax:
        winner = key
        currentMax = value
    percentage = (value/float(votes_in_total)) * 100
    print('%-15s%-15.0f%d' % (key, percentage, value))
print("-------------------------------------------------")   
print("Winner: %s" %winner)

    
        


