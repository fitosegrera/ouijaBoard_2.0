#!/bin/bash

#This script is executed from python and uses SOX to record a .flac audio file from the microphone.
#It starts recording after detecting at least 0.1 seconds of noise and stops after 1.5 second of silence. 
#Sensitivity is set to 1%.

echo "Recording..."
sox -r 16000 -t alsa default voice.flac silence 1 0.1 1% 1 1.5 1%



	