import os
import csv
import numpy as np
Pypoll_csv = os.path.join("Resources","election_data.csv")
dataArray=[]
with open(Pypoll_csv) as csvfile:
    reader=  csv.reader(csvfile, delimiter=',') 
    header= next(reader)
    firstrow=next(reader)
    line_count=0
    votes=[]
    candidates=[]
    for row in reader:
        votes.append(row[0])
        candidates.append(row[2])

    Correy_total = 0
    Khan_total = 0
    Li_total = 0
    OTooley_total = 0
    print(votes[0])
    for i in range(len(candidates)):
        if candidates[i] == 'Correy':
            Correy_total+=1
        elif candidates[i] == 'Khan':
            Khan_total+=1
        elif candidates[i]== 'Li':
            Li_total+=1
        else:
            OTooley_total+=1
res_array = [Correy_total, Khan_total, Li_total, OTooley_total]
res_names = ['Correy', 'Khan', 'Li', 'O\'Tooley']
result = np.where(res_array == np.amax(res_array))
winner = res_names[int(result[0][0])]
print('Election Results')
print('---------------------------')
print('Total Votes: '+str(len(votes)))
print('---------------------------')
print('Khan: '+format((Khan_total*100)/len(candidates),".3f") +'% ('+str(Khan_total)+')')
print('Correy: '+format((Correy_total*100)/len(candidates),".3f") +'% ('+str(Correy_total)+')')
print('Li: '+ format((Li_total*100)/len(candidates),".3f") +'% ('+str(Li_total)+')')
print('O\'Tooley: '+format((OTooley_total*100)/len(candidates),".3f") +'% ('+str(OTooley_total)+')')
print('---------------------------')
print('Winner: ' + winner)
print('---------------------------')

output_path = os.path.join("Analysis", "election_result.csv")
with open(output_path,'w') as csvfile:
    csvwriter= csv.writer(csvfile)
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['---------------------------'])
    csvwriter.writerow(['Total Votes: '+str(len(votes))])
    csvwriter.writerow(['---------------------------'])
    csvwriter.writerow(['Khan: '+format((Khan_total*100)/len(candidates),".3f") +'% ('+str(Khan_total)+')'])
    csvwriter.writerow(['Correy: '+format((Correy_total*100)/len(candidates),".3f") +'% ('+str(Correy_total)+')'])
    csvwriter.writerow(['Li: '+ format((Li_total*100)/len(candidates),".3f") +'% ('+str(Li_total)+')'])
    csvwriter.writerow(['O\'Tooley: '+format((OTooley_total*100)/len(candidates),".3f") +'% ('+str(OTooley_total)+')'])
    csvwriter.writerow(['---------------------------'])
    csvwriter.writerow(['Winner: ' + winner])
    csvwriter.writerow(['---------------------------'])
