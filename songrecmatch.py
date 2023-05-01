import pandas as pd
from vocalrange import q, get_current_note
from threading import Thread

print("Sing a Low Note: ")

t = Thread(target=get_current_note)
t.daemon = True
t.start()

low_note = ""
high_note = ""
have_low = False
have_high = True
ch = 'y'

noteHoldLength = 20  # how many samples in a row user needs to hold a note
noteHeldCurrently = 0  # keep track of how long current note is held
noteHeld = ""  # string of the current note

centTolerance = 30  # how much deviance from proper note to tolerate
   
try:
    while True:
        if not q.empty():
            b = q.get()
            print("{} held for: {} and note CURRENTLY: {}".format(b['Note'], noteHeld,noteHeldCurrently),'\r', end='')           
            if b['Note'] == noteHeldCurrently:
                noteHeld += 1
                if noteHeld == noteHoldLength:
                    if not have_low:
                        low_note = noteHeldCurrently
                        have_low = True
                        # high = b['Note']
                        print("Sing a High Note")
                    else:
                        print("{} held for: {} and note CURRENTLY: {}".format(b['Note'], noteHeld,noteHeldCurrently),'\r', end='')
                        if int(noteHeldCurrently[-1]) <= int(low_note[-1]):
                            noteHeld = 0  # we're holding a lower octave note
                        elif int(noteHeldCurrently[-1]) and not high_note:
                            high_note = noteHeldCurrently
                            have_high = True
                            print("Vocal range: {} to {}".format(low_note,high_note))
            else:
                noteHeldCurrently = b['Note']
                noteHeld = 1
except KeyboardInterrupt:
    print("Keyboard interrupt received. Exiting...")     
df = pd.read_csv("csv\\Shape Of You.csv")
print(max(df.frequency),min(df.frequency))
#if ((abs(high_note-max(df.frequency))//max(df.frequency))<=1):

