# https://stackoverflow.com/questions/27279864/generate-midi-file-and-play-it-without-saving-it-to-disk
# switch StringIO to BytesIO

from midiutil.MidiFile import MIDIFile
from io import BytesIO

# CREATE MEMORY FILE

memFile = BytesIO()
MyMIDI = MIDIFile(1)
track = 0
time = 0
channel = 0
pitch = 60
duration = 1
volume = 100
MyMIDI.addTrackName(track,time,"Sample Track")
MyMIDI.addTempo(track,time,120)

# WRITE A SCALE

MyMIDI.addNote(track,channel,pitch,time,duration,volume)
for notestep in [2,2,1,2,2,2,1]:
    time += duration
    pitch += notestep
    MyMIDI.addNote(track,channel,pitch,time,duration,volume)
MyMIDI.writeFile(memFile)

# PLAYBACK

import pygame
import pygame.mixer
from time import sleep

pygame.init()
pygame.mixer.init()
memFile.seek(0)  # THIS IS CRITICAL, OTHERWISE YOU GET THAT ERROR!
pygame.mixer.music.load(memFile)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    sleep(1)
print("Done!")
