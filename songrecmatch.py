import pandas as pd
from vocalrange import q, get_current_note
from threading import Thread
t = Thread(target=get_current_note)
t.daemon = True
t.start()
low_note = ""
high_note = ""
have_low = False
have_high = True

noteHoldLength = 20  # how many samples in a row user needs to hold a note
noteHeldCurrently = 0  # keep track of how long current note is held
noteHeld = ""  # string of the current note

centTolerance = 20  # how much deviance from proper note to tolerate
if not q.empty():
    b = q.get()
    if b['Note'] == noteHeldCurrently:
        noteHeld += 1
        if noteHeld == noteHoldLength:
            if not have_low:
                low_note = noteHeldCurrently
                have_low = True
                high = b['Note']
            else:
                if int(noteHeldCurrently[-1]) <= int(low_note[-1]):
                    noteHeld = 0  # we're holding a lower octave note
                elif int(noteHeldCurrently[-1]) and not high_note:
                    high_note = noteHeldCurrently
                    have_high = True
        else:
            noteHeldCurrently = b['Note']
            noteHeld = 1
df = pd.read_csv("csv\\ShapeOfYou1.csv")
print(max(df.frequency),min(df.frequency),high_note,low_note)
#if ((abs(high_note-max(df.frequency))//max(df.frequency))<=1):

