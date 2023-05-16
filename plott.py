from matplotlib import pyplot as plt
import mysql.connector

mydb = mysql.connector.connect(host = "127.0.0.1", user = "root",password = "ankita", auth_plugin='mysql_native_password', database = "Pitch_Perfect")
cur = mydb.cursor()
cur.execute("SELECT name,csv FROM Song WHERE song_id=")
result = cur.fetchall()
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["time", "frequency"]
df = pd.read_csv(path, usecols=columns)
# print("Contents in csv file:", df)
plt.plot(df.time, df.frequency)
plt.axis('off')
# plt.show()
path = "plots\\" + filename[:-4] + ".png"
plt.savefig(path)