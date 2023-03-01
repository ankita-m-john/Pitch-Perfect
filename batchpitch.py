# importing the required modules
import glob
import pandas as pd
from matplotlib import pyplot as plt


# specifying the path to csv files
path = "D:\\Main Project\\Dataset\\Data\\genres_original\\classical\\csv"
  
# csv files in the path
files = glob.glob(path + "/*.csv")
  
# defining an empty list to store 
# content
data_frame = pd.DataFrame()
content = []

plt.rcParams["figure.figsize"] = [18.00, 18.00]
plt.rcParams["figure.autolayout"] = True
columns = ["time", "frequency"]
#directory = "D:\\Main Project\\Dataset\\Data\\genres_original\\classical\\plots\\"
# checking all the csv files in the 
# specified path
for filename in files:
    #filepath = directory + filename + '.png'
    # reading content of csv file
    # content.append(filename)
    df = pd.read_csv(filename, usecols=columns)
    plt.plot(df.time, df.frequency)
    filename = filename[:-13] + '_' + filename[-12:-7]
    plt.savefig(filename)
#    content.append(df)
# print("Contents in csv file:", df)
# converting content to data frame
#data_frame = pd.concat(content)
#print(data_frame)