# importing the required modules
import glob
import pandas as pd
from matplotlib import pyplot as plt


# specifying the path to csv files
path = "D:\\Main Project\\Data\\genres_original\\blues\\csv"
  
# csv files in the path
files = glob.glob(path + "/*.csv")
  
# defining an empty list to store 
# content
data_frame = pd.DataFrame()
content = []

plt.rcParams["figure.figsize"] = [18.00, 18.00]
plt.rcParams["figure.autolayout"] = True
columns = ["time", "frequency"]

# checking all the csv files in the 
# specified path
for filename in files:
    
    # reading content of csv file
    # content.append(filename)
    df = pd.read_csv(filename, usecols=columns)
    plt.plot(df.time, df.frequency)
    plt.savefig("D:\\Main Project\\Data\\genres_original\\blues\\plots\\"+filename+".png")
#    content.append(df)
# print("Contents in csv file:", df)
# converting content to data frame
#data_frame = pd.concat(content)
#print(data_frame)