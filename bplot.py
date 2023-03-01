# importing the required modules
import glob
import pandas as pd
from matplotlib import pyplot as plt
import os
import csv

path = "D:\\Main Project\\Dataset\\Data\\genres_original\\hiphop\\csv\\"


plt.tick_params(axis='both', which='major', labelsize=8)

# Iterate over the files in the current directory
for filename in os.listdir(path):
    # Initialize a new set of lists for each file
    timeList = []
    f0List = []
    # Load the file
    with open(path+filename, 'r') as file:
        for row in csv.DictReader(file):
            timeList.append(float(row['time']))
            f0List.append(float(row['frequency']))
        # Add new data to the plots
    plt.plot(timeList, f0List)
    filename = filename[:-13] + '_' + filename[-12:-7]
    output_path = path[:-4] + "plot\\" + filename
    plt.savefig(output_path)
    print("Saved at "+output_path)
    plt.close()
    

#plt.show()
plt.close('all')
