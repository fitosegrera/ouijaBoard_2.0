#!/bin/bash

echo "Recording... Press Ctrl+C to Stop."
ffmpeg -f alsa -ac 2 -ar 44100 -i pulse voice.flac 

	