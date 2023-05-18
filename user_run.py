from demuc import demuc
from cr import pitch_detect
from plotorig import plot_original
from songrec import songrec
from vocalRange import vocalrange
from lyricalignment import align
import sys
sys.path.insert(1,'D:\\Main Project\\Pitch-Perfect\\lyricalign')
from alignmentmatch import alignmentscore
from pydub import AudioSegment

if False:
    vocal_range()

else:
    #get recording from ui and store as audio/song.mp3
    demuc()  #performs audio source separation on song.mp3  

    # AudioSegment.from_mp3("audio/song.mp3").export("audio/song.wav", format="wav")  

    pitch_detect() #detects pitch and stores csv files as song.csv  

    plot_original()  #needs fixing and change paths later gives plots of original (song.png) and user songs (song1.png)  

    align() #change lyric alignment input aligns user's song with original lyrics
    alignmentscore() #matches user song's aligned lyrics to the originals song's and generates a percentage match

    songrec() # runs snn code to get percentage of match between song.png and song1.png
              # Generates user score and recommends songs based on total scores 

