import os
import csv

total_months = 0
total_value = 0
previous = 0
diff = [] #creating to save "3rd" column to hold the difference
change = []
change = 0
Averagediff = 0
date = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999]



csvpath = os.path.join("C:/Users/kyran/OneDrive/Documents/Python_HW/budget_data.csv")

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    next(csv_reader)

    for row in csv_reader:
        #total months included in dataset
        total_months = total_months + 1


        #for collecting the greatest increase and decrease date
        date.append(row[0])

        #total amount of profit/losses over the period
        total_value = total_value + int(row[1])
        change = int(row[1])-previous #subtracting profit/loss 
        previous = int(row[1])
        diff.append(change) #diff is being pushed to the list to be saved
        length = len(diff) - 1
        date=date + [row[0]]

        #greatest increase/decrease in profits over the period
        if(change>greatest_increase[1]):
            greatest_increase[1]=change
            greatest_increase[0]=row[1]
        if(change<greatest_decrease[1]):
            greatest_decrease[0]=row[1]
            greatest_decrease[1]=change
     


    #average of the changes in profit/losses over the period    
    Averagediff = sum(diff[1:])/length      


    #print total months, total profit/losses, and average change
    print("----------------------------------------------------------")
    print("Fiancial Analysis")
    print("----------------------------------------------------------")

    print("Total Months: " + str(total_months))  
    print("Total: $" +str(total_value))
    print("Average Change: $", (Averagediff, 2))
    print("Greatest Increase in Profits:" + str(date[0]), "$" + str(greatest_increase[1]))
    print("Greatest Decrease in Profits:" + str(date[0]), "$" + str(greatest_decrease[1]))
    print("----------------------------------------------------------")

     #print total months, total profit/losses, and average change to document
    
    new_line = "\n"
     #print total months, total profit/losses, and average change to document
    text_file = open('pybank_financial_analysis.txt', 'w')
    text_file.write("----------------------------------------------------------")
    text_file.write(new_line)
    text_file.write("Fiancial Analysis")
    text_file.write(new_line)
    text_file.write("----------------------------------------------------------")
    text_file.write(new_line)
    text_file.write("Total Months: " + str(total_months))  
    text_file.write(new_line)
    text_file.write("Total: $" +str(total_value))
    text_file.write(new_line)
    text_file.write("Average Change: $" + str(round(Averagediff,2)) )
    text_file.write(new_line)
    #                                                      This should be a date
    text_file.write("Greatest Increase in Profits:" + str(date[0]) + "($ " + str(greatest_increase[1]) + ")")
    text_file.write(new_line)
    text_file.write("Greatest Decrease in Profits:" + str(date[0]) +  "($ " + str(greatest_decrease[1]) + ")")
    text_file.write(new_line)
    text_file.write("----------------------------------------------------------")
    
    text_file.close()



    
 
        
