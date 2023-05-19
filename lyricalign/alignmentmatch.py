import mysql.connector

def alignmentscore():
    mydb = mysql.connector.connect(host = "127.0.0.1", user = "root",password = "ankita", auth_plugin='mysql_native_password', database = "Pitch_Perfect")
    cur = mydb.cursor()
    cur.execute("SELECT name,lrc FROM Song WHERE song_id=1")
    result = cur.fetchall() 
    file1 = open(result[0][1],'r')
    file2 = open("D:\\Main Project\\Pitch-Perfect\\lyricalign\\output.txt",'r') 

    file1_lines = file1.readlines()
    file2_lines = file2.readlines()
    count = 0   

    for i in range(len(file2_lines)):
        L1 = file1_lines[i].split('\t')
        L2 = file2_lines[i].split('\t')
        t1 = float(L1[0])
        t2 = float(L2[0])
        if ((t1-1) <= t2) and (t2<=(t1+1)):
            count = count + 1
    print("Match percentage: {:.2f}".format((count/(i+1))*100)) 

    file1.close()
    file2.close()

if __name__ == '__main__':
    alignmentscore()