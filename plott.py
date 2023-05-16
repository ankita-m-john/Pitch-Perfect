from matplotlib import pyplot as plt
import pandas as pd
import mysql.connector
import csv

def plot():

    path = "D:\\Main Project\\Pitch-Perfect\\csv\\Shape Of You.csv"
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    columns = ["time", "frequency"]
    df = pd.read_csv(path, usecols=columns)
    max_time = max(df.time)
    index = int(max_time*100 + 2)
    # print("Contents in csv file:", df)
    plt.plot(df.time, df.frequency)
    plt.axis('off')
    # plt.show()
    path = "plots\\song.png"
    plt.savefig(path)   

    mydb = mysql.connector.connect(host = "127.0.0.1", user = "root",password = "ankita", auth_plugin='mysql_native_password', database = "Pitch_Perfect")
    cur = mydb.cursor()
    cur.execute("SELECT name,csv FROM Song WHERE song_id=1")
    result = cur.fetchall() 
    
    index = 20000
    with open(result[0][1]) as fd:
        reader=csv.reader(fd)
        rows = list(reader)
        rows2= rows[:index+1]
    df = pd.DataFrame(rows2, columns = ['Time', 'Frequency'])
    # time = [x for x, y in rows2]
    # frequency = [y for x, y in rows2]
    #print(time)
    # print(frequency)
    # print(df[0])
    plt.plot(df.Time,df.Frequency)
    # plt.axis('off')
    plt.show()
    path = "plots\\song1.png"
    plt.savefig(path)
