import csv
from collections import Counter

with open("C-104HW.csv", newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

#finding the mean
n = len(new_data)
total = 0
for x in new_data:
    total+=x
mean = total/n
print("The mean is " + str(mean))

#finding the median
n = len(new_data)
new_data.sort()
if n%2 == 0:
    med1 = float(new_data[n//2])
    med2 = float(new_data[n//2-1])
    median = (med1+med2)/2
else:
    median = new_data[n//2]
    print(n)
print("The median is " + str(median))

#finding mode
data = Counter(new_data)
mode_for_range = {
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0,
}
for height, occurrence in data.items():
    if 75 < float(height) < 85:
        mode_for_range["75-85"]+=occurrence
    elif 85 < float(height) < 95:
        mode_for_range["85-95"]+=occurrence
    elif 95 < float(height) < 105:
        mode_for_range["95-105"]+=occurrence
    elif 105 < float(height) < 115:
        mode_for_range["105-115"]+=occurrence
    elif 115 < float(height) < 125:
        mode_for_range["115-125"]+=occurrence
    elif 125 < float(height) < 135:
        mode_for_range["125-135"]+=occurrence
    elif 135 < float(height) < 145:
        mode_for_range["135-145"]+=occurrence
    elif 145 < float(height) < 155:
        mode_for_range["145-155"]+=occurrence
    elif 155 < float(height) < 165:
        mode_for_range["155-165"]+=occurrence
    elif 165 < float(height) < 175:
        mode_for_range["165-175"]+=occurrence
mode_range, mode_ocurrence = 0,0
for range, occurrence in mode_for_range.items():
    if occurrence > mode_ocurrence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurrence 
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"The mode is {mode:2f}")