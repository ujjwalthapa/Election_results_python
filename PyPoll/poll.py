
#Importing operating software and csv module
import os
import csv 

#Creating lists 
voter_id = list()
candidate = list()
county = list()
 

#Declaring variable value
total_profit = 0

#Set path for the csv file
csvpath = "../Resources/election_data.csv"

#Open the CSV file
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
#for loop to create a new variable row_list
    next(csvreader)
    for row in csvreader:
        row_list= list(row)
        
        voter_id.append(row_list[0])
        candidate.append(row_list[2])
        county.append(row_list[1])
    
total_vote = (len(voter_id))


candidate_set = set(candidate)
print(candidate_set)

khan_count = (candidate.count('Khan'))
correy_count = (candidate.count('Correy'))
li_count = (candidate.count('Li'))
otooley_count = (candidate.count('O\'Tooley'))
print (otooley_count)
print (khan_count)
print (li_count)


print (total_vote)

print('Khan: '+ str((khan_count/total_vote)*100)+ '% ('+str(khan_count)+')')
#print('Khan: %.3f\% (%d)'%(((khan_count/total_vote)*100),khan_count))

print('Correy: '+ str((correy_count/total_vote)*100)+ '% ('+str(correy_count)+')')

print('Li: '+ str((li_count/total_vote)*100)+ '% ('+str(li_count)+')')

print('O\'Tooley: '+ str((otooley_count/total_vote)*100)+ '% ('+str(otooley_count)+')')

print ("Winner: Khan")


'''
#Election Results
#-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
'''


#In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)


#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:



#The total number of votes cast


#A complete list of candidates who received votes


#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.




