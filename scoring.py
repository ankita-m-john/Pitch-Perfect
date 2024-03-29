#from vocalRange import low_note_f, high_note_f
import pandas as pd
import mysql.connector

def Total_Score():
    mydb = mysql.connector.connect(host = "127.0.0.1", user = "root",password = "ankita", auth_plugin='mysql_native_password', database = "Pitch_Perfect")
    cur = mydb.cursor()
    cur.execute("SELECT low_note,high_note FROM User WHERE user_id=1") #userid match
    result = cur.fetchall()
    low_limit = result[0][0]
    high_limit = result[0][1]
    cur.execute("SELECT song_id,name,csv FROM Song") #userid match
    result = cur.fetchall()
    #print(low_note_f,high_note_f)
    # with open("temp_vr.txt", "r+") as file1:
    #     # Reading from a file
    #     low_limit = float(file1.readline())
    #     high_limit = float(file1.readline())  
    for i in range(8):
        df = pd.read_csv("D:\\Main Project\\Pitch-Perfect\\csv\\"+result[i][1]+".csv")
        print(max(df.frequency),min(df.frequency), high_limit, low_limit)   

        D = {i:1000 + 100*i for i in range(101)}
        x = ((abs(high_limit-max(df.frequency))/max(df.frequency))*100)
        # if x in D:
        #     print(x,D[x])
        y = ((abs(low_limit-min(df.frequency))/min(df.frequency))*100)
        # print(x,1000+100*x)
        # print(y,1000+100*y)
        Total_score = 1000+100*x+100*y
        print(round(Total_score))
        song_id = 8 #match song id
        sql = "UPDATE Scoring SET Total_Score = %s WHERE user_id = 1 and song_id = %s"
        # fp = open("temp_vr.txt",'w')
        L = (Total_score,result[i][0])
        cur.execute(sql,L)
        mydb.commit()
        # print(cur.rowcount,"Record inserted.") 
if __name__ == "__main__":
    Total_Score()