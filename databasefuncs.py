#!/usr/bin/python3
import mysql.connector as mariadb
from mysql_dbconfig import read_db_config

cursor = "" 
# dbuser = "root"
# dbpasswrd = "eaGL3s!"
db_config = read_db_config()

def dbConnect():
    try:
        mariadb_connection = mariadb.connect(**db_config)
        #mariadb_connection = mariadb.connect(user='" + *dbuser + "', password='" + *dbpasswrd + "', database='snips_music')
        cursor = mariadb_connection.cursor()
       # deleteDB()
       # createMusicDB()
    except mariadb.Error as error:
       # createMusicDB()
        print(error)

def createMusicDB():
    mariadb_connection = mariadb.connect(**db_config)
    #mariadb_connection = mariadb.connect(user='" + dbuser + "', password='" + dbpasswrd + "')
    cursor = mariadb_connection.cursor()
    try:
        cursor.execute("Create database snips_music")
        print("Snips Music DB created succesfully!")   
    except:
        print("There was an issue creating the database")

    try:
        createArtistTable()
    except:
        print("Error trying to create Artist table")

    try:
        createAlbumTable()
    except:
        print("Error trying to create Album table")

    try:
        createSongTable()
    except:
        print("Error trying to create Song table")

    finally:
        mariadb_connection.close()

def deleteDB():
    try:
        mariadb_connection = mariadb.connect(**db_config)
        #mariadb_connection = mariadb.connect(user='" + dbuser + "', password='" + dbpasswrd + "', database='snips_music')
        cursor = mariadb_connection.cursor()
        cursor.execute("drop database snips_music")
    except:
        print("There was an issue removing the old database")

def createArtistTable():
    try:
        mariadb_connection = mariadb.connect(**db_config)
        #mariadb_connection = mariadb.connect(user='" + dbuser + "', password='" + dbpasswrd + "', database='snips_music')
        cursor = mariadb_connection.cursor()
        cursor.execute("create table tblArtists(artistID int(10) not null auto_increment, artistName varchar(50) not null, constraint artist_pk primary key (artistID));")
    except:
        print("There was an issue creating Artist table")

    finally:
        mariadb_connection.close()

def createAlbumTable():
    try:
        mariadb_connection = mariadb.connect(**db_config)
        #mariadb_connection = mariadb.connect(user='" + dbuser + "', password='" + dbpasswrd + "', database='snips_music')
        cursor = mariadb_connection.cursor()
        cursor.execute("create table tblAlbums(albumID int(10) not null auto_increment, artistID int(10) not null, albumName varchar(50) not null, constraint album_pk primary key (albumID));")
    except:
        print("There was an issue creating Album table")

    finally:
        mariadb_connection.close()


def createSongTable():
    try:
        mariadb_connection = mariadb.connect(**db_config)
        #mariadb_connection = mariadb.connect(user='" + dbuser + "', password='" + dbpasswrd + "', database='snips_music')
        cursor = mariadb_connection.cursor()
        cursor.execute("create table tblSongs(songID int(10) not null auto_increment, albumID int(10) not null, songName varchar(50) not null, songPath varchar(300), constraint song_pk primary key (songID));")
    except:
        print("There was an issue creating Song table")

    finally:
        mariadb_connection.close()

def getArtist(artist_Name):
    mariadb_connection = mariadb.connect(**db_config)
    #mariadb_connection = mariadb.connect(user='" + dbuser + "', password='" + dbpasswrd + "', database='snips_music')
    cursor = mariadb_connection.cursor()
    cursor.execute("select ArtistName from tblArtists where artistName=%s", (artist_Name,))
    for artistName in cursor:
        print("Artist Name: {}").format(artistName)

def getAlbum(album_Name):
    mariadb_connection = mariadb.connect(**db_config)
    #mariadb_connection = mariadb.connect(user='" + dbuser + "', password='" + dbpasswrd + "', database='snips_music')
    cursor = mariadb_connection.cursor()
    cursor.execute("select albumName from tblAlbums where albumName=%s", (album_Name,))
    for albumName in cursor:
        print("Album Name: {}").format(albumName)

def getSong(song_Name):
    songrslt = ""
    songname = ""
    songpath = ""
    mariadb_connection = mariadb.connect(**db_config)
    #mariadb_connection = mariadb.connect(user='" + dbuser + "', password='" + dbpasswrd + "', database='snips_music')
    cursor = mariadb_connection.cursor()
#    sqlQuery = """select songName, songPath from tblSongs where songName = %s"""
    cursor.execute("select songName, songPath from tblSongs where songName=%s", (song_Name,))
    records = cursor.fetchall()
    for record in records:
    #    print("Song Name: {}").format(song_Name)
    #    return songName
        songname = record[0]
        songpath = record[1]
        songrslt = [songname, songpath]
    mariadb_connection.close()
    return songrslt

def insertArtist(artist_Name):
    mariadb_connection = mariadb.connect(**db_config)
    #mariadb_connection = mariadb.connect(user='" + dbuser + "', password='" + dbpasswrd + "', database='snips_music')
    cursor = mariadb_connection.cursor()
    sql = "Insert into tblArtists (artistName) values (%s)"
    #val = (artist_Name)
    #cursor.execute(sql, val)
    cursor.execute("Insert into tblArtists (artistName) values (%s)", (artist_Name,))
    lastID = cursor.lastrowid
    mariadb_connection.commit()
    return lastID

def insertAlbum(artist_id, album_Name):
    mariadb_connection = mariadb.connect(**db_config)
    #mariadb_connection = mariadb.connect(user='" + dbuser + "', password='" + dbpasswrd + "', database='snips_music')
    cursor = mariadb_connection.cursor()
    sql = "Insert into tblAlbums (artistID, albumName) values (%s,%s)"
    val = (artist_id, album_Name)
    cursor.execute("Insert into tblAlbums (artistID, albumName) values (%s,%s)", (artist_id, album_Name))
    lastalbumId = cursor.lastrowid
    mariadb_connection.commit()
    return lastalbumId

def insertSong(album_id, song_Name, song_Path):
    mariadb_connection = mariadb.connect(**db_config)
    #mariadb_connection = mariadb.connect(user='" + dbuser + "', password='" + dbpasswrd + "', database='snips_music')
    cursor = mariadb_connection.cursor()
    cursor.execute("Insert into tblSongs (albumID, songName, songPath) values (%s,%s, %s)", (album_id, song_Name, song_Path))
    mariadb_connection.commit()

def getAlbumID(album_name):
    mariadb_connection = mariadb.connect(**db_config)
    cursor = mariadb_connection.cursor()
    cursor.execute("Select albumID from tblAlbums where albumName = %s", (album_name,))
    records = cursor.fetchall()
    albumrst = records
    mariadb_connection.close()
    return albumrst[0]

def getSongbyAlbumID(album_id):
    print("Getting Album ID")
    print(album_id)
    mariadb_connection = mariadb.connect(**db_config)
    cursor = mariadb_connection.cursor()
    print("Time to query")
    print(str(album_id[0]))
    songAlbumID = album_id[0]
    print(str(songAlbumID))
    cursor.execute("Select songPath from tblSongs where albumID = %s", (songAlbumID,))
    print("Query complete")
    records = cursor.fetchall()
    print("fetch records")
    for record in records:
    #    print("Song Name: {}").format(song_Name)
    #    return songName
        songpath = record
        print(songpath)
    mariadb_connection.close()
    return records
