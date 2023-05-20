import crepe
from scipy.io import wavfile
# import os
import numpy as np
# import pandas as pd
# from matplotlib import pyplot as plt
import sys
def pitch_detect():
    path = "D:\\Main Project\\Pitch-Perfect\\separated\\htdemucs\\The Gambler\\vocals.wav"
    try:
        sr, audio = wavfile.read(path)
    except ValueError:
        print("CREPE: Could not read The Gambler", file=sys.stderr)
        raise
    time, frequency, confidence, activation = crepe.predict(audio, sr, viterbi=True)
    #f0_file = output_path("adio", ".f0.csv","csv\/")
    path= "csv\\The Gambler.csv"
    f0_data = np.vstack([time, frequency]).transpose()
    np.savetxt(path, f0_data, fmt=['%.3f', '%.3f'], delimiter=',',
    header='time,frequency', comments='')

if __name__ == '__main__':
    pitch_detect()