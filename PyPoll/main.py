#import required libraries
import os
import csv

#get filepath to election_data.csv for open()
csvFilePath = os.path.join("Resources","election_data.csv")

#Open the csv file
with open(csvFilePath) as csvFile:
    #make a reader of the csv file
    csvReader = csv.read(csvFile, delimiter = ",")

    #Make a variable for headers using next()
    headers = next(csvReader)

    #store data
    elec_data = []
    for row in csvReader:
        elec_data.append(row)


#make accumulator for number of votes

    
