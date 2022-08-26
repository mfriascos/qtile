#!/bin/sh

# systray 
nm-applet &

# systray battery icon
cbatticon -u 5 &
# systray volume
#volumeicon &

nitrogen --restore &
