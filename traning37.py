import pandas as pd
import math
import sys
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('prog4Data.xlsx')

training_rows = int(sys.argv[1])

testing_rows = int(sys.argv[2])
if sys.argv[3] == "~v":
    verbose = True
else:
    verbose = False
a1_list = [[0]*3 for i in range(4)]
a2_list = [[0]*3 for i in range(4)]
a3_list = [[0]*3 for i in range(4)]
a4_list = [[0]*3 for i in range(4)]
a5_list = [[0]*3 for i in range(4)]
a6_list = [0]*3
accuracy = 0
Q = 0
R = 0
Q_R = 0

for i in range(training_rows):
    a1 = df["a1"][i]
    a2 = df["a2"][i]
    a3 = df["a3"][i]
    a4 = df["a4"][i]
    a5 = df["a5"][i]
    a6 = df["a6"][i]
    a1_list[a1-1][a6-1] += 1
    a2_list[a2-1][a6-1] += 1
    a3_list[a3-1][a6-1] += 1
    a4_list[a4-1][a6-1] += 1
    a5_list[a5-1][a6-1] += 1
    a6_list[a6-1] += 1
    

for j in range(1000-testing_rows,1000,1):
    a1 = df["a1"][j]
    a2 = df["a2"][j]
    a3 = df["a3"][j]
    a4 = df["a4"][j]
    a5 = df["a5"][j]
    a6 = df["a6"][j]
    min_log = 999999
    a6_label = 0
    for k in range(3):
        
        a1_a6 = (a1_list[a1-1][k]+.1)/(a6_list[k]+.4)
        a2_a6 = (a2_list[a2-1][k]+.1)/(a6_list[k]+.4)
        a3_a6 = (a3_list[a3-1][k]+.1)/(a6_list[k]+.4)
        a4_a6 = (a4_list[a4-1][k]+.1)/(a6_list[k]+.4)
        a5_a6 = (a5_list[a5-1][k]+.1)/(a6_list[k]+.4)
        lp_a6 = (a6_list[k]+.1)/(training_rows + .3)
        lp_1 = math.log(2,a1_a6)
        lp_2 = math.log(2,a2_a6)
        lp_3 = math.log(2,a3_a6)
        lp_4 = math.log(2,a4_a6)
        lp_5 = math.log(2,a5_a6)
        lp_6 = math.log(2,lp_a6)
        #print("terms")
        #print(a1_list[a1-1][k]+.1)
        #print(a6_list[k]+.4)
        #print("This is the negative log")
        #print(math.log(2,a1_list[a1-1][k]+.1) - math.log(2,a6_list[k]+.4))
        #print(math.log(2,1/a1_a6))
        #print(1/math.log(2,1/a1_a6))
        
        
        log_sum = lp_1 + lp_2 + lp_3 + lp_4 +lp_5 + lp_6
        if log_sum < min_log:
            min_log = log_sum
            a6_label = k+1
    if a6_label == a6:
        accuracy +=1
        
    if a6_label == 3:
        Q += 1
    
    if a6 == 3:
        R += 1
        
    if a6 == 3 and a6_label == 3:
        Q_R += 1
final_accuracy = accuracy / testing_rows
if Q != 0:
    precision = Q_R/Q
else:
    precision = 0
if R != 0:
    recall = Q_R/R

else:
    recall = 0

print("Accuracy =",final_accuracy,"Precision = ",precision, "Recall = ",recall)
a61 = (a6_list[0]+.1)/(training_rows + .3)
a62 = (a6_list[1]+.1)/(training_rows + .3)
a63 = (a6_list[2]+.1)/(training_rows + .3)
print(1/math.log(2,1/a61), 1/math.log(2,1/a62), 1/math.log(2,1/a63))

if verbose == True:
    all_array = [[0]*4 for i in range(15)] 
    for l in range(4):
        for n in range(3):
            a1 = a1_list[l][n]
            a2 = a2_list[l][n]
            a3 = a3_list[l][n]
            a4 = a4_list[l][n]
            a5 = a5_list[l][n]
            a6 = a6_list[n]
            a1_a6 = (a1+.1)/(a6+.4)
            a2_a6 = (a2+.1)/(a6+.4)
            a3_a6 = (a3+.1)/(a6+.4)
            a4_a6 = (a4+.1)/(a6+.4)
            a5_a6 = (a5+.1)/(a6+.4)
            lp_a6 = (a6+.1)/(training_rows + .3)
            all_array[n][l] = 1/math.log(2,1/a1_a6)
            all_array[n+3][l] = 1/math.log(2,1/a2_a6)
            all_array[n+6][l] = 1/math.log(2,1/a3_a6)
            all_array[n+9][l] = 1/math.log(2,1/a4_a6)
            all_array[n+12][l] = 1/math.log(2,1/a5_a6)


for i in range(15):
    print(all_array[i])
            
            
            



        
