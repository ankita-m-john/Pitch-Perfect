# from demuc import demuc
from cr import pitch_detect
from plotorig import plot_original
from songrec import songrec
# from vocalRange import vocalRange
# from lyricalignment import align
import sys
sys.path.insert(1,'D:\\Main Project\\Pitch-Perfect\\lyricalign')
from alignmentmatch import alignmentscore
import mysql.connector
# from pydub import AudioSegment
import subprocess

mydb = mysql.connector.connect(host = "127.0.0.1", user = "root",password = "ankita", auth_plugin='mysql_native_password', database = "Pitch_Perfect")
cur = mydb.cursor()

if False:
    # vocal_range()
    print("Nope")

else:
    #get recording from ui and store as audio/song.mp3
    r = subprocess.run(["demucs","audio\\song.mp3"])  #performs audio source separation on song.mp3  
    print("Alia1")
    
    # AudioSegment.from_mp3("separated/htdemucs/song/vocals.mp3").export("audio/song.wav", format="wav")  
    # print("Alia2")
    
    pitch_detect() #detects pitch and stores csv files as song.csv  
    print("Alia3")

    plot_original()  #needs fixing and change paths later gives plots of original (song.png) and user songs (song1.png)  
    print("Alia4")

    cur.execute("SELECT song_id,mp3,lyrics FROM Song WHERE song_id = 1")
    result = cur.fetchall()
    r = subprocess.run(["py","lyricalign/go.py",result[0][1],result[0][2],"lyricalign/output.txt"]) #change lyric alignment input aligns user's song with original lyrics
    alignmentscore() #matches user song's aligned lyrics to the originals song's and generates a percentage match
    print("Alia5")

    songrec() # runs snn code to get percentage of match between song.png and song1.png
              # Generates user score and recommends songs based on total scores 
    print("Alia6")
