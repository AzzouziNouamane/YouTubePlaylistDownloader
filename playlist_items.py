# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlistItems.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

import sys
import json

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main(youtube, playlistID):

    request = youtube.playlistItems().list(
        part="contentDetails",
        maxResults = 25,
        playlistId= playlistID
    )
    response = request.execute()

    itemsCount = len(response['items'])
    print(itemsCount)

    videoId = request.execute()['items'][itemsCount-1]['contentDetails']['videoId']
    print(videoId)
    return videoId

#lastVideoId = 

if __name__ == "__main__":
    main()