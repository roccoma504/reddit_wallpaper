#!/usr/bin/python

# This script changes the wallpaper of the current OSX desktop. It will change the wallpaper of the desktop on each screen but not each desktop.

from AppKit import NSWorkspace, NSScreen
from Foundation import NSURL
import os
import praw
import urllib

# Define the reddit object.
r = praw.Reddit(user_agent='User-Agent: osx:com.frocco.reddit_wallpaper:v0.1 (by /u/roclobster)')

# Retrieve and save the top image of /r/WQHD_Wallpaper
testfile = urllib.URLopener()
testfile.retrieve(list(r.get_subreddit('WQHD_Wallpaper').get_top(limit=1))[0].url, "reddit_wallpaper.jpg")

# Generate a fileURL for the desktop picture
file_url = NSURL.fileURLWithPath_(os.getcwd() + "/reddit_wallpaper.jpg")

# Get shared workspace
ws = NSWorkspace.sharedWorkspace()

# Iterate over all screens
for screen in NSScreen.screens():
    # Tell the workspace to set the desktop picture
    (result, error) = ws.setDesktopImageURL_forScreen_options_error_(file_url, screen, {}, None)
    if error:
        print error
        exit(-1)