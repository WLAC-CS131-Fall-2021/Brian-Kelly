from midiutil import MIDIFile 
import random


notes = 96 
count = time = track = channel = 0 
duration = 1 
volume = 127 
tempo = 120 

MyMIDI = MIDIFile(1) 
MyMIDI2 = MIDIFile(2) 

MyMIDI.addTrackName(track,time,"Drum Track") 
MyMIDI2.addTrackName(track,time,"Rhythm Track") 

MyMIDI.addTempo(track,time,tempo) 
MyMIDI2.addTempo(track,time,tempo)


def fib_nr(n):
    num1 = 0
    num2 = 1
    term = 0
    for i in range(n):
        num1 = num2
        num2 = term
        term = num1 + num2
    return term


nterms = 16 
f = []
print_f = []

for i in range(0,nterms): 
    f.append(fib_nr(i)%16) #mod 16 to keep from going out of range of number of kick drum patterns
    print_f.append(fib_nr(i))



print("Fibonacci #'s:\n", print_f)
print("Fibonacci #'s with % 16:\n", f, "\n")
i=36 
beats =( 
    [i,i,i,i], 
    [i,i,i,0], 
    [i,i,0,i], 
    [i,i,0,0], 
    [i,0,i,i], 
    [i,0,i,0], 
    [i,0,0,i], 
    [i,0,0,0], 
    [0,i,i,i], 
    [0,i,i,0], 
    [0,i,0,i], 
    [0,i,0,0], 
    [0,0,i,i], 
    [0,0,i,0], 
    [0,0,0,i], 
    [0,0,0,0], 
) 



metal_r=[24,26,27,29,31,32,35,36] 
metal_r2 =[36,38,39] #43,45,46,48,50,51,54,55 
scale = [50, 53, 57, 62, 65, 69] 
vel = [63,63,64,63]

melody1 = [] 
#set melody1 
for i in (range(0, 16)): 
    m = random.choice(metal_r2) 
    melody1.append(m) 

#with .25, the kicks are 1/16th notes. 16 kick notes in one bar ( 4 notes)  
def write_kick_with_rhythm(): 
    kick_note = 36 
    time = 0 
    count = 0  

    for i in range(0,int(notes)): 
        n = beats[f[count%16]] 
        
        if i < 16:
            print("Beat ", f[i], n)
        xx = random.choice (metal_r2)  

        for idx in (n): 
            MyMIDI.addNote(track,channel,idx,time,duration,volume) 

            if i < notes*(1/3) or i >= notes*(2/3): 
                if count%4 == 2: 
                    MyMIDI2.addNote(track,channel,metal_r2[count%3],time,duration,64) 
                if idx!= 0: 
                    MyMIDI2.addNote(track,channel,metal_r[count%3],time,duration,63) 
                time+=.25 
            if i >=notes*(1/3) and i < notes*(2/3): 
                if idx != 0: 
                    MyMIDI2.addNote(track,channel,melody1[count%16],time,.25,vel[count%3]) 
                    MyMIDI2.addNote(track,channel,melody1[count%16],time+.50,.25,vel[count%3]) 
                else: 
                    MyMIDI2.addNote(track,channel,metal_r[count%3],time,duration,63) 
                time+=.25 
        count+=1 
def write_snare(): 
    snare_note = 38 
    time = 2 
    count = 0

    for i in range(0,int(notes/4)): 
        MyMIDI.addNote(track,channel,snare_note,time,duration,volume) 
        time+=4 
def write_ride(): 
    time = 0 
    ride_note = 46 
 
    for i in range(0,notes): 
        MyMIDI.addNote(track,channel,ride_note,time,duration,volume) 
        time+=1 

write_kick_with_rhythm() 
write_snare() 
write_ride() 

binfile = open("drums.mid",'wb') 
binfile2 = open("rhythm.mid",'wb') 

MyMIDI.writeFile(binfile) 
MyMIDI2.writeFile(binfile2) 

binfile.close() 
binfile2.close() 



 

 