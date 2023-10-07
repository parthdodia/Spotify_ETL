# Spotify_ETL

For this project, the data was collected from Spotify using Spotify’s API and ‘spotipy’ library.
The data is on top 50 songs in India (ranked weekly)

https://open.spotify.com/playlist/37i9dQZEVXbLZ52XmnySJg

Services used:
S3, IAM, Glue, Lambda, Athena, EventBridge

Process:
1. Created Spotify developer account to generate API keys.
2. Assigned roles and policies for the services used thorough IAM.
3. Created custom python package and generated custom layer to support spotipy library in AWS.
4. Coded function to extract raw data using Spotify API and ‘spotipy’ python library.
5. Automated data extraction using lambda triggers and EventBridge for a specified time and store data in ‘raw_data’ folder in S3 bucket.
6. Executed transform function to convert the raw data into 3 csv files – album, artist, songs in S3
7. Automated the process of transform function and to copy the transformed files into ‘processed_data’ folder and delete the data from ‘raw_data’ folder.
8. Utilized Glue crawlers to infer schema and generate tables from the csv files.
9. Queried the database using Athena to generate insights.

It was a great experience using API to collect data and then transform this raw data into legible data using AWS. This was a fun project as I was able to work with real time data which keeps on updating.


Spotify Developer : https://developer.spotify.com 

Python Custom Package : https://www.youtube.com/watch?v=lrEAu75zhNI

## Architecture Diagram

![Architecture Diagram](https://github.com/ParthDodia/Spotify_ETL/assets/88946343/7a7378fb-8478-4501-a271-dc04e76526ae)
