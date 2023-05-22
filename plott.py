from matplotlib import pyplot as plt
import pandas as pd


def plot():

    path = "D:\\Main Project\\Pitch-Perfect\\csv\\song.csv"
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    columns = ["time", "frequency"]
    df = pd.read_csv(path, usecols=columns)
    max_time = max(df.time)
    index = int(max_time*100 + 2)
    # print("Contents in csv file:", df)
    plt.plot(df.time, df.frequency)
    plt.axis('off')
    plt.show()
    path = "D:\\Main Project\\Pitch-Perfect\\plots\\song.png"
    plt.savefig(path,transparent=True)   
    plt.close()
    return(index)
    
if __name__ == '__main__':
    i = plot()