#!/usr/bin/env python
import sys;
import os;

#Config
videoplayer = "/usr/local/bin/mplayer";
vidplayerargs = '-zoom -cache 1024 -vo x11';
ytdl = "/usr/local/bin/youtube-dl";
ytdlargs = ' -g ';

#Commandline Var
ytvid = sys.argv[1];

#build command
vid = videoplayer + " " + vidplayerargs + " " + "$(" + ytdl + " " + ytdlargs + " " + "'" + ytvid + "')";

#execute
print("starting"+ytvid);
os.system(vid);
