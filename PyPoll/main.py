#import required libraries
import os
import csv

#get filepath to election_data.csv for open()
csvFilePath = os.path.join("Resources","election_data.csv")

#Open the csv file
with open(csvFilePath) as csvFile:
    #make a reader of the csv file
    csvReader = csv.reader(csvFile, delimiter = ",")

    #Make a variable for headers using next()
    headers = next(csvReader)

    #store data
    elec_data = []
    for row in csvReader:
        elec_data.append(row)


#make accumulator for number of votes
votes = 0

#make dictionary to store election results
election_results = {}

#loop through election data to grab results
for row in elec_data:
    #row[0] is ballot ID, row[1] is County, row[2] is candidate
    #Use Candidates as the dictionary key and the number of
        #votes for them as their value
    
    #check to see if candidate is already in dictionary
    if row[2] in election_results:
        #Add to candidate count
        election_results[row[2]] += 1
    #if not in dictionary, add them to dictionary with value 1
    else:
        election_results[row[2]] = 1

    #add to the number of votes
    votes += 1


#make list with style
# [candidate name, candidate votes, candidate percents]
cand_stats = []

#Use to track winner
winner = ""

#loop through keys of election_results (candidate names)
for name in election_results:
    #make new list for each candidate with cand name
    cand = [name]

    #add cand votes after cand name
    cand.append(election_results[name])

    #add cand percent of vote to cand list by 
    #as candidate's vote count/total vote count
    cand.append(election_results[name]/votes*100)

    #add candidate and their stats to the cand_stats list
    cand_stats.append(cand)

    #Create conditional to set winner
    #If winner is blank, set name as winner
    if winner=="":
        winner = name

    #If winner already exists, check if name's vote count
    #is higher than current winner
    elif cand[1]>election_results[winner]:
        #if it is, set the current cand as the new winner
        winner = name


#Print out the required stats
#------------------------------------------------------
print("Election Results")
print("----------------------------")
#Print total votes
print(f"Total Votes: {votes}")
print("----------------------------")
#loop through cand_stats to print results for each candidate
for cand in cand_stats:
    #cand[0] = name, cand[1] = votes, cand[2] = percent of total vote
    print(f"{cand[0]}: {cand[2]:.3f}% ({cand[1]})")
print("----------------------------")
#print winner
print(f"Winner: {winner}")
print("----------------------------")
#------------------------------------------------------



#Write to text file
#------------------------------------------------------
#in order to write to a file, use with open(filepath,"w")
outputFilePath = os.path.join("analysis","results.txt")

with open(outputFilePath,"w") as txtOutput:

    #use the csv .writer() module to write information to a .txt file
    txtWriter = csv.writer(txtOutput)

    #write the information, using same formating as print inside the brackets
    txtWriter.writerow(['Election Results'])
    txtWriter.writerow(["----------------------------"])
    txtWriter.writerow([f"Total Votes: {votes}"])
    txtWriter.writerow(["----------------------------"])
    for cand in cand_stats:
        txtWriter.writerow([f"{cand[0]}: {cand[2]:.3f}% ({cand[1]})"])
    txtWriter.writerow(["----------------------------"])
    txtWriter.writerow([f"Winner: {winner}"])
    txtWriter.writerow(["----------------------------"])