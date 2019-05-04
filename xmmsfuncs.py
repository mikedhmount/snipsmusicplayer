#!/usr/bin/python3

import subprocess
from word2number import w2n

def playSong():
    subprocess.check_call(['xmms2', 'play'])

def stopSong():
    subprocess.check_call(['xmms2', 'stop'])

def addSong(songPath):
    cmd = ['xmms2', 'add', '-f', songPath]
    subprocess.check_call(cmd)

def listSongs():
    subprocess.check_call(['xmms2', 'list'])

def clearSongs():
    subprocess.check_call(['xmms2', 'clear'])

def getCurrent():
    p = subprocess.check_output(['xmms2', 'current'])
    p = str(p.decode().strip())
    #print(p)
    p = p.split(': ')
    #print(p[0])
    return p

def setVolume(volumeLevel):
    if "percent" in volumeLevel:
        volumeLevel = volumeLevel.replace(' percent', '%')
        print(volumeLevel)
        volumenum = volumeLevel[:-1]
        #print(w2n.word_to_num(volumeLevel))
        print(w2n.word_to_num(volumenum))
        volumeLevel = w2n.word_to_num(volumenum)
        print(str(volumeLevel) + "%")
        volumeLevel = str(volumeLevel) + "%"
    subprocess.check_call(['amixer', 'set', 'PCM', volumeLevel])

def volumeUp():
    subprocess.check_call(['amixer', 'set', 'PCM', '5db+'])

def volumeDown():
    subprocess.check_call(['amixer', 'set', 'PCM', '5db-'])

def pauseSong():
    subprocess.check_call(['xmms2', 'pause'])

def listPlaylist():
    subprocess.check_output(['xmms2', 'list'])

def sortSongs():
    subprocess.check_call(['xmms2', 'playlist', 'sort'])

def nextSong():
    subprocess.check_call(['xmms2', 'next'])

def prevSong():
    subprocess.check_call(['xmms2', 'prev'])

def clearPlaylist():
    subprocess.check_call(['xmms2', 'playlist', 'clear'])