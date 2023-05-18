# import pandas as pd
from getpitch import q, get_current_note
from threading import Thread
# import music21
import mysql.connector

def vocalrange():
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
                            low_note_f = b['Frequency']
                            have_low = True
                            # high = b['Note']
                            print("\nSing a High Note:")
                        else:
                            print("{} held for: {} and note CURRENTLY: {}".format(b['Note'], noteHeld,noteHeldCurrently),'\r', end='')
                            if int(noteHeldCurrently[-1]) <= int(low_note[-1]):
                                noteHeld = 0  # we're holding a lower octave note
                            elif int(noteHeldCurrently[-1]) and not high_note:
                                high_note = noteHeldCurrently
                                high_note_f = b['Frequency']
                                have_high = True
                                print("\nVocal range: {} to {} i.e {:.2f} to {:.2f}".format(low_note,high_note,low_note_f,high_note_f))
                else:
                    noteHeldCurrently = b['Note']
                    noteHeld = 1
    except KeyboardInterrupt:
        print("Keyboard interrupt received. Exiting...")
    low_note_f = 100.0
    high_note_f = 200.0
    mydb = mysql.connector.connect(host = "127.0.0.1", user = "root",password = "ankita", auth_plugin='mysql_native_password', database = "Pitch_Perfect")
    cur = mydb.cursor()
    sql = "UPDATE User SET low_note = %s, high_note = %s WHERE user_id=1" #User id must be matched with UI
    # fp = open("temp_vr.txt",'w')
    L = (low_note_f,high_note_f)
    cur.execute(sql,L)
    mydb.commit()
    print(cur.rowcount,"Record updated.") 
# fp.writelines(L) 
# fp.close()

if __name__=="__main__":
    vocalrange()