# from vocalRange import vocalRange
from cr import pitch_detect
from plotorig import plot_original
from songrec import songrec
import sys
sys.path.insert(1,'D:\\Main Project\\Pitch-Perfect\\lyricalign')
from alignmentmatch import alignmentscore
import mysql.connector
import subprocess
import torch.nn as nn
import argparse
import tkinter
sys.path.insert(1,'D:\\Main Project\\Pitch-Perfect\\audiotool-main')
from main import record
from pydub import AudioSegment

parser = argparse.ArgumentParser()
parser.add_argument('song_id', help='')
args = parser.parse_args()

mydb = mysql.connector.connect(host = "127.0.0.1", user = "root",password = "ankita", auth_plugin='mysql_native_password', database = "Pitch_Perfect")
cur = mydb.cursor()
class SiameseNetwork(nn.Module):
    def __init__(self):
        super(SiameseNetwork, self).__init__()
        print("Alia5")
        self.reflection_pad = nn.ReflectionPad2d(1)
        self.conv1 = nn.Conv2d(1, 4, kernel_size=3)
        self.conv2 = nn.Conv2d(4, 8, kernel_size=3)
        self.conv3 = nn.Conv2d(8, 8, kernel_size=3) 
        self.relu = nn.ReLU(inplace=True)
        self.batch_norm1 = nn.BatchNorm2d(4)
        self.batch_norm2 = nn.BatchNorm2d(8) 
        self.fc1 = nn.Linear(8 * 100 * 100, 500)
        self.fc2 = nn.Linear(500, 500)
        self.fc3 = nn.Linear(500, 5)
        
    def forward_one_branch(self, x):
        x = self.batch_norm1(self.relu(self.conv1(self.reflection_pad(x))))
        x = self.batch_norm2(self.relu(self.conv2(self.reflection_pad(x))))        
        x = self.batch_norm2(self.relu(self.conv3(self.reflection_pad(x))))   
        x = x.view(x.size()[0], -1)
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))        
        x = self.fc3(x)
        
        return x
        
    def forward(self, input1, input2):
        output1 = self.forward_one_branch(input1)
        output2 = self.forward_one_branch(input2)     
        
        return output1, output2
    
if False:
    # vocal_range()
    print("Nope")

else:
    record() #get recording from ui and store as audio/song.mp3
    AudioSegment.from_mp3("D:\\Main Project\\music-player-with-lyrics-synchronization-musixmatch\\audio\\song.wav").export("D:\\Main Project\\music-player-with-lyrics-synchronization-musixmatch\\audio\\song.mp3", format="mp3")
    r = subprocess.run(["demucs","D:\\Main Project\\music-player-with-lyrics-synchronization-musixmatch\\audio\\song.wav"])  #performs audio source separation on song.mp3  
    # print("Alia1")
    
    # AudioSegment.from_mp3("D:\\Main Project\\music-player-with-lyrics-synchronization-musixmatch\\audio\\song.wav").export("D:\\Main Project\\music-player-with-lyrics-synchronization-musixmatch\\audio\\song.mp3", format="mp3")  
    # print("Alia2")
    
    pitch_detect() #detects pitch and stores csv files as song.csv  
    # print("Alia2")

    plot_original(args.song_id,)  #needs fixing and change paths later gives plots of original (song.png) and user songs (song1.png)  
    # print("Alia3")

    cur.execute("SELECT song_id,mp3,lyrics FROM Song WHERE song_id = %s",(args.song_id,))
    result = cur.fetchall()
    r = subprocess.run(["py","lyricalign/go.py",result[0][1],result[0][2],"D:\\Main Project\\Pitch-Perfect\\lyricalign\\output.txt"]) #change lyric alignment input aligns user's song with original lyrics
    
    alignscore = alignmentscore(args.song_id,) #matches user song's aligned lyrics to the originals song's and generates a percentage match
    # print("Alia4")

    Score, target, name = songrec() # runs snn code to get percentage of match between song.png and song1.png
              # Generates user score and recommends songs based on total scores 
    
    # print("Alia5")
    # Import the tkinter module
    
    # Creating the GUI window.
    window = tkinter.Tk()
    window.title("Scores")
    window.geometry("800x1000")
    
    # Creating our text widget.
    sample_text = tkinter.Entry(window)
    sample_text.pack()
    sample_text1 = tkinter.Entry(window)
    sample_text1.pack()
    sample_text2 = tkinter.Entry(window)
    sample_text2.pack()
    sample_text3 = tkinter.Entry(window)
    sample_text3.pack()
    # Creating the function to set the text
    # with the help of button
    def set_text_by_button():
    
        # Delete is going to erase anything
        # in the range of 0 and end of file,
        # The respective range given here
        sample_text.delete(0,"end")
        sample_text1.delete(0,"end")
        sample_text2.delete(0,"end")
        sample_text3.delete(0,"end")

        # Insert method inserts the text at
        # specified position, Here it is the
        # beginning
        sample_text.insert(0,"Pitch Similarity: {:.2f}".format(Score))
        sample_text1.insert(0, "Alignment: {:.2f}".format(alignscore))
        sample_text2.insert(0, "User Score: {:}".format(target))
        sample_text3.insert(0, name)
    # Setting up the button, set_text_by_button()
    # is passed as a command
    set_up_button = tkinter.Button(window, height=1, width=10, text="Set",
                        command=set_text_by_button)
    
    set_up_button.pack()
    
    window.mainloop()
