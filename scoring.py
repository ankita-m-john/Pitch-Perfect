#from vocalRange import low_note_f, high_note_f
import pandas as pd

#print(low_note_f,high_note_f)
with open("temp_vr.txt", "r+") as file1:
    # Reading from a file
    low_limit = float(file1.readline())
    high_limit = float(file1.readline())

df = pd.read_csv("csv\\Shape Of You.csv")
print(max(df.frequency),min(df.frequency), high_limit, low_limit)

D = {i:1000 + 100*i for i in range(101)}
x = ((abs(high_limit-max(df.frequency))/max(df.frequency))*100)
# if x in D:
#     print(x,D[x])
y = ((abs(low_limit-min(df.frequency))/min(df.frequency))*100)
# print(x,1000+100*x)
# print(y,1000+100*y)
Total_score = 1000+100*x+100*y
print(round(Total_score))