from demuc import demuc
from cr import pitch_detect
from plott import plot
from songrec import songrec
from vocalRange import vocalrange
from alignmentmatch import alignmentscore
from pydub import AudioSegment

if False:
    vocal_range()

else:
    #get recording from ui and store as audio/song.mp3
    demuc()  #performs audio source separation on song.mp3  

    AudioSegment.from_mp3("audio/song.mp3").export("audio/song.wav", format="wav")  

    pitch_detect() #detects pitch and stores csv files as song.csv  

    plot()  #needs fixing and change paths later gives plots of original (song.png) and user songs (song1.png)  

    #add lyric alignment here
    alignmentscore() #matches user song's aligned lyrics to the originals song's and generates a percentage match

    songrec() # runs snn code to get percentage of match between song.png and song1.png
              # Generates user score and recommends songs based on total scores 

