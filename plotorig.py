import mysql.connector
from plott import plot
import matplotlib
from matplotlib import pyplot as plt
import pandas as pd

def plot_original(song_id):
    mydb = mysql.connector.connect(host = "127.0.0.1", user = "root",password = "ankita", auth_plugin='mysql_native_password', database = "Pitch_Perfect")
    cur = mydb.cursor()
    cur.execute("SELECT name,csv FROM Song WHERE song_id=%s",(song_id,))
    result = cur.fetchall() 
    
    index = plot()
    path = "D:\\Main Project\\Pitch-Perfect\\csv\\Shape Of You.csv" #result[0][1]
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    columns = ["time", "frequency"]
    df = pd.read_csv(path, usecols=columns)
    plt.plot(df.time[:index+1],df.frequency[:index+1])
    plt.axis('off')
    plt.show()
    # plt.clf()
    path = "D:\\Main Project\\Pitch-Perfect\\plots\\song1.png"
    plt.savefig(path,transparent=True)

if __name__ == '__main__':
    matplotlib.use('TkAgg')
    plot_original()