import sys
 
genius = Genius(sys.argv[1])
with open(Path(ROOT_DIR, 'data', 'rappers.txt')) as f:
    for rapper in [line.strip() for line in f.readlines()]:
        genius.scrape_artist(artist_name)