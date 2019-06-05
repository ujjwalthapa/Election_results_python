# Your task is to create a Python script that analyzes the records to calculate each of the following:

#Importing operating software and csv module
import os
import csv 

#Creating lists 
dates = []
profit = []

#Declaring variable value
total_profit = 0

#Set path for the csv file
csvpath = "../Resources/budget_data.csv"

#Open the CSV file
with open(csvpath, mode= 'r', newline =  '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
#for loop to create a new variable row_list
    next(csvreader)
    for row in csvreader:
        row_list= list(row)
        
        dates.append(row_list[0])
        profit.append(int(row_list[1]))
#print(sum(profit))



#print the total for dates. Minues 1 as the first row is a header. Print = count (total dates -1 (for header))
print(len(dates))

#Calculating total profit. First declated a new variable x who range startes from 1 and I put len(profit)-1 as the first column is classified as ) in Python
#Then, I convert profit into integer and increase the running total for total_profit and print total profit.

for x in range(0,len (profit)):
    total_profit = int(profit[x]) + total_profit
print (total_profit)

#Calculating average using total_profit and dividing my profit entries on the .csv
average_change = total_profit/(len(profit))
print(average_change)

# Declared two variables max and min. Used the range loop of line 31. Than if the profit is gretaer that the previous profit value, print the new profit value 
# as specfied. Same rule has been applied for minumum as well.
max =0
min=0
for x in range(1, len(profit)-1):
    if int(profit[x]) > max:
        max= int(profit[x])

for x in range(1, len(profit)-1):
    if int(profit[x]) < min:
        min= int(profit[x])

print (max)
print (min)


