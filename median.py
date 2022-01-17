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
new_data.sort()
if n%2 == 0:
    median1 = float(new_data[n//2 - 1])
    median2 = float(new_data[n//2])
    median = (median1 + median2)/2 
else:
    median = float(new_data[n//2])
print("Median :-"+str(median))