import os 
import csv

csv_path = os.path.joint ("Resources" , 'budget_data.csv')


with open(budget_data, newline = "") as csvfile:
    cvsreader = csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    #for row in csvreader: 