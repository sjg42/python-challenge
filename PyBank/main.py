#import os module
import os #allows for operating system / file handling function

#import module for csv files
import csv

#general file path to our contacts.csv -
#../Resources/contacts.csv

#instead, we can use os.path.join to form a path to the csv file
csvFilePath = os.path.join("Resources","budget_data.csv")

#use the with open() funciton to open the csvFilePath into an object
with open(csvFilePath) as csvFile:
    
    
    #csv module .reader() function specifies the delimiter and object name for the
    #reader in the open() function
    csvReader = csv.reader(csvFile, delimiter = ",")

    #csvReader has the info in the file, split into rows of lists
    # that correspond to each row of data in the file

    #Note: Once csvReader has gone through a line,
            #it will not remember the line.
            #E.g. can only run ONE for loop

    #if the first row has header data, use next() to pass over the row
    header = next(csvReader) #skips header data
    b_data = []
    for row in csvReader:
        b_data.append(row)

#make accumulator for months
num_months = 0

#make accumulator for net Profit/Loss
prof_loss = 0

#make variables for greatest increase in profits
greatest_inc_month = 0
greatest_inc_prof = 0

#make variables for greatest decrease in profits
greatest_dec_month = 0
greatest_dec_prof = 0

for i in range(len(b_data)):
    #add to month accumulator
    num_months+=1

    #add to net Prof/Loss
    prof_loss+=float(b_data[i][1])
    
    #check for first month
    if num_months == 1:
        continue
    #check for new greatest increase
    elif (float(b_data[i][1]) - float(b_data[i-1][1]))>greatest_inc_prof:
        greatest_inc_month = b_data[i][0]
        greatest_inc_prof = float(b_data[i][1]) - float(b_data[i-1][1])
    #check for new greatest decrease
    elif (float(b_data[i][1]) - float(b_data[i-1][1]))<greatest_dec_prof:
        greatest_dec_month = b_data[i][0]
        greatest_dec_prof = float(b_data[i][1]) - float(b_data[i-1][1])

#calculate average change in Profits/Losses
#by taking ((last prof/loss value) - (first prof/loss value)) / (num_months-1)
Average_change = (float(b_data[len(b_data)-1][1])-float(b_data[0][1]))/(num_months-1)

#print Necessary info to terminal
print(f"Total Months: {num_months}")
print(f"Total: ${prof_loss:.0f}")
print(f"Average Change: ${Average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc_prof:.0f})")
print(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec_prof:.0f})")


#in order to write to a file, use with open(filepath,"w")
outputFilePath = os.path.join("analysis","analysis.txt")

with open(outputFilePath,"w") as txtOutput:

    #use the csv .writer() module to write information to a .txt file
    txtWriter = csv.writer(txtOutput)

    #write the information
    txtWriter.writerow(['Financial Analysis'])
    txtWriter.writerow(['---------------------------'])
    txtWriter.writerow([f"Total Months: {num_months}"])
    txtWriter.writerow([f"Total: ${prof_loss:.0f}"])
    txtWriter.writerow([f"Average Change: ${Average_change:.2f}"])
    txtWriter.writerow([f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc_prof:.0f})"])
    txtWriter.writerow([f"Greatest Increase in Profits: {greatest_dec_month} (${greatest_dec_prof:.0f})"])
