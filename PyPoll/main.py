import os
import csv


election_data = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')             #Path initiated

with open(election_data, "r")as csvfile:                                                   #Read CSV file
    csvreader= csv.reader(csvfile,delimiter=",")
    election_data_header=next(csvreader)





    candidates = []                                                                         #initiate the candidate list
    count=0                                                                                 #Total Vote count variable
    for row in csvreader:                                                                   #total vote calculation
        count += 1
        candidates.append(row[2])                                                           #filled list with candidate names

    candidate1=0                                                                            #candidates  vote count variables
    candidate2=0
    candidate3=0

    for i in range(len(candidates)-1):                                                      #calculated candidate vote counts and sotred candidate names
        if candidates[i] == "Charles Casper Stockham":
            candidate1 += 1
            candidate1_name=candidates[i]

        if candidates[i] == "Diana DeGette":
            candidate2 +=1
            candidate2_name=candidates[i]

        if candidates[i] == "Raymon Anthony Doane":
            candidate3 += 1
            candidate3_name=candidates[i]




    candidate_percent_1=round((candidate1/count)*100,3)                                                    #calculated and rounded percentage vote count
    candidate_percent_2=round((candidate2/count)*100,3)
    candidate_percent_3=round((candidate3/count)*100,3)


#    print(candidates)
    print("Election Results\n")                                                                             #pritn results
    print("______________________________\n")
    print(f"Total Votes:{count}\n")
    print("______________________________\n")
    print(f"{candidate1_name}: {candidate_percent_1}% ({candidate1})\n")
    print(f"{candidate2_name}: {candidate_percent_2}% ({candidate2})\n")
    print(f"{candidate3_name}: {candidate_percent_3}% ({candidate3})\n")
    print("______________________________\n")
    print(f"Winner : {candidate2_name}\n")
    print("______________________________\n")


with open(os.path.join("analysis","result_data.txt"),"w") as f:                                         #create text with final result
    f.writelines("Election Results\n")
    f.writelines("______________________________\n")
    f.writelines(f"Total Votes:{count}\n")
    f.writelines("______________________________\n")
    f.writelines(f"{candidate1_name}: {candidate_percent_1}% ({candidate1})\n")
    f.writelines(f"{candidate2_name}: {candidate_percent_2}% ({candidate2})\n")
    f.writelines(f"{candidate3_name}: {candidate_percent_3}% ({candidate3})\n")
    f.writelines("______________________________\n")
    f.writelines(f"Winner : {candidate2_name}\n")
    f.writelines("______________________________\n")


