ouijaBoard_2.0
==============

This Version of the ouija board uses a raspberry pi, python with wiringPi and google's speech API to operate. The reason why I developed this version is because the accuracy of google's API is superior than the one I achieved with pocketsphinx in the earlier version.

###Software Installation:

For instructions on how to set-up your raspberry pi from scratch follow my previous repository https://github.com/fitosegrera/ouijaBoard_1.0/edit/master/README.md

###Putting everything together

These python 2.7 libraries are needed:

sys /
os /
urllib2 /
json /
subprocess /

For recording the audio we are calling a shell script that uses sox to detect when there is certain threshold of noise and start recording from the microphone... Once the noise stops, so does the recording. This is the line we are using:

    sox -r 16000 -t alsa default voice.flac silence 1 0.1 1% 1 1.5 1%

