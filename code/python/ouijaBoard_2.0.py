#!/usr/bin/python
import sys
import os
import urllib2 #For doing https POST
import json #for handling JSON objects - in this case the return from google's API
import subprocess #This library is for calling shell scripts from within python

print "Press the 'r' key followed by ENTER to start capturing voice..."

while True:
    char = sys.stdin.read(1)
    #print 'You pressed %s' % char
    if char == 'r':
    	subprocess.call(['./googleSpeech.sh'])
    	print "/////////////////"

    	f = open("voice.flac")
    	flac_cont = f.read()
    	f.close()

    	lang_code='en-US'
    	googl_speech_url = 'https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key=AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw'
    	hrs = {'Content-type': 'audio/x-flac; rate=16000'}
    	req = urllib2.Request(googl_speech_url, data=flac_cont, headers=hrs)
    	p = urllib2.urlopen(req)
    	print p.read()
    	#j = json.load(p)
    	#ourResult = j['result'][0]['alternative']
    	#print ourResult
    	#os.remove('voice.flac') #This line deletes the audio file once the operation is done
