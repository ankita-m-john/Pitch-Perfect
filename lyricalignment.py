import os
import mysql.connector
def align():
    mydb = mysql.connector.connect(host = "127.0.0.1", user = "root",password = "ankita", auth_plugin='mysql_native_password', database = "Pitch_Perfect")
    cur = mydb.cursor()
    cur.execute("SELECT song_id,lyrics,lrc FROM Song")
    result = cur.fetchall()
    os.system('cmd /k "py lyricalign/go.py lyricalign/example_data/Muse.GuidingLight.mp3 lyricalign/example_data/Muse.GuidingLight.txt lyricalign/output.txt"')

if __name__=="__main__":
    align()