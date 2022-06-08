import spotipy
from bs4 import BeautifulSoup
import requests
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

APP_ID = "YOUR_APP_ID"
SECRET = "YOUR_SECRET"
TOKEN = "YOUR_ACCESS_TOKEN"

billboard_url = "https://www.billboard.com/charts/hot-100"
spotify_url = "https://accounts.spotify.com/authorize"

what_year = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")

response = requests.get(f"{billboard_url}/{what_year}")
billboard_webpage = response.text

soup = BeautifulSoup(billboard_webpage, "html.parser")
titles = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
song_list = [title.getText() for title in titles]


redirect_uri = "https://example.com"
scope="playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=APP_ID,
                                        client_secret=SECRET,
                                        redirect_uri=redirect_uri,
                                        scope=scope,
                                        show_dialog=True,
                                        cache_path="token.txt"
                                       ))


user_id = sp.current_user()["id"]

song_uris = []
year = what_year.split("-")[0]
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{what_year} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)