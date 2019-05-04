#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
from hermes_python.hermes import Hermes
from hermes_python.ffi.utils import MqttOptions
from hermes_python.ontology import *
import io
import os
import xmmsfuncs

import databasefuncs as dbfunks

CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

class SnipsConfigParser(configparser.SafeConfigParser):
    def to_dict(self):
        return {section : {option_name : option for option_name, option in self.items(section)} for section in self.sections()}


def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, configparser.Error) as e:
        return dict()

def subscribe_intent_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    action_wrapper(hermes, intentMessage, conf)



def action_wrapper(hermes, intentMessage, conf):
     try:
        #Get ID of Album
        Albumname = intentMessage.slots.songAlbums
        dbfunks.dbConnect()
        print(Albumname[0].raw_value)
        song = dbfunks.getAlbumID(Albumname[0].raw_value)
        
        isPlaying = xmmsfuncs.getCurrent()
        if isPlaying[0] == 'Stopped':
            xmmsfuncs.clearPlaylist()

        #Get all songs via AlbumID
        songs = dbfunks.getSongbyAlbumID(song)
        for songpaths in songs:
            print("Here are your paths")
            print(songpaths[0])
            xmmsfuncs.addSong(songpaths[0])
        xmmsfuncs.sortSongs()
        xmmsfuncs.listSongs()
        
        xmmsfuncs.playSong()

     except Exception as e:
        print(e)

if __name__ == "__main__":
    mqtt_opts = MqttOptions()
    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent("mike_dh_mount:songAlbums", subscribe_intent_callback) \
         .start()
