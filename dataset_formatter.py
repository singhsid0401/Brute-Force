import csv
  
inputfile = csv.reader(open('Predict-The-Data-Scientists-Salary-In-India-Hackathon-Original/Final_Train_Dataset.csv','r'))

count1 = 0
count2 = 0
exp = 0
sal = 0
lst_exp = []
lst_sal = []

for row in inputfile:
    for i in row:
        if 'yrs' in i:
            i = i.replace(' yrs','')
            a = list(map(int, i.split('-')))
            exp = sum(a)/len(a)
            print ('exp ',exp)
            lst_exp.insert(0, exp)
            count1 += 1
        if 'to' in i:
            a = list(map(int, i.split('to')))
            sal = sum(a)/len(a)
            print ('sal ',sal)
            lst_sal.insert(0, sal)
            count2 += 1
        
# zip(lst_exp,lst_sal)   

with open('text.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(zip(lst_exp,lst_sal))     
        
        
    

# print (lst_exp)
# print (lst_sal)
        
        
            
#            count2 += 1
            
# print (count1)
# print (count2)
            
#    print (row)
#    print (type(row))


#f = open('Final_Train_Dataset.csv')
#csv_f = csv.reader(f)

#for row in csv_f:
#       for i in row[1]:
#       print (row[0])