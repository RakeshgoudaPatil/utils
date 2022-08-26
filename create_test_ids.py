import csv

row_list = []  
row_list.append(['userId']) 
for i in range(100):
        val=100000+i
        row_list.append(['Demofghijklmnopqr'+str(val)])

with open('Test_01.csv', 'w', newline ='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)
