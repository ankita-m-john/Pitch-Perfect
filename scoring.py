#from vocalRange import low_note_f, high_note_f
import pandas as pd

#print(low_note_f,high_note_f)
with open("temp_vr.txt", "r+") as file1:
    # Reading from a file
    low_limit = float(file1.readline())
    high_limit = float(file1.readline())

df = pd.read_csv("csv\\Shape Of You.csv")
print(max(df.frequency),min(df.frequency))
D = {1: 1000, 2:1100, 3:}
for i in range(101): D[i] = L[i]
#((abs(high_limit-max(df.frequency))//max(df.frequency))<=1):

