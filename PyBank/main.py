import os
import csv

print(f"Financial Analysis")
print(f"------------------------------")

total_months = 0
month_list = []
money_list = []
total_money = float(0)
percentage_change_list = []
previous_value = float(0)

csvpath = os.path.join("budget_data.csv")

with open(csvpath, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

#  skip the header

    csv_header = next(csv_reader)


    for value in csv_reader:
        total_months += 1
        month_list.append(str(value[0]))
        money_list.append(float(value[1]))


        current_value = value[1]
        change_value = float(current_value) - float(previous_value)
        percentage_change_list.append(change_value)
        previous_value = current_value

total_money = round(sum(money_list))      

def average(percentage_change_list):
    x = len(percentage_change_list)
    total = sum(percentage_change_list) - percentage_change_list[0]
    avg = total / (x - 1)
    return avg

# average change calculation

average_change = round(average(percentage_change_list), 2)


# greatest increase and decrease calculation

greatest_increase = round(max(money_list))
greatest_decrease = round(min(money_list))

highest_index = money_list.index(greatest_increase)
lowest_index = money_list.index(greatest_decrease)
   

print(f"Total: ${total_money}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {month_list[highest_index]} ({greatest_increase})")
print(f"Greatest Decrease in Profits: {month_list[lowest_index]} ({greatest_decrease})")

#print to text file

new_file = open("Budget Analysis.txt", "w")

new_file.write(f"Financial Analysis \n")
new_file.write(f"------------------------------ \n")
new_file.write(f"Total: ${total_money} \n")
new_file.write(f"Average Change: ${average_change} \n")
new_file.write(f"Greatest Increase in Profits: {month_list[highest_index]} ({greatest_increase}) \n")
new_file.write(f"Greatest Decrease in Profits: {month_list[lowest_index]} ({greatest_decrease}) \n")

new_file.close()
   
    
    

