#!/usr/bin/python3

import subprocess

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
    subprocess.check_call(['amixer', 'set', 'PCM', volumeLevel])

def volumeUp():
    subprocess.check_call(['amixer', 'set', 'PCM, '5%+'])

def volumeDown():
    subprocess.check_call(['amixer', 'set', 'PCM', '5%-'])
