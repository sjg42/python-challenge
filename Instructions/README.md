# Unit 3 Homework: Python

In this assignment, you'll complete two challenges in which you'll apply your new Python skills. 

## Background

It's time to put away the Excel sheet and join the big leagues. Welcome to the world of programming with Python. In this homework assignment, you'll use the concepts you've learned to complete the **two** Python challenges, PyBank and PyPoll.

Both of these challenges present a real-world situation where your newfound Python scripting skills can come in handy. These challenges aren't easy, so expect some hard work ahead!

## Setup

Before starting the assignment, be sure to do the following:

* Create a new repository for this project called `python-challenge`. **Do not add this homework assignment to an existing repository**.

* Clone the new repository to your computer.

* Inside your local git repository, create a directory for each Python challenge. Use folder names corresponding to the challenges: **PyBank** and  **PyPoll**.

* Inside of each folder that you just created, add the following:

  * A new file called `main.py`. This will be the main script to run for each analysis.
  * A `Resources` folder that contains the CSV files you used. Make sure your script has the correct path to the CSV file.
  * An `analysis` folder that contains your text file that has the results from your analysis.

* Push these changes to GitHub or GitLab.

## PyBank Instructions

In this challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: "Date" and "Profit/Losses". (Thankfully, your company has rather lax standards for accounting, so the records are simple.)

Your task is to create a Python script that analyzes the records to calculate each of the following:

* The total number of months included in the dataset

* The net total amount of "Profit/Losses" over the entire period

* The changes in "Profit/Losses" over the entire period, and then the average of those changes

* The greatest increase in profits (date and amount) over the entire period

* The greatest decrease in profits (date and amount) over the entire period

Your analysis should look similar to the following:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $22564198
  Average Change: $-8311.11
  Greatest Increase in Profits: Aug-16 ($1862002)
  Greatest Decrease in Profits: Feb-14 ($-1825558)
  ```

In addition, your final script should both print the analysis to the terminal and export a text file with the results.

## PyPoll Instructions

In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote.

Your analysis should look similar to the following:


  ```text
  Election Results
  -------------------------
  Total Votes: 369711
  -------------------------
  Charles Casper Stockham: 23.049% (85213)
  Diana DeGette: 73.812% (272892)
  Raymon Anthony Doane: 3.139% (11606)
  -------------------------
  Winner: Diana DeGette
  -------------------------
  ```

In addition, your final script should both print the analysis to the terminal and export a text file with the results.

## Hints and Considerations

* Consider what you've learned so far. You've learned how to import modules like `csv`; to read and write files in various formats; to store contents in variables, lists, and dictionaries; to iterate through basic data structures; and to debug along the way. Using what you've learned, try to break down your tasks into discrete mini-objectives. 

* The datasets for these challenges are quite large. This was done purposefully, as it showcases one of the limits of Excel-based analysis. As data analysts, our first instinct is often to go straight to Excel, but creating scripts in Python can provide us with more robust options for handling big data.

* Write one script for each dataset provided. Run your script separately to make sure that the code works for its respective dataset.

* Feel encouraged to work in groups, but don't shortchange yourself by copying someone else's work. You get what you put in, and the art of programming is extremely unforgiving to those who don't do their own work. 

* Start early, and reach out for help when you need it! Be sure to identify specific questions for your instructors and TAs so that they understand your thought process and can provide targeted guidance.

* Always commit your work and back it up with pushes to GitHub or GitLab. You don't want to lose hours of your work! Also make sure that your repo has a detailed   `README.md` file. 

## Rubric

[Unit 3 Homework Rubric](https://docs.google.com/document/d/1Q5ZnMUD12NvbElOgE3a_lcahuRZdv83aDu9VtXZRiGg/edit?usp=sharing)

- - -

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
