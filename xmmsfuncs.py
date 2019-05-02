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

