#from vocalRange import low_note_f, high_note_f
import pandas as pd

#print(low_note_f,high_note_f)
with open("temp_vr.txt", "r+") as file1:
    # Reading from a file
    low_limit = file1.readline()
    high_limit = file1.readline()

df = pd.read_csv("csv\\Shape Of You.csv")
print(max(df.frequency),min(df.frequency))
if ((abs(high_limit-max(df.frequency))//max(df.frequency))<=1):
    
