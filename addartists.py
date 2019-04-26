#!/usr/bin/python3
import os
import io
import databasefuncs as dbfunks

searchpathname = '/var/lib/snips/skills/snipsmusicplayer/Music/'
file = open("Artists.txt", "w")
file2 = open("Albums.txt", "w")
file3 = open("Songs.txt", "w")
dbfunks.dbConnect()
dbfunks.deleteDB()
dbfunks.createMusicDB()

for filename in os.listdir(searchpathname):
    #List top level directories under searchpath - Artists
        lastID = dbfunks.insertArtist(filename)
        file.write(filename + '\n')
        for filename2 in os.listdir(searchpathname + filename):
            #List 2nd level under search path - Albums
            lastalbumid = dbfunks.insertAlbum(lastID, filename2)
            file2.write(filename2 + '\n')
            #continue
            for filename3 in os.listdir(searchpathname + filename + '/' + filename2 + '/'):
                if filename3.endswith(".mp3"):
                    songName = filename3.replace(".mp3", "").strip()
                    songPath = searchpathname + filename + '/' + filename2 + '/' + filename3.strip()
                    dbfunks.insertSong(lastalbumid, songName, songPath)
                    file3.write(songName + '\n')
                    continue
                else:
                    continue
        continue
    
