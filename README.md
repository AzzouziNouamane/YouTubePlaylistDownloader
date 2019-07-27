# YouTubePlaylistDownloader

## Getting Started
This script's job is to check continuously any playlist on YouTube (You can track it by its ID), and to download it automatically to your desktop.
YouTubePlaylistDownloader uses YouTube's API to track your desired playlist, and uses PyTube to download the latest videos added to the playlist.


### Prerequisites
You'll need to install some libraries : 
```
pip install --upgrade google-api-python-client
pip install --upgrade google-auth-oauthlib google-auth-httplib2
pip install --upgrade pytube
```
### How to execute the script ?
The main .py file to execute the program is "main.py" obviously.

You'll need to enter 1 argument : The YouTube playlist's ID.
You will find it in the URL of the YouTube playlist, for example : 
```
https://www.youtube.com/playlist?list=PLwovxsrPtS6-fMl-8mlbQQtWI73KQdVO1
```
The YouTube Playlist's ID is **PLwovxsrPtS6-fMl-8mlbQQtWI73KQdVO1**

So, as an example, here is a line to copy/paste in your terminal in order to execute the script : 
```
python .\main.py PLwovxsrPtS6-fMl-8mlbQQtWI73KQdVO1
```

After that, a special token will be needed. You can obtain it after linking your Google Account with the script.

### Author
[AZZOUZI Nouamane](https://github.com/AzzouziNouamane)
