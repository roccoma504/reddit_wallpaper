__author__ = 'rocco'

import os
import praw
import subprocess
import urllib

# Scripts to set the desktop image. This only sets the current desktop.
SET = """osascript -e 'tell application "Finder" to set desktop picture to POSIX file path'"""



# Refresh the dock to ensure the wallpaper is set.
REFRESH = """killall Dock"""


# Calls the scipts to set the desktop and refresh the dock.
def set_pic(path):
    subprocess.Popen([SET, str(path)], shell=True)
    subprocess.Popen(REFRESH, shell=True)


# Define the reddit object.
r = praw.Reddit(user_agent='User-Agent: osx:com.frocco.reddit_wallpaper:v0.1 (by /u/roclobster)')

# Retrieve and save the top image of /r/wallpapers
testfile = urllib.URLopener()
#print list(r.get_subreddit('WQHD_Wallpaper').get_top(limit=1))[0].url
testfile.retrieve(list(r.get_subreddit('wallpaper').get_top(limit=1))[0].url, "reddit_wallpaper.jpg")

print os.getcwd() + "/reddit_wallpaper.jpg"

# set the background using the absolute path of the image.
set_pic(os.getcwd() + "/reddit_wallpaper.jpg")

