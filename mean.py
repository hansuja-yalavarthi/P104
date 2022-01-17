import csv
with open ('data.csv') as f:
    reader = csv.reader(f)
    file_data = list(reader)
from collections import Counter
file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(n_num)
n = len(new_data)
total = 0 
for x in new_data:
    total=float(total)+float(x)
mean= total/n
print("Mean:-"+str(mean))