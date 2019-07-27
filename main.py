# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlists.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

import sys
import playlist_items
import apidownload_test
import time

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

myURL = sys.argv[1]
urlSplit = myURL.split('=')
idPlayList = urlSplit[1]
youtube = 'test'


def getting_started():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyBfL8zCeNuFUrbIu_uTEtBQeWt0N2ZE4ic"
    global youtube
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

def main():
    print(youtube)
    request = youtube.playlists().list(
        part="contentDetails",
        id = idPlayList,
        maxResults=25,
    )
    response = request.execute()['items'][0]['contentDetails']['itemCount']
    print(response)
    return response

if __name__ == "__main__":
    getting_started()
    currentItems = main()
    
    while(True):
        if main() < currentItems:
            currentItems = main()

        if main() > currentItems: 
            currentItems = main()
            print(playlist_items.main(youtube))
            apidownload_test.downloadVideo(playlist_items.main(youtube))
        time.sleep(10)
