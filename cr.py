import crepe
from scipy.io import wavfile
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
try:
    sr, audio = wavfile.read("audio/adio.wav")
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
f0_data = np.vstack([time, frequency]).transpose()
np.savetxt("csv/adio.fo.csv", f0_data, fmt=['%.3f', '%.3f'], delimiter=',',
header='time,frequency', comments='')

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["time", "frequency"]
df = pd.read_csv("csv/adio.fo.csv", usecols=columns)
# print("Contents in csv file:", df)
plt.plot(df.time, df.frequency)
# plt.show()
plt.savefig('plots/adio-f0.png')