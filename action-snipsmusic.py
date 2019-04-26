#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from snipsTools import SnipsConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io
import databasefuncs as dbfunks
import vlc

CONFIG_INI = "config.ini"

# If this skill is supposed to run on the satellite,
# please get this mqtt connection info from <config.ini>
# Hint: MQTT server is always running on the master device
MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

class Template(object):
    """Class used to wrap action code with mqtt connection

        Please change the name refering to your application
    """

    def __init__(self):
        # get the configuration if needed
        try:
            self.config = SnipsConfigParser.read_configuration_file(CONFIG_INI)
        except :
            self.config = None

        # start listening to MQTT
        self.start_blocking()

    # --> Sub callback function, one per intent
    def intent_1_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print ('[Received] intent: {}'.format(intent_message.intent.intent_name))
        songname = str(intent_message.slots.songName)
        snipssongname = intent_message.slots.songName
        # if need to speak the execution result by tts
        ## hermes.publish_start_session_notification(intent_message.site_id, songname[0].raw_value, "")
        #hermes.publish_start_session_notification(intent_message.site_id, "Action1 has been done", "")
        try:
            dbfunks.dbConnect()
            song = dbfunks.getSong('war pigs')
            songPath = song[1]
            print("song is " + song[1])
            #songPath = 'Music/Beck/Loser.mp3'
            #songPath = 'file:////var/lib/snips/skills/snipsmusicplayer/Loser.mp3'
            instance = vlc.Instance('--aout=alsa')
            #instance = vlc.Instance() 
            p = instance.media_player_new()
            m = instance.media_new_path(songPath)
            p.set_media(m)
            p.play()
            print(p.get_state())
            while True:
                 pass
            #p.pause()
            vlc.libvlc_audio_set_volume(p, 0)  # volume 0..100
        except Exception as e:
           # hermes.publish_start_session_notification(intent_message.site_id, snipssongname[0].raw_value, "") 
            #hermes.publish_start_session_notification(intent_message.site_id, e, "")
           print("Error: " + str(e))

    def intent_2_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print ('[Received] intent: {}').format(intent_message.intent.intent_name)

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, "Action2 has been done", "")

    def intent_3_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print ('[Received] intent: {}').format(intent_message.intent.intent_name)

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, "Action3 has been done", "")

    # More callback function goes here...

    # --> Master callback function, triggered everytime an intent is recognized
    def master_intent_callback(self,hermes, intent_message):
        coming_intent = intent_message.intent.intent_name
        if coming_intent == 'mike_dh_mount:playMeASong':
            self.intent_1_callback(hermes, intent_message)
        if coming_intent == 'mike_dh_mount:playArtist':
            self.intent_2_callback(hermes, intent_message)
        if coming_intent == 'mike_dh_mount:songAlbums':
            self.intent_3_callback(hermes, intent_message)

        # more callback and if condition goes here...

    # --> Register callback function and start MQTT
    def start_blocking(self):
        with Hermes(MQTT_ADDR) as h:
            h.subscribe_intents(self.master_intent_callback).start()

if __name__ == "__main__":
    Template()
