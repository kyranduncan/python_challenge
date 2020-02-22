import os
import csv

#Define variables
votes = 0
vote_count = []
candidates = []
csv_reader = ['1','2']


# Pull in data & read file
csvpath = os.path.join("C:/Users/kyran/OneDrive/Documents/Python_HW/pypoll_data.csv")

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    next(csv_reader)

    for row in csv_reader:

        #Tally votes
        votes = votes + 1

        #Candidates
        candidate = row[2]

        #Votes per candidate
        if candidate in candidates:
           candidate_index = candidates.index(candidate)
           vote_count[candidate_index] = vote_count[candidate_index] + 1
           
        else:
           candidates.append(candidate)
           vote_count.append(1)

        
#Percentages
percentages = []
most_votes = vote_count[0]
most_votes_index = 0

for count in range(len(candidates)):
    vote_percentage = vote_count[count]/votes*100
    percentages.append(vote_percentage)
    if vote_count[count] > most_votes:
        print(most_votes)
        most_votes_index = count
winner = candidates[most_votes_index]

percentages = [round (i,2) for i in percentages]

#Print results           
print()
print("Election Results")
print("--------------------------------")
print(f"Total Votes: {votes}")
print("--------------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_count[count]})")
print("--------------------------------")
print(f"Winner:  {winner}")
print("--------------------------------")

new_line = "\n"
     #print total months, total profit/losses, and average change to document
text_file = open('pypoll_election_analysis.txt', 'w')
text_file.write("ELECTION RESULTS")
text_file.write(new_line)
text_file.write("----------------------------------------------------------")
text_file.write(new_line)
text_file.write("Total Votes: {votes}")
text_file.write(new_line)
text_file.write("----------------------------------------------------------")
text_file.write(new_line)
for count in range(len(candidates)):
    text_file.write(f"{candidates[count]}: {percentages[count]}% ({vote_count[count]})") 
text_file.write(new_line)
text_file.write("----------------------------------------------------------")
text_file.write(new_line)
text_file.write(f"Winner:  {winner}")
text_file.write(new_line)
text_file.write("----------------------------------------------------------")
    
text_file.close()









