import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime


def lambda_handler(event, context):
    client_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')
    
    client_credentials_manager = SpotifyClientCredentials(client_id = client_id , client_secret= client_secret )
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    
    playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbLZ52XmnySJg"
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    
    #getting data in json format
    spotify_data = sp.playlist_tracks(playlist_URI)
    
    client = boto3.client("s3")
    
    filename = "spotify_raw" + str(datetime.now()) + ".json"
    
    client.put_object(
        Bucket = "de-spotify-etl",
        Key= "extracted_data/to_process/" + filename,
        Body= json.dumps(spotify_data)
        )