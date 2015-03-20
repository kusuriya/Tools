#!/usr/bin/env sh
#giftranslate.sh video.mkv anim.gif "0:00" 25
#In order <video source> <Output Name> <Start time> <Duration in seconds>

start_time=$3
duration=$4
palette="/tmp/palette.png"
filters="fps=15,scale=320:-1:flags=lanczos"

#Work, Work, Work
ffmpeg -v warning -ss $start_time -t $duration -i $1 -vf "$filters,palettegen" -y $palette
ffmpeg -v warning -ss $start_time -t $duration -i $1 -i $palette -lavfi "$filters [x]; [x][1:v] paletteuse" -y $2
