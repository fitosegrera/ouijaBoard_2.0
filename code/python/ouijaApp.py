#!/usr/bin/python
# -*- coding: utf-8 -*-

#              _ _         _                         _
#             (_|_)       | |                       | |
#   ___  _   _ _ _  __ _  | |__   ___   __ _ _ __ __| |
#  / _ \| | | | | |/ _` | | '_ \ / _ \ / _` | '__/ _` |
# | (_) | |_| | | | (_| | | |_) | (_) | (_| | | | (_| |
#  \___/ \__,_|_| |\__,_| |_.__/ \___/ \__,_|_|  \__,_|
#              _/ |
#             |__/
#
# Ouija Board
# Code for controlling the ouija board (raspberry pi digital pins) and Google Search API
# Created by: fito_segrera 
# www.fii.to
# 05-07-14

from googleSTT import googleSTT # From the file googleSTT.py import the class googleSTT 

ouija = googleSTT()

# Google API key for voice recognition
apiKey = 'AIzaSyDT34UUHcNJ6lDTkj4EegMMpDn3FHaTSwY'
# apiKey = 'AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw'  # Google API key for
# voice recognition
recognitionType = 'search'
returnedText = ouija.voiceRecognitionAndSearch(apiKey, recognitionType)  # executes the function ouija.voiceRecognitionAndSearch(apiKey) and asignes the return value to the variable 'returnedText'
print returnedText

# This next part of the code takes the returned string and compares it with other strings to determine pairs...
toCompare1 = "invoke" # Voice command necessary to invoke the digital soul
toCompare2 = "are you there" # Voice command necessary to verify the presence of the digital soul
ouija.compareResults(returnedText, toCompare1, toCompare2)