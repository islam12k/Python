import os
import csv


budget_data = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#Path initiated

with open(budget_data, "r")as csvfile:
    csvreader= csv.reader(csvfile,delimiter=",")
    budget_data_header=next(csvreader)
    profit_loss_list = []                                            #initiate the empty list for the amount
    count = 0                                                       #initiate the variable to count Months
    net_profit = 0                                                    #initiate the variable to count net_profit
    profit_loss_time = []                                               #initiate the empty list for the time

    for row in csvreader:
        profit_loss_list.append(int(row[1]))                                #append all amounts in list
        profit_loss_time.append(row[0])                                   #append all items for time
        count += 1                                                             #count months
        net_profit += int(row[1])                                             #calculate net profit
# print(profit_loss_list)


    change_list = []

    for i in range(len(profit_loss_list)-1):                                    #calculate change from each items
        change = profit_loss_list[i+1]-profit_loss_list[i]
        change_list.append(change)                                             #all items fom change

#  print(change_list)

    maximum_profit= max(change_list)                                          #calculate the max profit

    minimum = min(change_list)                                                  #calculate min profit

# print(change_list.index($1862002))
# print(change_list.index(-1825558))




    greatest_profit = (profit_loss_time[79])                               #extrasct months from the time list
    greatest_loss = (profit_loss_time[49])

    Average=0
    for i in range(len(change_list)):                                              #calculate average
        Average += change_list[i]

    total_average = (Average/len(change_list)-1)


    print("Finanacial Analysis\n")                                              #print results
    print("\n ____________________________________\n")
    print(f"Total Months: {count}\n")
    print(f"Total: ${net_profit}\n")
    print(f"Average Change:$ {total_average}\n")
    print(f"Greatest Increase in profits: {greatest_profit} (${maximum_profit})\n")
    print(f"Greatest Decrease in profits: {greatest_loss} (${minimum})\n")

with open(os.path.join("analysis","finanacial_analysis.txt"),"w") as f:        #create text file with the result
    f.writelines("Finanacial Analysis\n")
    f.writelines("______________________________\n")
    f.writelines(f"Total Months: {count}\n")
    f.writelines(f"Total: ${net_profit}\n")
    f.writelines(f"Average Change:$ {total_average}\n")
    f.writelines(f"Greatest Increase in profits: {greatest_profit} (${maximum_profit})\n")
    f.writelines(f"Greatest Decrease in profits: {greatest_loss} (${minimum})\n")

3




















