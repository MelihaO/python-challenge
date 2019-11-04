import os 

import csv

csv_path = os.path.join("..", "Resources" , 'budget_data.csv')

with open(csv_path, newline = "") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csv_reader)

    months_intotal = 0

    Net_profit_loss = []
    
    Net_changes = []

    months = []

    max_profit = 0

    max_loss = 0 

    for row in csv_reader:

        months_intotal = months_intotal + 1

        Net_profit_loss.append(row[1])

        months.append(row[0])
 
    #net total loss and profit

    Net_total_loss_profit = 0

    for l in range(len(Net_profit_loss)):

        print(Net_profit_loss[l])

        Net_total_loss_profit = Net_total_loss_profit + int(Net_profit_loss[l])

        if l != 0:
            Net_changes.append(int(Net_profit_loss[l]) - int(Net_profit_loss[l -1]))

    #get max and minimum change        
            
    max_profit = max(Net_changes)

    max_loss = min(Net_changes)

    #get months where max and minimum change occurred
    
    max_profit_month_ind = Net_changes.index(max_profit)

    max_loss_month_ind = Net_changes.index(max_loss)
    
    #calculate average change

    avg_change = float(sum(Net_changes)) / (months_intotal -1)


    #print formatting

    print("Financial Analysis")

    print("----------------------------------------")

    print("Total Months: %d" %months_intotal)

    print("Total Revenue: $%d" %Net_total_loss_profit)

    print("Average Change: $%.2f" %avg_change)

    print("Greatest increase: %s ($%d)" % (months[max_profit_month_ind + 1], max_profit))

    print("Greatest decrease: %s ($%d)" % (months[max_loss_month_ind + 1], max_loss))p