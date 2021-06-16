import os
from pathlib import Path
import lyricsgenius
import sys
import concurrent.futures


ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent


 
class Genius:
  def __init__(self, client_access_token):
    self._api = lyricsgenius.Genius(client_access_token)
 
  def scrape_artist(self, artist_name: str, max_songs=50):
    artist = self._api.search_artist(artist_name, max_songs)
    artist_path = Path(Path(ROOT_DIR), 'data', artist.name)
    os.makedirs(artist_path, exist_ok=True)
    for song in artist.songs:
       #song.save_lyrics(filename=artist.songs)
       #song.save_lyrics(filename=artist.songs)
       with open(Path(artist_path, f'{song.title}.txt'), 'w', errors='ignore') as f:
         f.write(song.lyrics)


genius = Genius("f2ANcY9V9jGEpVTkdN6DbwQ2i7XylsmRxba61JUkP3rE00o81J1-Fz_o0xgNiqJ3")
with open(Path(ROOT_DIR, 'data', 'rappers.txt', errors='ignore')) as f:
    for rapper in [line.strip() for line in f.readlines()]:
        genius.scrape_artist(rapper)

rappers = open(Path(ROOT_DIR, 'data', 'rappers.txt', errors='ignore')).read().splitlines()
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(genius.scrape_artist, rappers)