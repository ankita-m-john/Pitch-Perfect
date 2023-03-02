import crepe
from scipy.io import wavfile
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
filename = input("Enter file name: ")
path = "audio\\" + filename
try:
    sr, audio = wavfile.read(path)
except ValueError:
    print("CREPE: Could not read %s" % file, file=sys.stderr)
    raise
# def output_path(file, suffix, output_dir):
#     """
#     return the output path of an output file corresponding to a wav file
#     """
    #path = re.sub(r"(?i).wav$", suffix, file)
    # if output_dir is not None:
    #     path = os.path.join(output_dir, os.path.basename("csv/"))
    # return path
time, frequency, confidence, activation = crepe.predict(audio, sr, viterbi=True)
#f0_file = output_path("adio", ".f0.csv","csv\/")
path= "csv\\" + filename[:-4] + ".csv"
f0_data = np.vstack([time, frequency]).transpose()
np.savetxt(path, f0_data, fmt=['%.3f', '%.3f'], delimiter=',',
header='time,frequency', comments='')

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["time", "frequency"]
df = pd.read_csv(path, usecols=columns)
# print("Contents in csv file:", df)
plt.plot(df.time, df.frequency)
# plt.show()
path = "plots\\" + filename[:-4] + ".png"
plt.savefig(path)