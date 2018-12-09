import os
import csv

candidate = {}

print ("Election Resuls")
print ("--------------------------")

# read the csv file 
                              
election_data = os.path.join("election_data.csv")
with open(election_data, newline="") as csvfile:
  csvreader = csv.reader (csvfile, delimiter=",")
  next (csvreader)  

  for row in csvreader:       
    if row[2] in candidate:  
      candidate[row[2]] += 1 
    else:                    
      candidate[row[2]] = 1  
total_votes = csvreader.line_num - 1

print ("Total Votes: " + str(total_votes))
print ("--------------------------")
                                      
#output each candidte with the percentage won and number of votes 

for key, value in candidate.items(): 
                                      
  print (key + ": " + "{0:.3f}%".format(value/total_votes * 100) + " (" + str(value) + ")")
 
# print the winner
print ("--------------------------") 
print ("Winner: " + max(candidate, key=candidate.get) ) 
print ("--------------------------") 

new_file = open("Election_Results", "w")

new_file.write(f"Election Results\n")
new_file.write(f"------------------------------\n")
new_file.write("Total Votes: " + str(total_votes) + "\n")
new_file.write(f"------------------------------\n")
for key, value in candidate.items():                                     
  new_file.write(key + ": " + "{0:.3f}%".format(value/total_votes * 100) + " (" + str(value) + ")\n")
new_file.write("Winner: " + max(candidate, key=candidate.get)+ "\n") 
new_file.write("--------------------------\n")

new_file.close()
