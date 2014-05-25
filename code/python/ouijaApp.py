#!/usr/bin/python
# -*- coding: utf-8 -*-

from ouijaClass import ouija

ouija = ouija()

apiKey = 'AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw'  # Google API key for voice recognition

ouija.voiceRecognition(apiKey)
