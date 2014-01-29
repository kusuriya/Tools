#!/usr/bin/env python
import sys;
import os;

#Config
videoplayer = "/usr/local/bin/mplayer";
vidplayerargs = '-zoom -cache 1024 -autosync 30 -nobps -ni -forceidx -mc 0 -framedrop -y 480 -x 845';
ytdl = "/usr/local/bin/youtube-dl --cookies /tmp/cookies.txt -t --max-quality 34";
ytdlargs = '-g';

##############
# User, What r u doing?
# USER, STALP!
#
# Do not change anything
# below this line unless
# you really understand what
# you are doing
###############
#Commandline Var
ytvid = sys.argv[1];

#build command
vid = videoplayer + " " + vidplayerargs + " " + "$(" + ytdl + " " + ytdlargs + " " + "\"" + ytvid + "\")";

#execute
print("Starting: "+vid);
os.system(vid);
