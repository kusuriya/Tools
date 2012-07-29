#!/usr/bin/env python
import sys;
import os;

#Config
videoplayer = "/usr/local/bin/mplayer";
vidplayerargs = '-zoom -cache 1024 -autosync 30 -nobps -ni -forceidx -mc 0 -framedrop';
ytdl = "/usr/local/bin/youtube-dl --cookies /tmp/cookies.txt -t";
ytdlargs = '-g --max-quality 44';

#Commandline Var
ytvid = sys.argv[1];

#build command
vid = videoplayer + " " + vidplayerargs + " " + "$(" + ytdl + " " + ytdlargs + " " + "\"" + ytvid + "\")";

#execute
print("starting "+vid);
os.system(vid);
