import os
import csv
pybank_csv = os.path.join("Resources","budget_data.csv")
total_month=0
total_profitloss=0.0
change=0
net_changelist=[]
monthofchange=[]
greatest_increase= ['',0]
greatest_decrease= ['',9999999999]
with open(pybank_csv) as csvfile:
    # csvreader = csv.reader(csvfile,delimiter= ",")
    # csv_header=next(csvfile)
    # print(f"CSV Header: {csv_header}")
    reader= csv.reader(csvfile)   
    header= next(reader)
    firstrow=next(reader)
    total_month = total_month+1 
    total_profitloss=total_profitloss+int(firstrow[1])
    print(total_profitloss)
    previous_net=int(firstrow[1])
    for row in reader:
        total_month = total_month+1 
        total_profitloss=total_profitloss+int(row[1])
        change=int(row[1])-previous_net
        previous_net=int(row[1])
        net_changelist= net_changelist+[change]
        monthofchange= monthofchange+[row[0]]
        if change > greatest_increase[1]:
            greatest_increase[0]=row[0]
            greatest_increase[1]=change
        if change < greatest_decrease[1]:
            greatest_decrease[0]=row[0]
            greatest_decrease[1]=change

averagechange=sum(net_changelist)/len(net_changelist)
print('Financial Analysis')
print('---------------------------')
print(total_month)
print(total_profitloss)
print(round(averagechange,2))
print(greatest_increase[0],(greatest_increase[1]))
print(greatest_decrease[0],(greatest_decrease[1]))

output_path=os.path.join("Analysis","output.csv")
with open(output_path,"w") as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['---------------------------'])
    csvwriter.writerow(['Total Month:'+str(total_month)])
    csvwriter.writerow(['Total Profit/loss:'+str(total_profitloss)])
    csvwriter.writerow(['Average change:'+'$'+str(round(averagechange,2))])
    csvwriter.writerow(['Greatest Increase in Profit:'+str(greatest_increase[0])+'($'+str(greatest_increase[1])+')'])
    csvwriter.writerow(['Greatest Decrease in Profit:'+str(greatest_decrease[0])+'($'+str(greatest_decrease[1])+')'])




