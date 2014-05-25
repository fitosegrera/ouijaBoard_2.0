#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2  # For doing https POST
import subprocess  # This library is for calling shell scripts from within python
import simplejson as json  # for handling JSON objects - in this case the return from google's API
import os


class ouija:

    def voiceRecognition(self, apiKey):
        subprocess.call(['./googleSpeech.sh'])
        print '================================'
        f = open('voice.flac')
        audioFile = f.read()
        f.close()
        lang_code = 'en-US'
        googl_speech_url = \
            'https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key=' \
            + apiKey
        hrs = {'Content-type': 'audio/x-flac; rate=16000'}
        req = urllib2.Request(googl_speech_url, data=audioFile,
                              headers=hrs)
        p = urllib2.urlopen(req)

        # -----------------------
        # For some reason the google speech API returns 2 json objects (the first one is empty)
        # and parsing with the json library was breaking the code...
        # I solved the issue writing a .txt file with the json data and deleting the first json object in the stream...
        # As follows:

        textFile = open('data.txt', 'a+')  # the +r makes allows to read and write over the .txt file
        textFile.write(p.read())  # we write the content of the https request to the data.txt file
        textFileClean = textFile.readlines()  # Reads the .txt file as a list
        textFile.close()
        print 'RAW-DATA:'
        print p.read()
        print '================================'

        del textFileClean[0:1]  # delete the first line of the list (index 0)

        jsonString = ''.join(textFileClean)  # converts the LIST into a STRING

        # -----------------------
        # Parsing the CLEAN JSON data:

        data = json.loads(jsonString)  # Loads the converted and cleaned data as a JSON object
        print data['result'][0]['alternative'][0]['transcript']  # prints only the transcript element from the JSON object

        os.remove('voice.flac')  # This line deletes the audio file once the operation is done
