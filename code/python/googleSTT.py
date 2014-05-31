#!/usr/bin/python
# -*- coding: utf-8 -*-

# googleSTT.py
# Created by: fito_segrera 
# www.fii.to
# 05-07-14



import urllib  # For http request / google search
import urllib2  # For doing https POST
# This library is for calling shell scripts from within python
import subprocess
# for handling JSON objects - in this case the return from google's API
import simplejson as json
import os


class googleSTT:

    # This function takes the converted "SpeechToTexta" string and compares it with 
    # other strings (toCompare1, toCompare2, etc...) in order to find pairs
    def compareResults(self, returnedText, toCompare1, toCompare2):
        #TO DO!!!!!
        # IMPORTANT NOTE: 'toCompare1' MUST be compared to an array... If any of the array indexes contain the same word, THEN DO SOMETHING...
        if toCompare1 in returnedText:
            print 'Digital Soul Invoked!!!'
            print '================================'
        if returnedText == toCompare2:
            print 'YES I AM HERE'
            print '================================'

    # This function records voice using the microphone input, uploads
    # the .flac audio file to google Speech API transcripts that to text and
    # searches for it on google's search engine
    # The function takes 2 arguments: 
    # apiKey contains the GOOGLE SPEECH API Key
    # recognitionType contains the type of process that will be executed:
    #       'search' = Whatever the user Speaks it will be searched in google
    #      'compare' = Whatever the user Speaks will NOT be searched... 
    #                  It will be compared to the contents of an array to see if matches an specific voice command

    def voiceRecognitionAndSearch(self, apiKey, recognitionType):
        subprocess.call(['./googleSpeech.sh'])
        print '================================'
        f = open('voice.flac')
        audioFile = f.read()
        f.close()
        lang_code = 'en-US'
        googl_speech_url = 'https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key=' + apiKey
        hrs = {'Content-type': 'audio/x-flac; rate=16000'}
        req = urllib2.Request(googl_speech_url, data=audioFile, headers=hrs)
        p = urllib2.urlopen(req)

        # -----------------------
        # For some reason the google speech API returns 2 json objects (the first one is empty)
        # and parsing with the json library was breaking the code...
        # I solved the issue writing a .txt file with the json data and deleting the first json object in the stream...
        # As follows:

        rawData = p.read()
        print 'RAW-DATA:'
        print rawData
        print '================================'
        print 'CLEAN-DATA:'
        # removes the empty "{"result":[]}" object that comes in the json
        # string
        textFileClean = rawData.replace("""{"result":[]}""", '')
        print textFileClean
        print '================================'

        # -----------------------
        # Parsing the CLEAN JSON data:

        # Loads the converted and cleaned data as a JSON object
        data = json.loads(textFileClean)
        parsedData = data['result'][0]['alternative'][0]['transcript']
        # prints only the transcript element from the JSON object
        print 'FIRST TRANSCRIPT RESULT'
        print parsedData
        print '================================'

        # Read through all the json object and store all the 'transcript' items in an array called 'allData'
        allData = []
        itemsCounter = 0
        print 'ALL TRANSCRIPTS'
        for items in data['result'][0]['alternative']:
            allData.append(items['transcript'])
            print allData[itemsCounter]
            itemsCounter += 1

        # This line deletes the audio file once the operation is done
        os.remove('voice.flac')

        # ------------------------
        # Searching the returned text in google using urllib http request with the following link
        # http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=TEXT_TO_SEARCH_GOES_HERE

        # encode the clean data for searching with google... eg. 'hello world' --> 'hello%20world'
        # Spaces are replaced with %20
        encodedData = urllib.quote(parsedData)
        print '================================'
        print 'ECODED-DATA(for search):'
        print encodedData
        print '================================'

        rawSearch = urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=' + encodedData).read()

        # Uncomment the next 3 lines if you wish to print the RAW google search Results...
        
        #print 'RAW-SEARCH:'
        #print rawSearch
        #print '================================'

        jsonSearch = json.loads(rawSearch)  # load json to variable
        # Parse the jason object and get the specific item
        cleanSearch = jsonSearch['responseData']['results'][0]['content']
        print 'CLEAN-RESULT:'
        print cleanSearch

        # if the argument recognitionType from the function is 'search' then return just 
        # the first 'transcript' item of the JSON string 
        if recognitionType == 'search':
            return parsedData
        # if the argument recognitionType from the function is 'compare' then return an
        # array containing all the 'transcript' items of the JSON string
        if recognitionType == 'compare':
            return allData
